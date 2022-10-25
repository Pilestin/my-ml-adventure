# Subplots()
# iç içe oluşturduğumuz figure işlemini şimdi metod ile yapabiliriz. 
# Dikkat : subplots tupple döndürür. 
# boş bir figure + eksen çıkarır. Tupple döndürür  
import numpy 
import matplotlib.pyplot as pyp 

nDizisi1 = numpy.linspace(0,10,20)
nDizisi2 = nDizisi1 ** 2

(figure1 , eksenler ) = pyp.subplots(nrows=1,ncols=2) # kaç satır ve kaç kolon olacağı  
# fakat bu halde hata verir. Çünkü eksenim tek değil. Eksenim artık bir dizi
# AttributeError: 'numpy.ndarray' object has no attribute 'plot'

# döngü içinde bunu çözebiliriz 
for eksen in eksenler:
    eksen.plot(nDizisi1 , nDizisi2 , "g")
    eksen.set_xlabel("x")
    eksen.set_ylabel("y")

pyp.tight_layout() # aradaki mesafeyi düzeltir. Güzel görünmesi için 
pyp.show()
