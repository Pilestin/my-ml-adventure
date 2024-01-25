# Figure 

import numpy 
import matplotlib.pyplot as pyp 

numpyDizisi1 = numpy.linspace(0,10,20) # 0 ile 10 arasındaki sayılardan 20 eşit aralıklı dizi
numpyDizisi2 = numpyDizisi1 ** 3 

# boş bir figure oluşturalım ve yukarıdaki 2 diziyi eksenler şeklinde ayarlayalım 
figure1 = pyp.figure()  # boş bir figure oluşturuldu
eksen = figure1.add_axes([0.2,0.2,0.5,0.5]) # eksenler oluşturuldu. ( - , - , yükseklik , genişlik )
eksen.plot(numpyDizisi1, numpyDizisi2 ,"g")
eksen.set_xlabel("X ekseni")    # x ekseni 
eksen.set_ylabel("Y ekseni")    # y ekseni 
eksen.set_title("Grafik falan") # grafik başlığı 
pyp.show()                      # tabloyu göster 

# add_axes([sol taraftan uzaklık , aşağıdan uzaklık ])

# şimdi iç içe grafikleri görelim 
figure2 = pyp.figure()  # boş bir figure oluşturuldu 
eksen1 = figure2.add_axes([0.1,0.1,0.8,0.8]) # eksenler eklendi ( büyük grafik)
eksen2 = figure2.add_axes([0.23,0.6,0.2,0.2]) # eksenler eklendi ( içteki küçük grafik) 
    # eksen 1 için 
eksen1.plot(numpyDizisi1 , numpyDizisi2,"g") 
eksen1.set_xlabel("X ekseni")
eksen1.set_ylabel("Y ekseni")
eksen1.set_title("Ana Grafik Başlık")
    # eksen 2 için ( içteki grafik)
eksen2.plot(numpyDizisi2 , numpyDizisi1 , "y")
eksen2.set_xlabel("x")
eksen2.set_ylabel("y")
eksen2.set_title("Küçük grafik")
pyp.show()
