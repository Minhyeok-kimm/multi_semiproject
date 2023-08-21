# -*- coding: utf-8 -*-

import pickle
from flask import Flask, render_template, request, jsonify
from flask import Flask, render_template, request, flash


app = Flask(__name__)
app.secret_key = '1234'


@app.route("/", methods=['GET', 'POST'])
def index():

    return render_template('index.html')


@app.route("/predict", methods=['GET', 'POST'])
def predict():
    result = ""
    prediction = ""
    if request.method == 'POST':
        # 데이터를 입력하지 않은 경우 데이터 입력할 수 있도록 경고창 생성
        rainfall = request.form['1hr_rainfall']
        altitude = request.form['altitude']
        m = request.form['month']
        d = request.form['day']
        if rainfall == "" or altitude == "" or m == "" or d == "":
            flash('입력을 완료하고 예측버튼을 누르세요.')
            return render_template('predict.html')

        # 사용자가 입력한 데이터 가져오기 + 데이터프레임 생성을 위한 dict 생성
        df_template = {
            '1hr_최대강수량': float(request.form['1hr_rainfall']),
            '해발고도': float(request.form['altitude']),
            '불투수면': float(request.form['impervious_surface']),
            '녹지면적율': float(request.form['green_area']),
            '하천면적율': float(request.form['river_area']),
            '복개하천개수': float(request.form['river_count']),
            '맨홀개수': float(request.form['manhole_count']),
            '빗물펌프개수': float(request.form['rain_pump_count']),
            'month': int(request.form['month']),
            'day': int(request.form['day']),
        }

        # 구 데이터 받아오기
        gu = request.form['district']

        pred_df = pd.DataFrame(df_template, index=[0])

        # 구별 모델 로드
        model = joblib.load(f"model/자치구_{gu}_model.pkl")

        # 모델로 예측 수행
        prediction = model.predict(pred_df)

        # 결과 출력
        if prediction >= 0.8:
            result = "침수 피해가 발생할 가능성이 높습니다."
        else:
            result = "침수 피해가 발생할 가능성이 낮습니다."

    return render_template('predict.html', result=result, probability=prediction)


if __name__ == '__main__':

    app.run(debug=True, port=8080)
