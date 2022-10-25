import numpy as NP 

benimDizim = NP.arange(0,15)
benimDizim[5] # indexler bildiğimiz liste mantığı 
benimDizim[2:7] # slicing , yine biliyoruz 

benimListem = [[10,20,30],[30,40,50],[40,50,60]]
print(benimListem)  # python'dan bildiğimiz iç içe liste görünümü 

benimMatrixListem = NP.array(benimListem)
print(benimMatrixListem) # matris gösterimi
 
# aynı indis kuralları geçerlidir. 
# bir ekstra : benimMatrixListem[1][2] = benimMatrixListem[1,2]  => ikisi de 50 verecektir 

print(benimMatrixListem[1:,1]) # 1. satırdan sonraki elemanların 1.elemanlarını al
# -> [40 50]

print(benimMatrixListem[2:,0]) # son satırdaki sadece 0.elemanı al
# -> [40]

# sağ taraftaki tek elemanı ifade etti , orayı da bütünü kapsayacak şekilde değiştirebiliriz 

print(benimMatrixListem[1:,0:]) # sağ tarafta da slicing yapabiliriz. ( 0 dan sonrasını al dedik)
# -> [ [30 40 50]
#      [40 50 60] ]
