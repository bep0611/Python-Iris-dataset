import pandas as pd

def ara(iris, turu):
    bulunanlar = iris[iris['iris'] == turu]
    
    if bulunanlar.empty:
        print(f"{turu} türü bulunamadı.")
    else:
        print(f"{turu} Türü Raporu:")
        print(bulunanlar)


def baris():
    deneme=True
    if deneme:
        iris = pd.read_excel("iris.xlsx")
        turu = input("çiçek türü gir: ")
        ara(iris, turu)

