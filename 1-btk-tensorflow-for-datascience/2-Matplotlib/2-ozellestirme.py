
import numpy 
import matplotlib.pyplot as pyp 
import matplotlib.figure as fg

numpyDizisi1 = numpy.linspace(0,10,20) # 0 ile 10 arasındaki sayılardan 20 eşit aralıklı dizi
numpyDizisi2 = numpyDizisi1 ** 3 

pyp.plot(numpyDizisi1 , numpyDizisi2 , "g--")   # kesikli çizgiler ile gösterim
# pyp.plot(numpyDizisi1 , numpyDizisi2 , "g*-") # yıldız şeklinde gösterim 
#pyp.show() 
# ------------------------------------------------------------------------

# Birden çok grafik yapmak 
# ( Kaç sıra olacak , Kaç kolon olacak , kaçıncı grafik )
pyp.subplot(1,2,1) # 1 sıra 2 kolon(grafik) , şu an 1.yi çiziyorum
pyp.plot(numpyDizisi1 , numpyDizisi2 , "r*-")
pyp.subplot(1,2,2) # 1 sıra 2 kolon(grafik) , şu an 2.yi çiziyorum
pyp.plot(numpyDizisi2 , numpyDizisi1 , "g--")
#pyp.show()
# ------------------------------------------------------------------------- 
