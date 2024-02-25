# coding: utf-8
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__))) # どのようにフォルダ展開しても使用可能
# sys.path.append("..") # オリジナル表記 (Ch01をフォルダ展開した場合に使用)
# sys.path.append(".") # 別表記 (Deep-learning-from-scratchをフォルダ展開した場合に使用)
# print(sys.path)
from dataset import spiral
import matplotlib.pyplot as plt


x, t = spiral.load_data()
print('x', x.shape)  # (300, 2)
print('t', t.shape)  # (300, 3)

# データ点のプロット
N = 100
CLS_NUM = 3
markers = ['o', 'x', '^']
for i in range(CLS_NUM):
    plt.scatter(x[i*N:(i+1)*N, 0], x[i*N:(i+1)*N, 1], s=40, marker=markers[i])
plt.show()
