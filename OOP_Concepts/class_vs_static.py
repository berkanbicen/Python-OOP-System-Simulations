class Ogrenci:
    def __init__(self, ad, not_degeri):
        self.ad = ad
        self.not_degeri = not_degeri
    
    def bilgi_ver(self):
        # Bu standart bir Instance Method'dur (self kullanir)
        return f"Ogrenci: {self.ad} - Not: {self.not_degeri}"

    # --- 1. CLASS METHOD (Alternatif Kurucu / Factory) ---
    # Gelen veri: "Mehmet-90" seklinde string ise bunu ayiklayip nesne ureten metot
    @classmethod
    def metinden_olustur(cls, metin_verisi):
        isim, puan = metin_verisi.split("-") # Tireden parcala -> ["Mehmet", "90"]
        return cls(isim, int(puan)) # cls(...) diyerek aslinda Ogrenci(...) cagirmis oluyoruz

    # --- 2. STATIC METHOD (Yardimci Fonksiyon) ---
    # Sinifla veya nesneyle dogrudan isi yok, sadece yardimci bir hesap yapiyor
    @staticmethod
    def harf_notu_hesapla(puan):
        if puan >= 90: return "AA"
        elif puan >= 50: return "CC"
        else: return "FF"

# --- TEST ---

# 1. Normal Kullanim (__init__)
o1 = Ogrenci("Ali", 60)
print("Normal:", o1.bilgi_ver())

# 2. Class Method Kullanimi (Factory Pattern)
# Elimizde bozuk bir veri var ama metinden_olustur sayesinde kolayca nesne yapiyoruz
o2 = Ogrenci.metinden_olustur("Ayse-95") 
print("Factory:", o2.bilgi_ver())

# 3. Static Method Kullanimi
# Nesne olusturmadan direkt sinif uzerinden cagirabiliriz
harf = Ogrenci.harf_notu_hesapla(45)
print(f"45 puanin harf karsiligi: {harf}")