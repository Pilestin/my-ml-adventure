# multi index

import numpy 
import pandas 

ilkIndeksler = ["Simpson","Simpson","Simpson","South Park","South Park","South Park"]
icIndeksler = ["Homer","Bart","Marge","Cartman","Kenny","Kyle"]

birlesmisIndeks = list(zip(ilkIndeksler , icIndeksler))
print(birlesmisIndeks)      # tuple gibi
print("------------------------------------")
birlesmisIndeks = pandas.MultiIndex.from_tuples(birlesmisIndeks)
print(birlesmisIndeks)      # özel tipe çevrildi
print("------------------------------------") 

cizgiFilmListem = [ [40,"A"],[10,"B"],[30,"C"],[9,"D"],[10,"E"],[11,"F"] ]
numpyDizim = numpy.array(cizgiFilmListem)           # data = numpy.random.randn(4,3) demek gibi
dfTablom   = pandas.DataFrame(numpyDizim , index=birlesmisIndeks ,columns=["Yaş","Meslek"])  # df   = pandas.DataFrame(data , index=["Yasin" , ...] , columns=["yaş", ....] ) gibi 
print(dfTablom)
print("------------------------------------")

# tablodan veri alma ( y ekseni )
print(dfTablom.loc["Simpson"].loc["Homer"]) # liste içindeki liste gibi 
print("------------------------------------")

# multi indeks kısmına etiket ekleme : 
dfTablom.index.names = ["Soyisim","İsim"]
print(dfTablom)
