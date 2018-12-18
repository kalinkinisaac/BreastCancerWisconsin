import numpy as np


# from database import db

# Функция активации -- сигмоида (самая популярная)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# Производная сигмоиды, понадобиться для высчитываения ошибки
def dsigmoid(x):
    return x * (1 - x)


np.random.seed(1337)  # Делаем рандом менее рандомным :(


class SelectionTree(object):
    def __init__(self):
        self._weight_matrix_1 = None
        self._weight_matrix_2 = None
        self._weight_matrix_3 = None
        self._weight_matrix_init()

    def _weight_matrix_init(self):
        self._weight_matrix_1 = np.random.random((9, 5)) - 1
        self._weight_matrix_2 = np.random.random((5, 3)) - 1
        self._weight_matrix_3 = np.random.random((3, 1)) - 1

    def test(self, data):
        # TODO: переделать проверку
        data = np.matrix(data)
        return [self._calculate(d) for d in data]

    def _calculate(self, data):
        return sigmoid(sigmoid(data.dot(self._weight_matrix_1)).dot(self._weight_matrix_2).dot(self._weight_matrix_3))

    def _dostep(self, input_train, output_train):
        Z_12 = np.dot(input_train, self._weight_matrix_1)
        A_2 = sigmoid(Z_12)

        Z_23 = np.dot(A_2, self._weight_matrix_2)
        A_3 = sigmoid(Z_23)

        Z_34 = np.dot(A_3, self._weight_matrix_3)
        A_4 = sigmoid(Z_34)

        Err_4 = output_train - A_4
        D_43 = Err_4 * dsigmoid(A_4)

        Err_3 = np.dot(D_43, self._weight_matrix_3.T)
        D_32 = Err_3 * dsigmoid(A_3)

        Err_2 = np.dot(D_32, self._weight_matrix_2.T)
        D_21 = Err_2 * dsigmoid(A_2)

        self._weight_matrix_1 += np.dot(input_train.T, D_21)
        self._weight_matrix_2 += np.dot(A_2.T, D_32)
        self._weight_matrix_3 += np.dot(A_3.T, D_43)

    def train(self, training_data):
        for (input_train, output_train) in training_data:
            self._dostep(input_train, output_train)


BRW = SelectionTree()

training_data = ([1, 2, 3, 4, 5, 6, 7, 8, 9], [1])
BRW.train(training_data=training_data)
