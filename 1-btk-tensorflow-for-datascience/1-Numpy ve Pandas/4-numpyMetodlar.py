
import numpy 

# range ile liste oluşturabiliriz 
print(list(range(0,10)))

liste1 = numpy.arange(0,10) # 0 dan 9 a liste oluşturur
print(liste1)

liste2 = numpy.zeros(5)     # listeyi 0 ile doldurur. ((2,2)) şeklinde kullanım ile matris yapabiliriz.#tupple kullanımı 
print(liste2)

# linspace çok kullanılır.
liste3 = numpy.linspace(0,20,22) # kaçtan başlar , kaça kadar , kaç tane veri olacak
print(liste3)