# pandas bir veri analizi kütüphanesidir
# pip install pandas ile indirmemiz gerekli.  
# import edilmesi gereklidir. 

from operator import index
import numpy 
import pandas 
#---------------------------------------------------------------------------------------
# İlk olarak SERİLER'i görelim.

# numpy dizilerine benzer 
# python'da bildiğimiz sözlük veri tipine de benzer 
# verilerle oynamaya yarar 

benimSozlugum = {"Yasin" : 21 , "Ali" : 13 , "Recep" : 60}
benimSerim    = pandas.Series(benimSozlugum) # pandas.core.series.Series tipinde 

print(f"benimSozlugum :\n{benimSozlugum}")
print(f"benimSerim :\n{benimSerim}" )
print("--------------")
#---------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------
# şimdi bu işi ayrı listelerden yapalım , bir bakıma kartezyenleme ya da eşleştirme gibi.
liste1 = [18,10,20]
liste2 = ["Can" , "Ayşe" , "Fatma"]

yasIsım = pandas.Series(liste1 , liste2) 
# şöyle de yapabilirdik : 
pandas.Series(data=liste1 , index= liste2 )

print(yasIsım)
print("--------------")
#---------------------------------------------------------------------------------------