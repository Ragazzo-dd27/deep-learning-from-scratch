# coding: utf-8
import matplotlib.pyplot as plt
from matplotlib.image import imread
import os

# 获取脚本所在目录的父目录（项目根目录），然后构建正确的路径
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
img_path = os.path.join(project_root, 'dataset', 'lena.png')
img = imread(img_path) # 画像の読み込み
plt.imshow(img)

plt.show()