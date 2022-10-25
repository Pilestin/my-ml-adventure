
import numpy 
import pandas 

data = numpy.random.randn(4,3) # 4 satır , 3 sütun matris
df = pandas.DataFrame(data , index=["Yasin" , "Ersin" , "Muhsin","Tahsin"] , columns=["yaş","maaş","çalışma saati"])

# yeni kolon ekleme : 
df["emeklilik"] = df["yaş"] + df["yaş"] # emeklilik ekleyelim ve  yaş+yaş  olsun 
print(df)
#--------------------------------------

# kolon ve satır silme 
df.drop("Yasin") # yasin'i siler 
df.drop("yaş" , axis=1) # sütun için axis parametresi kullanılır , yazmassak hata alırız. Çünkü y ekseninde arar 

print("--------------------------------------------------")
# yapılan değişikliklerin orjinal tabloda geçerli olması için : 
df.drop("Yasin" , axis=0 , inplace=True) 
print(df) 

print("--------------------------------------------------")
# tek bilgiyi almak : 
print(df.loc["Muhsin"]["yaş"])