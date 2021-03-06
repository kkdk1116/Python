# -*- coding: utf-8 -*-
"""Threshold.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jOAShcIsMRyVwxwS48LHTWBSn4cRaiCo
"""

import numpy as np
from google.colab import drive


def act_tlu(out) :
  if(out > 0.0) :
      return 1.0
  return(0.0)


x = np.array([ [1.0, 0.0, 0.0], [1.0, 0.0, 1.0], [1.0, 1.0, 0.0], [1.0, 1.0, 1.0] ]) #x0, x1, x2    p0, p1, p2, p3    2차원 배열 선언     -입력-
t = np.array([0.0, 1.0, 1.0, 1.0]) # p0~p3 타겟     -출력-

lrate = 0.1

w = np.zeros(3)

w[0] = 0.5
w[1] = 0.2
w[2] = 0.7

for epoch in range (100):
  print("epoch %d", epoch)
  for i in range(4):
    out = w[0]*x[i][0] + w[1]*x[i][1] + w[2]*x[i][2]
    b = act_tlu(out)
    print(t[i], b, out)
    for j in range(3):
      w[j] = w[j] + lrate * (t[i]-b) *x[i][j]