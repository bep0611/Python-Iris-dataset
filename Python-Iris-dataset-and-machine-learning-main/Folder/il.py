import pandas as pd


def il(bolge, *a):
    bulunanlar = bolge[bolge['İl'].isin(a) | bolge['İlçe'].isin(a)]
    
    if bulunanlar.empty:
        print("Girilen il/ilçeler veri setinde bulunamadı.")
    else:
        print("Aranan İl/İlçe Raporu:")
        print(bulunanlar)

def doruk():
        bolge = pd.read_excel("bölgeler.xlsx")
        ilce = input("Lütfen aranacak il/ilçe(ler)i virgülle ayırarak girin: ").split(",")
        il(bolge, *ilce)


