from dataclasses import dataclass
class EskiOgrenci:
    def __init__(self, ad, numara, ortalama):
        self.ad=ad
        self.numara=numara
        self.ortalama=ortalama

    def __str__(self):
        return f"EskiOgrenci(ad={self.ad}, numara={self.numara}, ortalama={self.ortalama} )"
    
@dataclass
class YeniOgrenci:
    ad: str
    numara: int
    ortalama: float

print ("--- ESKI YONTEM ---")
o1 = EskiOgrenci("Ali", 101, 75.5)
o2 = EskiOgrenci("Ali", 101, 75.5)
print(o1)
print(f"Esit mi? {o1 == o2}")

print("\n--- DATACLASS ---")
y1=YeniOgrenci("Ayse", 202, 90.0)
y2=YeniOgrenci("Ayse", 202, 90.0)
print(y1)
print(f"Esit mi? {y1==y2}")