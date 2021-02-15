from random import randint

class Matrix:
    def __init__(self, matr):
        self.matr = matr

    def __str__(self):                #почему тут через return не получается вывести все элементы?
        for i in self.matr:
            print(*i)

    def __add__(self, other):
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]              # а тут в пустой список не знаю как добавить,
                                                                # пришлость вписать нули(
        for i in range(len(self.matr)):               #ну тут вроде понятно как складывать поэлементно
            for j in range(len(self.matr)):
                matrix[i][j] = self.matr[i][j] + other[i][j]
        return matrix


     #чтоб долго не думать над матрицами сделал через рандом, да и для лишней практики лишним не будет
a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(3):
    for j in range(3):
        a[i][j] = randint(0, 10)
matrix_1 = Matrix(a)
print("первая матрица")
matrix_1.__str__()

b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(3):
    for j in range(3):
        b[i][j] = randint(0, 10)
matrix_2 = Matrix(b)
print("вторая матрица")
matrix_2.__str__()
      #а вот тут в голову ничего не пришло кроме как создать еще один объект для вывода новой матрицы
mat = matrix_1.__add__(b)
m = Matrix(mat)
print("сумма матриц")
m.__str__()
