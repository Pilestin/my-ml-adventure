# Operasyonlar  
# Eksik veri olduğunda ne yapacağız 
from matplotlib.pyplot import axis
import numpy 
import pandas 



sozlukVerisi = {"Istanbul" : [30,29,numpy.nan] , "Ankara" : [20,numpy.nan,25] , "Izmir" : [40,39,38]}  # sözlük verimizi oluşturalım , df için 
# numpy.nan ile veri olmadığını belirttik 
havaDurumuDF = pandas.DataFrame(sozlukVerisi)
print(havaDurumuDF,"\n")

# ------------------------------
# nan verileri atalım 
print(havaDurumuDF.dropna(),"\n") # nan veriye sahip satırlar atılır. Sadece tüm verilerin olduğu setler gelecektir. Dikkat : illeri değil satırları atar. 
print(havaDurumuDF.dropna(axis=1),"\n") # axis=1 kolonlaRI seçer. Yani Nan olmayan verileri kolonlarda arar. Dikkat : satırları değil illeri atar.  

# ------------------------------
# yeni veri üzerinden birden fazla nan olma durumunu inceleyelim 
yeniSozluk =  {"Istanbul" : [30,29,numpy.nan] , "Ankara" : [20,numpy.nan,25] , "Izmir" : [40,39,38] , "Antalya" : [39,numpy.nan,numpy.nan]}
yeniDF = pandas.DataFrame(yeniSozluk)
print(yeniDF,"\n") 
# şimdi il verilerinde 2 tane nan varsa onları almayalım ama tek nan varsa alalım.
print(yeniDF.dropna(axis=1 , thresh=2) , "\n") # Burada thresh kaç tane nan'a kadar kabul edilebilir olduğunu verdi.

#--------------------------------
# Peki boş olan verileri doldurmak isteseydik 
print(yeniDF.fillna(31))




