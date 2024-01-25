
import numpy 
import pandas 

data = numpy.random.randn(4,3) # 4 satır , 3 sütun matris
df = pandas.DataFrame(data , index=["Yasin" , "Ersin" , "Muhsin","Tahsin"] , columns=["yaş","maaş","çalışma saati"])

print(df)
print("------------------------------------")

# İndeks değiştirme 
df.reset_index(inplace=True)    # orjinal referansı değiştirmek için 
print(df)
print("------------------------------------")
# İndex ekleme 
# - önce bir liste oluşturalım 
# - sonra listeyi df objemize kolon olarak ekleyelim 
# - ardından bu kolonu index olarak ayarlayalım 

yeniIndexListem = ["Yas" , "Ers" , "Muh" , "Tah"]
df["yenikolon"] = yeniIndexListem
print(df)
print("------------------------------------")
df.set_index("yenikolon" , inplace=True) # artık yeni kolon tablomuzun index kısmı oldu. ( orjinal listemizi değiştirdik "inplace" )
print(df)