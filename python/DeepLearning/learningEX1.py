from sklearn.datasets import load_diabetes
import numpy as np
import matplotlib.pyplot as plt
# np.random.randn(1000)   난수 1000개 생성 (numpy.ndarray)
# plt.scatter(x,y)  산점도 찍기
# plt.plot([x1,x2],[y1,y2])  선 그리기 좌표 값은 x,y 둘 다 각자 2개씩 있어야 그려짐
# plt.show()  그래프 보여주기
diabetes = load_diabetes()
x = diabetes.data[:, 2]
y = diabetes.target
w = 1.0  # 가중치
b = 1.0  # 절편
# ==================================================== 가중치 업데이트 =================================================
y_hat = x[0] * w + b  # 예측값 찾기        훈련 데이터의 첫 번쨰 샘플 데이터

w_inc = w + 0.1  # 가중치 증가로 예측을 함
y_hat_inc = x[0]*w_inc + b  # 가중치 증가에 따른 변경된 예측값 구함
print(y_hat_inc)
w_rate = (y_hat_inc - y_hat)/(w_inc - w)
print(w_rate)  # 예측값 변동폭 구하기

w_new = w + w_rate  # 가중치 업데이트 (음,양수 전부 해당)
print(w_new)
# ==================================================== 절편 업데이트 =================================================
b_inc = b + 0.1  # 절편 증가
y_hat_inc = x[0] * w + b_inc  # 절편 증가로 인한 예측값 변동
print(y_hat_inc)

b_rate = (y_hat_inc - y_hat) / (b_inc - b)  # 절편 증가에 대한 변화율
print(b_rate)

b_new = b + b_rate  # 절편 업데이트
print(b_new)

# ==================================================== 오차 역전파 =================================================

# y_hat와 y의 차이를 이용해  w, b를 업데이트               (2022.02.01)                         60p. 까지 읽음

# x[0]일 때 w의 변화율 b의 변화율에 오차를 곱한 다음 w_new, b_new 업데이트
err = y[0] - y_hat  # 오차율
w_new = w + w_rate * err  # w_new 업데이트
b_new = b + b_rate * err  # b_new 업데이트
print(w_new, b_new)

# 두 번째 샘플 x[1]을 사용하여 오차를 구하고 새로운 w, b를 구한다.
y_hat = x[1] * w_new + b_new  # 예측 값을 두 번째 샘플을 이용해서 새로운 기울기와 새 절편에 대입해서 구함.
err = y[1] - y_hat  # 오차율을 두 번째 샘플 값일 때와 두 번째 샘플을 이용한 오차율 계산
w_rate = x[1]  # 61p. 참고
w_new = w_new + w_rate * err  # w_new 업데이트
b_new = b_new + 1 * err  # b_new 업데이트
print(w_new, b_new)

# ==============================전체 샘플 반복===============================================================

for x_i, y_i in zip(x, y):  # zip()은 여러 개의 배열에서 동시에 요소를 하나씩 꺼내주는 함수이다.
    y_hat = x_i * w + b
    err = y_i - y_hat
    w_rate = x_i
    w = w + w_rate * err
    b = b + b_rate * err
print(w, b)
