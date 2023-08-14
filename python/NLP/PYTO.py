import torch
import numpy as np


# https://tutorials.pytorch.kr/beginner/basics/tensorqs_tutorial.html

# 텐서 초기화


# 데이터로부터 직접 생성, 데이터 자료형은 자동으로 유추
data = [[1, 2], [3, 4]]
x_data = torch.tensor(data)
print(x_data)


# Numpy 배열로 생성
np_array = np.array(data)
x_np = torch.from_numpy(np_array)
print(x_np)
