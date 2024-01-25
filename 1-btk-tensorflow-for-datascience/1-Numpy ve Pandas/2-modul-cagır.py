# ---- MODÜL ---- 

from modulpaket import ornekFonksiyon

# modul çalıştırma 
# detaylar için modulpaket.py dosyasına bakınız 
ornekFonksiyon()

# ---- PAKET ----

from Paketim import anaPaketModul                   # Paket içerisinden dosya import ettik
from Paketim.AltPaket import altPaketModul          # Paket içerisindeki alt klasörden dosya import ettik.

# Paket içerisinden kullanım : ( dosya.fonksiyon)
anaPaketModul.anaFonksiyon()            
altPaketModul.altFonksiyon()