class EkranKarti:
    def __init__(self, model):
        self.model = model

    def goruntu_ver(self):
        return f"[{self.model}] Ekrana goruntu veriliyor... 4K Cozunurluk!"

class Islemci:
    def __init__(self, model, cekirdek):
        self.model = model
        self.cekirdek = cekirdek

    def islem_yap(self):
        return f"[{self.model}] {self.cekirdek} cekirdek ile hesaplama yapiliyor..."
    
class Bilgisayar:
    def __init__(self):
        self.ekran_karti = EkranKarti("NVIDIA RTX 4090")
        self.islemci = Islemci("Intel i9", 16)

    def ac(self):
        print("--- Bilgisayar Aciliyor ---")
        print(self.islemci.islem_yap())
        print(self.ekran_karti.goruntu_ver())
        print("--- Sistem Hazir ---")

if __name__ == "__main__":
    benim_pc = Bilgisayar()
    benim_pc.ac()