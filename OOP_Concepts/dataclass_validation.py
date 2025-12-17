from dataclasses import dataclass

@dataclass
class SinavKagidi:
    ogrenci_adi: str
    ders: str
    puan: int

    def __post_init__(self):
        # Validation (Dogrulama) İslemleri buraya yazilir
        if self.puan < 0 or self.puan > 100:
            raise ValueError(f"Hatali Puan: {self.puan}. Puan 0-100 arasinda olmalidir!")
        
        # Ekstra islem de yapabiliriz (Mesela ismi buyuk harfe cevirelim)
        self.ogrenci_adi = self.ogrenci_adi.upper()
        
        print(f"✅ {self.ogrenci_adi} icin not girisi basarili: {self.puan}")

try:
    kagit1 = SinavKagidi("ahmet", "Matematik", 85) # Ismi buyutecek
    kagit2 = SinavKagidi("mehmet", "Fizik", -10)   # Hata vermeli!

except ValueError as hata:
    print(f"🛑 HATA YAKALANDI: {hata}")