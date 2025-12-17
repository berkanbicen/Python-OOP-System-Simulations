class BakiyeYetersizHatasi(Exception):
    def __init__(self, bakiye, cekilmek_istenen):
        self.bakiye = bakiye
        self.cekilmek_istenen = cekilmek_istenen
        # Hatayi alan kisiye detayli bir mesaj hazirliyoruz
        self.mesaj = f"HATA: Hesabinizda {bakiye} TL var ama {cekilmek_istenen} TL cekmeye calistiniz!"
        # Babanin (Exception) kurucusunu cagirip mesaji iletiyoruz
        super().__init__(self.mesaj)

class BankaHesabi:
    def __init__(self, sahip, bakiye):
        self.sahip = sahip
        self.bakiye = bakiye

    def para_cek(self, miktar):
        if miktar > self.bakiye:
            # Burasi onemli: Artik siradan bir hata degil, KENDI hatamizi firlatiyoruz
            raise BakiyeYetersizHatasi(self.bakiye, miktar)
        
        self.bakiye -= miktar
        print(f"✅ {miktar} TL cekildi. Kalan: {self.bakiye} TL")

# --- TEST ---
try:
    hesap = BankaHesabi("Berkan", 1000)
    
    # 1. Basarili islem
    hesap.para_cek(200) 
    
    # 2. Hatali islem (Bakiye yetmeyecek)
    print("--- 1500 TL cekmeye calisiliyor... ---")
    hesap.para_cek(1500)

# Burada artik spesifik olarak KENDI hatamizi yakaliyoruz
except BakiyeYetersizHatasi as hata:
    print(f"🛑 OZEL HATA YAKALANDI: {hata}")
    # Istersek hatanin icindeki detaylara da ulasabiliriz
    print(f"Eksik Tutar: {hata.cekilmek_istenen - hata.bakiye} TL")

except Exception as e:
    print(f"Beklenmedik baska bir hata oldu: {e}")