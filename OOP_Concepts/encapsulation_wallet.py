class Cuzdan:
    def __init__(self, sahip, para_miktari):
        self.sahip = sahip
        self.__para = para_miktari

    def parayi_goster(self):
        return f"{self.sahip}'in hesabinda {self.__para} TL var."
    
    def parayi_yukle(self, miktar):
        if miktar > 0:
            self.__para += miktar
            print(f"{miktar} TL yuklendi.")
        else: 
            print("Hata: Eksi bakiye yukleyemezsin!")

benim_cuzdan = Cuzdan("Berkan", 100) 
print(benim_cuzdan.parayi_goster())

benim_cuzdan.parayi_yukle(50)
print(benim_cuzdan.parayi_goster())

benim_cuzdan.parayi_yukle(-5)


