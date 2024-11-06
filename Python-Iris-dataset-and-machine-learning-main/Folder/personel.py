class Personel:
    def __init__(self, ad, soyad, pozisyon):
        self.ad = ad
        self.soyad = soyad
        self.pozisyon = pozisyon

    def kimlik(self):
        return f"Ad: {self.ad}, Soyad: {self.soyad}, Pozisyon: {self.pozisyon}"

class Araştırmacı(Personel):
    def __init__(self, ad, soyad):
        super().__init__(ad, soyad, "Araştırmacı")

class Sekreter(Personel):
    def __init__(self, ad, soyad):
        super().__init__(ad, soyad, "Sekreter")

class SistemYoneticisi(Personel):
    def __init__(self, ad, soyad):
        super().__init__(ad, soyad, "Sistem Yöneticisi")

def merhaba():
    arastirmaci = Araştırmacı("Doruk", "Dölek")
    sekreter = Sekreter("Barış", "Paçcı")
    sistem_yoneticisi = SistemYoneticisi("Bahadır", "Acuner")

    print(arastirmaci.kimlik())
    print(sekreter.kimlik())
    print(sistem_yoneticisi.kimlik())

