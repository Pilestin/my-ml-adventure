# merge - birleştirme 
# ortak olan bir kolona göre birleştirme yapacağız 

import pandas 
import numpy 

sozluk1 = { "Isım": ["Ahmet","Mehmet","Zeynep","Yasin"] ,
            "Spor": ["Koşu","Yüzme","Koşu","Basketbol"]
          }

sozluk2 = { "Isım": ["Ahmet","Mehmet","Zeynep","Yasin"] ,
            "Kalori": [100,200,300,400]
          }

df1 = pandas.DataFrame(sozluk1)
df2 = pandas.DataFrame(sozluk2)
print(df1 , "\n", df2 , "\n")


# şimdi bu iki tabloyu ortak olan Isım kolonuna göre birleştirelim : 
mergedDF = pandas.merge(df1 , df2 , on="Isım") # Isım üzerinden merge yap 
print(mergedDF)


