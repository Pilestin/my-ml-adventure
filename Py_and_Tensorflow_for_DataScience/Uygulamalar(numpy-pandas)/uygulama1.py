import numpy as np 
import pandas as pd 
import matplotlib as mtp 

# cleandataset kaggle platformundan indirildi. 
# Türkiye'de mesleklerin ne kadar maaş aldıkları vb. bilgiler içerir.
# kaynak kariyer.net 'den alınmıştır.

# 1- Dosyada hakkındaki bilgiler.
df = pd.read_csv("dataset/cleandataset.csv")
result = df.info()

# 2- ilk 5 kaydı gösterin
result = df.head()

# 3- ilk 10 kaydı gösterin
result = df.head(10)

# 4- Son 5 kaydı gösterin
result = df[-6:-1]
result = df.tail()

# 5- Son 10 kaydı gösterin
result = df.tail(10)

# 6- Sadece job_name kolonunu alın.
result = df['job_name']

# 7- Sadece job_name kolonunu içeren ilk 5 kaydı alın.
result = df['job_name'].head()

# 8- Sadece job_name ve mean_salary kolonunu içeren ilk 5 kaydı alın.
result = df[['job_name', 'mean_salary']].head()

# 9- Sadece job_name ve mean_salary kolonunu içeren son 7 kaydı alın.
result = df[['job_name', 'mean_salary']].tail(7)

# 10- Sadece job_name ve mean_salary kolonunu içeren ikinci 5 kaydı alın.
result = df[['job_name', 'mean_salary']][5:10]
result = df[5:10][['job_name', 'mean_salary']]

# 11- Sadece "job_name","min_salary","mean_salary","max_salary" kolonunu içeren ve min_salary 8000 
#     ve üstünde olan kayıtlardan ilk 50 tanesini alınız.
result3 = df[df["min_salary"] >= 8000][["job_name","min_salary","mean_salary","max_salary"]].head(50)

