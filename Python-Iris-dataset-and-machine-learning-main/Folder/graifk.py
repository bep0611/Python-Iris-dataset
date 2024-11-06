import pandas as pd
import matplotlib.pyplot as plt
def deneme():
    iris_data = pd.read_excel('iris.xlsx')

    colors = {'Iris-setosa': 'purple', 'Iris-versicolor': 'black', 'Iris-virginica': 'green'}


    plt.figure(figsize=(10, 6))
    for iris_type, color in colors.items():
        plt.scatter(iris_data[iris_data['iris'] == iris_type]['sepal length'], 
                iris_data[iris_data['iris'] == iris_type]['sepal width'], 
                color=color, label=iris_type)
    plt.xlabel('Sepal Length')
    plt.ylabel('Sepal Width')
    plt.title('tablo')
    plt.legend()
    plt.grid(True)
    plt.show()
