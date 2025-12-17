# --- ANA SINIF (BABA / PARENT) ---
class Gitar:
    def __init__(self, marka, tel_sayisi):
        self.marka = marka
        self.tel_sayisi = tel_sayisi

    def ses_cikar(self):
        return "Tingir mingir... (Akustik ses)"

    def bilgi_ver(self):
        return f"Bu bir {self.marka} ve {self.tel_sayisi} teli var."

# --- MİRAS ALAN SINIF (COCUK / CHILD) ---
class ElektroGitar(Gitar):
    def ses_cikar(self):
        return "CAART! (Distortion sesi)"
    def amfiye_bagla(self):
        return "Amfiye baglandi, rock yapmaya hazir!"
    
klasik = Gitar("Yamaha", 6)
print("Klasik Gitar: " + klasik.ses_cikar())

ibanez = ElektroGitar("Ibanez", 7)
print("Senin Gitar: " + ibanez.ses_cikar())

print(ibanez.bilgi_ver())
print(ibanez.amfiye_bagla())