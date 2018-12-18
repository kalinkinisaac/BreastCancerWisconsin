import numpy as np
from .training_data import Tutorials


# Sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# Derivative of sigmoid function
def der_sigmoid(x):
    return x * (1 - x)


np.random.seed(1337)


class SelectionTree(object):
    def __init__(self, iterations=1000):
        self.iterations = iterations

        self._weight_matrix_1 = None
        self._weight_matrix_2 = None
        self._weight_matrix_3 = None

        self._weight_matrix_init()
        self._train()

    def _weight_matrix_init(self):
        self._weight_matrix_1 = np.random.random((9, 5)) - 1
        self._weight_matrix_2 = np.random.random((5, 3)) - 1
        self._weight_matrix_3 = np.random.random((3, 1)) - 1

    def test(self, data):
        data = np.array(data)
        Z_12 = np.dot(data, self._weight_matrix_1)
        A_2 = sigmoid(Z_12)

        Z_23 = np.dot(A_2, self._weight_matrix_2)
        A_3 = sigmoid(Z_23)

        Z_34 = np.dot(A_3, self._weight_matrix_3)
        return sigmoid(Z_34)

    def _step(self, input_train, output_train):
        Z_12 = np.dot(input_train, self._weight_matrix_1)
        A_2 = sigmoid(Z_12)

        Z_23 = np.dot(A_2, self._weight_matrix_2)
        A_3 = sigmoid(Z_23)

        Z_34 = np.dot(A_3, self._weight_matrix_3)
        A_4 = sigmoid(Z_34)

        Err_4 = output_train - A_4
        D_43 = Err_4 * der_sigmoid(A_4)

        Err_3 = np.dot(D_43, self._weight_matrix_3.T)
        D_32 = Err_3 * der_sigmoid(A_3)

        Err_2 = np.dot(D_32, self._weight_matrix_2.T)
        D_21 = Err_2 * der_sigmoid(A_2)

        self._weight_matrix_1 += np.dot(input_train.T, D_21)
        self._weight_matrix_2 += np.dot(A_2.T, D_32)
        self._weight_matrix_3 += np.dot(A_3.T, D_43)

    def _train(self):
        for j in range(self.iterations):
            try:
                data = Tutorials.get_samples()
            except ValueError:
                continue

            input_train = np.array(data[0])
            output_train = np.array([data[1]]).T

            self._step(input_train, output_train)

            # print(f'Training iteration {j} is completed')
