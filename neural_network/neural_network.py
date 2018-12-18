import numpy as np


# Функция активации -- сигмоида (самая популярная)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# Производная сигмоиды, понадобиться для высчитываения ошибки
def dsigmoid(x):
    return x * (1 - x)


np.random.seed(322 - 228)  # Делаем рандом менее рандомным :(


# (in_1) (in_2) (in_3)  -- Input    <--     A_1
#     (h_1)  (h_2)      -- Hidden   <--     A_2
#         (out)         -- Output   <--     A_3
#
# Если мы хотим приблизить функцию XOR(a, b), то
# a -- in_1     //      b -- in_2       //      in_3 -- отвечает за "свободную поправку"
# Weight_Matrix_1 -- матрица весов от Input --> Hidden [3x2] // Матрицу значений обозначим Z_12
# Weight_Matrix_2 -- матрица весов от Hidden --> Output [2x1] // Матрицу значений обозначим Z_23
#
# Error_3 -- насколько мы ошиблись в весах Hidden-->Output
# Error_2 -- насколько мы ошиблись в весах Input-->Hidden
# Для нахождения насколько именно надо изменить матрицу весов необходимо:
# перемножить ошибку на передаваемые значения (A_i) и умножить на производную в данной точке значений
# Производная показывает "куда" и "с какой скоростью" двигаться, а значения "насколько сильно"
#
# PS: ускорить обучение можно, если улучшить рассчет ошибок, например, через квадратичное отклонения

class XOR_NN(object):
    def __init__(self):
        self._weight_matrix_1 = None
        self._weight_matrix_2 = None
        self._weight_matrix_init()
        self.Output = None

    def _weight_matrix_init(self):
        self._weight_matrix_1 = np.random.random((3, 2)) - 1
        self._weight_matrix_2 = np.random.random((2, 1)) - 1

    def test(self, data):
        data = np.matrix(data)
        return [self._calculate(d) for d in data]

    def _calculate(self, data):
        return sigmoid(sigmoid(data.dot(self._weight_matrix_1)).dot(self._weight_matrix_2))

    def train(self, training_data, N=100000):
        Input_xor, Output_xor = training_data
        for i in range(N):
            Z_12 = np.dot(Input_xor, self._weight_matrix_1)
            A_2 = sigmoid(Z_12)

            Z_23 = np.dot(A_2, self._weight_matrix_2)
            A_3 = sigmoid(Z_23)

            error_3 = Output_xor - A_3

            D_32 = error_3 * dsigmoid(A_3)
            error_2 = np.dot(D_32, self._weight_matrix_2.T)

            D_21 = error_2 * dsigmoid(A_2)

            self._weight_matrix_2 += np.dot(A_2.T, D_32)
            self._weight_matrix_1 += np.dot(Input_xor.T, D_21)

            self.Output = A_3
        print(self.Output)


XOR = XOR_NN()

Input = np.array([[0, 0, 1],  # xor = 0
                  [0, 1, 1],  # xor = 1
                  [1, 0, 1],  # xor = 1
                  [1, 1, 1]])  # xor = 0
Output_xor = np.array([[0, 1, 1, 0]]).T  # Идеальные значения функции xor

XOR.train([Input, Output_xor], 100000)

print("\nВведите a и b, если хотите узнать XOR(a,b)\n")
a = float(input('a = '))
b = float(input('b = '))
print(XOR.test([a, b, 1]))
