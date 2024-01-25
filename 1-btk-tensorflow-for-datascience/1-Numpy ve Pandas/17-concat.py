# concatenation
# tablo birleştirme

import pandas 
import numpy 

# 3 ayrı tablo oluşturalım ve bunları birleştirmeyi deneyelim

sozluk1 = {"Isım" : ["Ahmet","Mehmet","Zeynep","Yasin"] ,
           "Spor" : ["Koşu" ,"Yüzme","Koşu","Basketbol"],
           "Kalori" : [100,200,300,400] 
}   # 1.tablo için sozlük 

sozluk2 = {"Isım" : ["Osman","Levent","Atlas","Metehan"] ,
           "Spor" : ["Koşu" ,"Yüzme","Koşu","Basketbol"],
           "Kalori" : [200,100,50,300] 
}   # 2.tablo için sozlük 

sozluk3 = {"Isım" : ["Ayşe","Mahmut","Duygu","Nur"] ,
           "Spor" : ["Koşu" ,"Yüzme","Badminton","Tenis"],
           "Kalori" : [100,200,300,400] 
}   # 3.tablo için sozlük 

df1 = pandas.DataFrame(sozluk1)
df2 = pandas.DataFrame(sozluk2)
df3 = pandas.DataFrame(sozluk3)

print(df1,"\n" , df2 , "\n" , df3 , "\n")
print("---------------------------------")

dfBirlesik = pandas.concat([df1 , df2 , df3])
print(dfBirlesik)
