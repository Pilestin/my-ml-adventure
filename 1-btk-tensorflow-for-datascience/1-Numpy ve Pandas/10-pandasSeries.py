import pandas 
import numpy 

yarisma1 = pandas.Series( [10 , 4 , 6] , ["Yasin" , "Yamur" , "Alihan"] )
yarisma2 = pandas.Series( [8 , 7 , 5]  , ["Yasin" , "Yamur" , "Alihan"] )

# sözlük tipinde olduğu gibi verileri görebiliriz. 
print(yarisma1["Yasin"])
print("--------------")
# serileri toplayabiliriz 
sonuc = yarisma1 + yarisma2 
print(sonuc)
print("--------------")
# peki listelerde farklı bir eleman olsaydı ya da teni bir eleman ekleseydik : 
farkliSeri1 = pandas.Series([1 , 27 , 65 , 5] , ["a","b","c","d"])
farkliSeri2 = pandas.Series([12 , 7 , 8 , 10] , ["a","c","f","g"])
print(farkliSeri1 + farkliSeri2) # kesişme varsa toplar , yoksa NaN yazar
