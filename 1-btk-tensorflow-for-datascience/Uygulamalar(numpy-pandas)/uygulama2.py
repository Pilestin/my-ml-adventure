import pandas as pd 

data = pd.read_csv("dataset/nba.csv")

# 1 - İlk 10 kaydı getiriniz 
result = data.head(10)

# 2 - Toplam kaç kayıt vardır 
result = len(data.index)

# 3 - Tüm oyuncuların toplam maaş ortalaması ne kadar 
result = data["Salary"].mean()

# 4 - En yüksek maaş ne kadardır 
result = data["Salary"].max()

# 5 - En yüksek maaşı alan oyuncu kimdir 
result = data[data["Salary"] == data["Salary"].max()]

# 6 - Yaşı 20-25 arasında olan oyuncuların isim ve oynadıkları takımları azalan şekilde sıralı getiriniz.
result = data[(data["Age"] <= 25) & (data["Age"] >= 20)][["Name","Team","Age"]].sort_values("Age", ascending = False)

# 7 - "John Holland" isimli oyuncunun oynadığı takım hangisidir ?
result = data[data["Name"] == "John Holland"][["Team"]]

# 8- Takımlara göre oyuncuların ortalama maaş bilgisi nedir ?
result = data.groupby("Team")["Salary"].mean()
# 9 - Kaç farklı takım mevcut 
result = len(data.groupby("Team"))

# 10 - Her takımda kaç oyuncu oynamaktadır 
result = data["Team"].value_counts()

# 11 - İsmi içinde "and" geçen kayıtları bulunuz 
data.dropna(inplace = True)
    # kayıp veriler atılır 
def str_find(name):
    if "and" in name.lower():
        return True
    return False

result = data[data["Name"].apply(str_find)]

print(result)