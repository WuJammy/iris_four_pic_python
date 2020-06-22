import pandas as pd
import matplotlib.pyplot as plt

# 畫出直條圖四張直方圖，採用4個子圖同時顯示方式, 四張子圖之x軸為iris資料的四個輸入特徵，直方圖組數可自訂但必須大於10

df = pd.read_csv("iris.csv",index_col="class",encoding = "utf8")#讀取iris資料，並將類別設為索引值

petal_length = df["petal length"]#取出petal長度的所有值
petal_width = df["petal width"]#取出petal寬度的所有值
sepal_length = df["sepal length"]#取出sepal長度的所有值
sepal_width = df["sepal width"]#取出sepal寬度的所有值

plt.subplots_adjust(hspace=0.8, wspace=0.5)#調整四個子圖的間距

plt.subplot(221)#設定Petal Length的子圖在左上角
plt.hist(sepal_length, 15)#畫出直方圖，並設定組數為15
plt.xlabel("length")#顯示x座標代表的文字
plt.ylabel("numbers")#顯示y座標代表的文字
plt.title("Petal Length")#顯示標題的文字

plt.subplot(222)#設定Petal Width的子圖在右上角
plt.hist(sepal_width, 15)#畫出直方圖，並設定組數為15
plt.xlabel("length")#顯示x座標代表的文字
plt.ylabel("numbers")#顯示y座標代表的文字
plt.title("Petal Width")#顯示標題的文字


plt.subplot(223)#設定Sepal Length的子圖在左下角
plt.hist(petal_length, 15)#畫出直方圖，並設定組數為15
plt.xlabel("length")#顯示x座標代表的文字
plt.ylabel("numbers")#顯示y座標代表的文字
plt.title("Sepal Length")#顯示標題的文字

plt.subplot(224)#設定Sepal Width的子圖在右下角
plt.hist(petal_width, 15)#畫出直方圖，並設定組數為15
plt.xlabel("length")#顯示x座標代表的文字
plt.ylabel("numbers")#顯示y座標代表的文字
plt.title("Sepal Width")#顯示標題的文字
