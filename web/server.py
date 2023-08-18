from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# 랜덤 포레스트 모델 로드
rf_model = joblib.load("C:/Users/kjr07/세미프로젝트/randomforest_real.pkl")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # 사용자가 입력한 데이터 가져오기
        input_data = [
            float(request.form['1hr_rainfall']),
            float(request.form['daily_rainfall']),
            float(request.form['slope']),
            float(request.form['altitude']),
            float(request.form['impervious_surface']),
            float(request.form['green_area']),
            float(request.form['river_area']),
            float(request.form['river_count']),
            float(request.form['manhole_count']),
            float(request.form['rain_barrels_count']),
            float(request.form['rain_pump_count'])
        ]

        # 모델로 예측 수행
        prediction = rf_model.predict(np.array([input_data]))
        prediction_probability = rf_model.predict_proba(np.array([input_data]))

        # 결과 출력
        if prediction == 1:
            result = "침수 피해가 발생할 가능성이 높습니다."
        else:
            result = "침수 피해가 발생할 가능성이 낮습니다."

        return render_template('index.html', result=result, probability=prediction_probability[0][1])

if __name__ == '__main__':
    app.run(debug=True)
