# Kütüphaneleri import etmemiz gerekli.
# Detaylar için dökümantasyondan bakabilirsin 

import numpy    # as np diye kısaltabilirdik
import matplotlib.pyplot as matplot         # kısaca matplot dedik , veri görselleştirme için kullanılır.

maasListesi = numpy.random.normal(4000,500,1000)  # 4000 civarında 500 standart sapmalı 1000 tane veri oluştur 

# random rastgele sayı üretecek ama bildiğimiz random değil , kendine özgü 
# normal dağılım kullanıldı.(detaylar için bkz. istatistik)

ortalamaMaas = numpy.mean(maasListesi)  # ortalama alır ( rastgele üretilen listenin )

# verileri görselleştirelim 
matplot.hist(maasListesi,50) # histogram grafiği , 50 tane histogram
matplot.show()
