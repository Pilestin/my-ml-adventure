
import pandas 
import numpy 

sozluk1 = { "Isım": ["Atıl","Yasin","Mete","Hasan"],
            "Departman" : ["Yazılım","Satış","Pazarlama","Yazılım"],
            "Maas" : [200,300,400,500]
          }

maasDF = pandas.DataFrame(sozluk1) 
print(maasDF)
print("-----------------------------------------------")
print(maasDF["Departman"].unique()) # Tekil bir şekilde departmanlar 
print(maasDF["Departman"].value_counts()) # departmanlara göre kişi sayıları 
print("-----------------------------------------------")

def bruttenNete(maas):
    # bir maas hesaplaması yapsın
    return maas * 0.66

print(maasDF["Maas"].apply(bruttenNete)) # bir for döngüsüne sokmamıza gerek kalmadan bunu kendisi fonksiyona göndererek yapar 
print("-----------------------------------------------")

yeniBirVeri = { "Karakter Sınıfı":["South Park","South Park","Simpson","Simpson"],
                "Karakter Ismi" : ["Cartman","Kenny","Homer","Bart"],
                "Karakter Yas" : [9,10,50,20]  
              }

karakterDF = pandas.DataFrame(yeniBirVeri)
print(karakterDF)
print("----------------pivot table-------------------------------")
print(karakterDF.pivot_table(values="Karakter Yas" , index=["Karakter Sınıfı","Karakter Ismi"]))
# karakter sınıfı ve karakter ismini solda tutup yas sağda kalır. 






