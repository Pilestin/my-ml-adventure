
import numpy 
import matplotlib.pyplot as pyp 

yasListesi = [10,20,30,30,30,40,50,60,70,75]
kiloListesi = [20,60,70,75,86,87,70,90,95,90]

# Genelde numpy listesi halinde tutmak daha iyidir.
numpyYasListesi  = numpy.array(yasListesi)
numpyKiloListesi = numpy.array(kiloListesi)

# BASİT GRAFİK OLUŞTURMA 
# .plot ile grafik oluşturacağız. ilk parametre x ekseni , ikinci parametre y ekseni için. Sondaki g ise çizgi rengini belirtir.
pyp.plot(numpyYasListesi ,numpyKiloListesi , "g")
pyp.xlabel("Yas")   # x ekseni etiketi
pyp.ylabel("Kilo")  # y ekseni etiketi
pyp.title("Kilonun yaşa göre değişimi grafiği")
pyp.show()          # ekranda sonuc grafiğini görmek için 



