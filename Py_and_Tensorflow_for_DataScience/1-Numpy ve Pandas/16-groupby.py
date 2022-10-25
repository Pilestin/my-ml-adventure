# groupby 

import numpy 
import pandas 
 
maasSozlugu =   {"Departman" : ["Yazılım","Yazılım","Pazarlama","Pazarlama","Hukuk","Hukuk"],
                 "Calisan Ismi" : ["Ahmet","Mehmet","Atil","Burak","Zeynep","Fatma"],
                 "Maas" : [100,150,200,300,400,500]
                }

maasDF = pandas.DataFrame(maasSozlugu) 
print("-----------maasDF--------------------")
print(maasDF,"\n")

grupObjesi = maasDF.groupby("Departman")
print("-----------grupObjesi--------------------")
print(grupObjesi , "\n")  # obje tipini verir ve ram'de yerini gösterir. 
print("-----------.count()--------------------")
print(grupObjesi.count(),"\n") # departmanların tekrar sayısı 
print("-----------.mean()--------------------")
print(grupObjesi.mean(),"\n")  # departmanların ortalaması. 
print("-----------.min()--------------------")
print(grupObjesi.min(),"\n")   # minimum veri 
print("-----------.max()--------------------")
print(grupObjesi.max(),"\n")   # maximum veri
 
