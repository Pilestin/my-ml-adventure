import numpy 

benimListem = numpy.random.randint(1,100,20) # 1 ile 100 arasından 20 tane rastgele sayı verdi
print(benimListem)

truefalseDizim = benimListem > 25
print(truefalseDizim)    # true false listesi şeklinde döndürür 


print(benimListem[truefalseDizim])   # bu şekilde sadece 25 den büyük olanları aldım
print("---------kök alma--------------")
# ---------------------------------- 

print(numpy.sqrt(benimListem))  # kök alır
print("----------4 işlem-----------")
print(benimListem + benimListem) # 4 işlem yapılabilir
