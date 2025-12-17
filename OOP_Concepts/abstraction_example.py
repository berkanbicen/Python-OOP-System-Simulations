from abc import ABC, abstractmethod

# --- SOYUT SINIF (KURALLAR) ---
class MuzikAleti(ABC):
    
    @abstractmethod
    def ses_cikar(self):
        pass

# --- GERÇEK SINIFLAR ---

class Gitar(MuzikAleti):
    def ses_cikar(self):
        return "Tingir mingir..."

class Bateri(MuzikAleti):
    def ses_cikar(self):
        return "Güm Bedak!"

# --- KULLANIM KISMI ---

# 1. Gitar üretelim (Artık hata vermemeli)
gitarim = Gitar()
print("Gitar: " + gitarim.ses_cikar())

# 2. Bateri üretelim
baterim = Bateri()
print("Bateri: " + baterim.ses_cikar())

# 3. Soyut sınıfı test edelim (Burası HATA verecek, bu normal!)
print("\n--- Hata Testi Başliyor ---")
try:
    hayalet = MuzikAleti()
except Exception as e:
    print(f"BEKLENEN HATA YAKALANDI: {e}")
    print("Mesaj: Soyut siniftan nesne üretemezsin, sadece miras alabilirsin!")