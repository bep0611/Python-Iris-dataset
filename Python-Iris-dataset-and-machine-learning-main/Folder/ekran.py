import pandas as pd

def raporla_iris():
    iris_veri = pd.read_excel("iris.xlsx")
    
    print("İris Veri Kümesi Raporu:")
    print(iris_veri)
    
    return iris_veri  

def deneme():
    iris_data = raporla_iris()  
    
    for i in range(5):
        print(f"Satır {i + 1}: Sepal Length: {iris_data.at[i, 'sepal length']}, Sepal Width: {iris_data.at[i, 'sepal width']}, Petal Length: {iris_data.at[i, 'petal length']}, Petal Width: {iris_data.at[i, 'petal width']}, Iris: {iris_data.at[i, 'iris']}")


