# DataFrame 
# Serilerin yan yana gelmesinden oluşmuş tablolardır
# Görsel hale getirir

import pandas 
import numpy 

# öncelikle rastgele numpy dizisi(matris) oluşturalım 
print("-------------data = numpy.random.randn(4,3)------------------")
data = numpy.random.randn(4,3) # 4 satır , 3 sütun matris
print(data) 

print("-------------dataFrame = pandas.DataFrame(data)------------------")
dataFrame = pandas.DataFrame(data)
print(dataFrame)

# indeksleri nasıl değiştiririz : 
print("-------------yeniDataFrame = pandas.DataFrame(data , index=['Yasin' , 'Ersin' , 'Muhsin','Tahsin'] , columns=['a','b','c'])------------------")
yeniDataFrame = pandas.DataFrame(data , index=["Yasin" , "Ersin" , "Muhsin","Tahsin"] , columns=["a","b","c"])
print(yeniDataFrame)
print("-------------tablodan sütun çekme------------------")
print(yeniDataFrame["a"])  # [ ["a"] ] yaparsak sütun üzerinde isim(a) de yazıyor
print("-------------çoklu sütun çekme ------------------")
print(yeniDataFrame[["a","b"]])

# peki bir satırı nasıl getiricez : 
print("-------------tablodan satır çekme(yeniDataFrame.loc['Yasin'])------------------")
print(yeniDataFrame.loc["Yasin"]) # [ ["Yasin"] ] yaparsak düzgün gösterimde geliyor
print("-------------tablodan satır çekme(yeniDataFrame.loc[['Yasin']])------------------")
print(yeniDataFrame.loc[["Yasin"]])
print("-------------indeks ile satır çekme------------------")
print(yeniDataFrame.iloc[1]) # 1. indisdeki satırı getir.
