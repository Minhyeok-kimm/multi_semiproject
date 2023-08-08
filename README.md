# 세미 프로젝트

## 주제

서울시의 집중호우에 의한 교통취약지 침수예보 예측

## 사용 데이터

### 1. 강수량

- 서울시 강우량 정보(10분 단위)
    - 서울열린데이터광장: [서울시 강우량 정보](http://data.seoul.go.kr/dataList/OA-1168/S/1/datasetView.do)
    - 2011~2020년 데이터 공공데이터포털 : [서울특별시_강우량 데이터](https://www.data.go.kr/data/15088760/fileData.do)

### 2. 지형

- 서울시 수치표고모델(DEM): 구별 평균 고도, 평균 경사도 추출에 이용
    - 국가공간정보포털: [수치표고모델(DEM)_90M](http://data.nsdi.go.kr/dataset/20001)

### 3. 지역 환경

- 녹지면적
    - 서울열린데이터광장: [서울시녹지현황(2018~2021)](https://data.seoul.go.kr/dataList/368/S/2/datasetView.do), [서울시 녹지대 위치정보 (좌표계: ITRF2000)(2022)](https://data.seoul.go.kr/dataList/OA-316/S/1/datasetView.do)
- 하수처리시설
    - 하수도정보시스템 : [2021-2018하수도통계](https://www.hasudoinfo.or.kr/stat/statRefList.do)
    - https://data.seoul.go.kr/dataList/506/S/2/datasetView.do
- 불투수면 데이터
    - 공공데이터포털: (서울특별시_자치구별 불투수면적 현황)[https://www.data.go.kr/data/15114478/fileData.do#tab-layer-file]
- 복개하천 갯수
    - [https://ko.m.wikipedia.org/wiki/파일:서울의_하천(Rivers_of_Seoul).png](https://ko.m.wikipedia.org/wiki/%ED%8C%8C%EC%9D%BC:%EC%84%9C%EC%9A%B8%EC%9D%98_%ED%95%98%EC%B2%9C%28Rivers_of_Seoul%29.png)
- 하천 면적
    - [서울시 토지현황 (지목별/법정동별) 통계> 데이터셋> 공공데이터 | 서울열린데이터광장 (seoul.go.kr)](https://data.seoul.go.kr/dataList/10582/S/2/datasetView.do#)

### 4. 하수관로 비율

- 서울열린데이터광장: [서울시 하수관로 수위현황](https://data.seoul.go.kr/dataList/OA-2527/S/1/datasetView.do)

### 5. 교통사고 데이터

- 도로교통공단 TASS(교통사고분석시스템): [일자별 시도, 시군구별 교통사고](https://taas.koroad.or.kr/sta/acs/exs/typical.do?menuId=WEB_KMP_OVT_UAS_PDS)