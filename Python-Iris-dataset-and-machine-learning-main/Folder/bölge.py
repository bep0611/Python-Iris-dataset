import pandas as pd

def bolge():
    arastirma_bolgesi_veri = pd.read_excel("bölgeler.xlsx")
    print("Araştırma Bölgesi Veri Kümesi Raporu:")
    print(arastirma_bolgesi_veri)
    return arastirma_bolgesi_veri


def deneme():
    iris_data = bolge()  
    
    for i in range(4):
        print(f"Satır {i + 1}: Yer Kodu: {iris_data.at[i, 'Yer Kodu']}, İlçe: {iris_data.at[i, 'İlçe']}, İl: {iris_data.at[i, 'İl']}, Bölge Adı: {iris_data.at[i, 'Bölge Adı']}")


