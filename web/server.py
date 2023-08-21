from flask import Flask, render_template, request, flash
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)
app.secret_key = 'abcd'

# 모델 로드
model = joblib.load("model/LightGBMRegressor.pkl")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # 데이터를 입력하지 않은 경우 데이터 입력할 수 있도록 경고창 생성
        rainfall = request.form['1hr_rainfall']
        altitude = request.form['altitude']
        m = request.form['month']
        d = request.form['day']
        if rainfall == "" or altitude == "" or m == "" or d == "":
            flash('입력을 완료하고 예측버튼을 누르세요.')
            return render_template('index.html')
        
        # 사용자가 입력한 데이터 가져오기 + 데이터프레임 생성을 위한 dict 생성
        df_template = {
            '1hr_최대강수량':float(request.form['1hr_rainfall']),
            '해발고도':float(request.form['altitude']),
            '불투수면':float(request.form['impervious_surface']),
            '녹지면적율':float(request.form['green_area']),
            '하천면적율':float(request.form['river_area']),
            '복개하천개수':float(request.form['river_count']),
            '맨홀개수':float(request.form['manhole_count']),
            '빗물펌프개수':float(request.form['rain_pump_count']),
            'month':int(request.form['month']),
            'day':int(request.form['day']),
            '자치구_강남':0, '자치구_강동':0,
            '자치구_강북':0, '자치구_강서':0,
            '자치구_관악':0, '자치구_광진':0,
            '자치구_구로':0, '자치구_금천':0,
            '자치구_노원':0, '자치구_도봉':0,
            '자치구_동대문':0, '자치구_동작':0,
            '자치구_마포':0, '자치구_서대문':0,
            '자치구_서초':0, '자치구_성동':0,
            '자치구_성북':0, '자치구_송파':0,
            '자치구_양천':0, '자치구_영등포':0,
            '자치구_용산':0, '자치구_은평':0,
            '자치구_종로':0, '자치구_중':0, '자치구_중랑':0
        }
        
        # 구 데이터 받아오기
        gu = request.form['district']
        
        pred_df = pd.DataFrame(df_template, index=[0])
        
        # 선택한 구에만 1이 되도록 지정
        for i in list(pred_df.columns):
            if gu in i:
                pred_df[i] = 1
                break
        
        # 모델로 예측 수행
        prediction = model.predict(pred_df)

        # 결과 출력
        if prediction >= 0.8:
            result = "침수 피해가 발생할 가능성이 높습니다."
        else:
            result = "침수 피해가 발생할 가능성이 낮습니다."

        return render_template('index.html', result=result, probability=prediction)

if __name__ == '__main__':
    app.run(port=80, debug=True)
