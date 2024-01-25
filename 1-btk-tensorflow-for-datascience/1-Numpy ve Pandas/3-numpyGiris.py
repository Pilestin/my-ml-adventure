# Veri Biliminde kullanılan bir kütüphanedir. Lineer Cebir (matris) işlemleri için kullanılır.
# Bilmemiz , hakim olmamız gereken bir kütüphanedir. 
# Çok fazla özelliği vardır. 
# Detaylar için dökümantasyona bak 

import numpy 

# liste oluşturalım 

benimListem = [10,15,20]
print(type(benimListem))
print(numpy.array(benimListem))         # göründüğü gibi bastırır

matris = [[0,0,1],[0,1,0],[1,0,0]]
print(type(matris))
print(numpy.array(matris))              # matrisi bastırır.