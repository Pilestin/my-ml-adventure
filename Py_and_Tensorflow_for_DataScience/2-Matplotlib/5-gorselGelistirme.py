# Görsel Geliştirmeler 

import numpy 
import matplotlib.pyplot as pyp 
 

numpyDizisi1 = numpy.linspace(0,10,20)
numpyDizisi2 = numpyDizisi1 ** 3
yeniFigur = pyp.figure() 
    # içerisine figsize=(3,3) gibi figür boyutunu ayarlayabiliriz 
    # içerisine dpi ile çözünürlük ayarlayabiliriz.


yeniEksen = yeniFigur.add_axes([0.1,0.1,0.9,0.9])
    # grafiğe etiket atayalım
yeniEksen.plot(numpyDizisi1 , numpyDizisi1 ** 2 , label="numpyDizisi ** 2")  # label ile etikette ne yazacağını belirliyoruz 
yeniEksen.plot(numpyDizisi1 , numpyDizisi1 ** 3 , label="numpyDizisi ** 3")  # label ile etikette ne yazacağını belirliyoruz 
yeniEksen.legend()  # etiket atandı 
    # legend(loc=herhangibirsayı) ile grafik labelinin yerini farklı bölgelere atayabiliriz 
pyp.show()

# figürü kayıt edebilirim. 
yeniFigur.savefig("benimfigürüm.png",dpi=200)