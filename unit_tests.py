import unittest
from regret_model import RegretModel

from numpy import array_equal

class Test_GetRegretMatrix(unittest.TestCase):
    """ Тест: получения матрицы рисков """
    def test_1_GetRegretMatrix(self):
        matrix = [
            [5, 7, 10],
            [7, 8, 6],
            [9, 8, 4]
        ]

        true_regret_matrix = [
            [4, 1, 0],
            [2, 0, 4],
            [0, 0, 6]
        ]

        model = RegretModel(matrix)

        regret_matrix = model._get_regret_matrix()

        assert array_equal(true_regret_matrix, regret_matrix) == True

    def test_2_GetRegretMatrix(self):
        matrix = [
            [15, 25, 50],
            [60, 20, 35],
            [25, 30, 45],
            [75, 5, 40]
        ]

        true_regret_matrix = [
            [60, 5, 0],
            [15, 10, 15],
            [50, 0, 5],
            [0, 25, 10]
        ]

        model = RegretModel(matrix)

        regret_matrix = model._get_regret_matrix()

        assert array_equal(true_regret_matrix, regret_matrix) == True

    def test_3_GetRegretMatrix(self):
        matrix = [
            [8, 9, 10, 11],
            [11, 10, 7, 8],
            [13, 8, 14, 7]
        ]

        true_regret_matrix = [
            [5, 1, 4, 0],
            [2, 0, 7, 3],
            [0, 2, 0, 4]
        ]

        model = RegretModel(matrix)

        regret_matrix = model._get_regret_matrix()

        assert array_equal(true_regret_matrix, regret_matrix) == True


class Test_PartialUncertainty(unittest.TestCase):
    """ Тест: критерий на известных вероятностях """
    def test_1_PartialUncertainty(self):
        matrix = [
            [5, 7, 10],
            [7, 8, 6],
            [9, 8, 4]
        ]
        probs = [0.7, 0.2, 0.1]

        true_expect = [2]

        model = RegretModel(matrix)

        expect = model.PartialUncertainty(probs)

        assert array_equal(true_expect, expect) == True

    def test_2_PartialUncertainty(self):
        matrix = [
            [15, 25, 50],
            [60, 20, 35],
            [25, 30, 45],
            [75, 5, 40]
        ]
        probs = [0.3, 0.1, 0.6]

        true_expect = [3]

        model = RegretModel(matrix)

        expect = model.PartialUncertainty(probs)

        assert array_equal(true_expect, expect) == True

    def test_3_PartialUncertainty(self):
        matrix = [
            [8, 9, 10, 11],
            [11, 10, 7, 8],
            [13, 8, 14, 7]
        ]
        probs = [0.25, 0.25, 0.25, 0.25]

        true_expect = [2]

        model = RegretModel(matrix)

        expect = model.PartialUncertainty(probs)

        assert array_equal(true_expect, expect) == True

class Test_WaldsCriterion(unittest.TestCase):
    """ Тест: критерий вальда """
    def test_1_WaldsCriterion(self):
        matrix = [
            [5, 7, 10],
            [7, 8, 6],
            [9, 8, 4]
        ]
        true_wald = [1]

        model = RegretModel(matrix)
        wald = model.WaldsCriterion()
        assert array_equal(true_wald, wald) == True

    def test_2_WaldsCriterion(self):
        matrix = [
            [15, 25, 50],
            [60, 20, 35],
            [25, 30, 45],
            [75, 5, 40]
        ]

        true_wald = [2]

        model = RegretModel(matrix)

        wald = model.WaldsCriterion()

        assert array_equal(true_wald, wald) == True

    def test_3_WaldsCriterion(self):
        matrix = [
            [8, 9, 10, 11],
            [11, 10, 7, 8],
            [13, 8, 14, 7]
        ]
        true_wald = [0]

        model = RegretModel(matrix)

        wald = model.WaldsCriterion()

        assert array_equal(true_wald, wald) == True

class Test_SavagesCriterion(unittest.TestCase):
    """ Тест: критерий сэвиджа """
    def test_1_SavagesCriterion(self):
        matrix = [
            [5, 7, 10],
            [7, 8, 6],
            [9, 8, 4]
        ]
        true_savage = [0, 1]

        model = RegretModel(matrix)
        savage = model.SavagesCriterion()
        assert array_equal(true_savage, savage) == True

    def test_2_SavagesCriterion(self):
        matrix = [
            [15, 25, 50],
            [60, 20, 35],
            [25, 30, 45],
            [75, 5, 40]
        ]
        true_savage = [1]

        model = RegretModel(matrix)
        savage = model.SavagesCriterion()
        assert array_equal(true_savage, savage) == True

    def test_3_SavagesCriterion(self):
        matrix = [
            [8, 9, 10, 11],
            [11, 10, 7, 8],
            [13, 8, 14, 7]
        ]
        true_savage = [2]

        model = RegretModel(matrix)
        savage = model.SavagesCriterion()
        assert array_equal(true_savage, savage) == True

class Test_HurwiczsCriterionPayoff(unittest.TestCase):
    """ Тест: критерий гурвица (выигрыш) """
    def test_1_HurwiczsCriterionPayoff(self):
        matrix = [
            [5, 7, 10],
            [7, 8, 6],
            [9, 8, 4]
        ]
        coef = 0.5
        true_hurwiczs = [0]

        model = RegretModel(matrix)
        hurwiczs = model.HurwiczsCriterionPayoff(coef)
        assert array_equal(true_hurwiczs, hurwiczs) == True

    def test_2_HurwiczsCriterionPayoff(self):
        matrix = [
            [15, 25, 50],
            [60, 20, 35],
            [25, 30, 45],
            [75, 5, 40]
        ]
        coef = 0.6
        true_hurwiczs = [1]

        model = RegretModel(matrix)
        hurwiczs = model.HurwiczsCriterionPayoff(coef)
        assert array_equal(true_hurwiczs, hurwiczs) == True

    def test_3_HurwiczsCriterionPayoff(self):
        matrix = [
            [8, 9, 10, 11],
            [11, 10, 7, 8],
            [13, 8, 14, 7]
        ]
        coef = 0.5
        true_hurwiczs = [2]

        model = RegretModel(matrix)
        hurwiczs = model.HurwiczsCriterionPayoff(coef)
        assert array_equal(true_hurwiczs, hurwiczs) == True

class Test_HurwiczsCriterionRegret(unittest.TestCase):
    """ Тест: критерий гурвица (риск) """
    def test_1_HurwiczsCriterionRegret(self):
        matrix = [
            [5, 7, 10],
            [7, 8, 6],
            [9, 8, 4]
        ]
        coef = 0.5
        true_hurwiczs = [0, 1]

        model = RegretModel(matrix)
        hurwiczs = model.HurwiczsCriterionRegret(coef)
        assert array_equal(true_hurwiczs, hurwiczs) == True

    def test_2_HurwiczsCriterionRegret(self):
        matrix = [
            [15, 25, 50],
            [60, 20, 35],
            [25, 30, 45],
            [75, 5, 40]
        ]
        coef = 0.6
        true_hurwiczs = [1]

        model = RegretModel(matrix)
        hurwiczs = model.HurwiczsCriterionRegret(coef)
        assert array_equal(true_hurwiczs, hurwiczs) == True

    def test_3_HurwiczsCriterionRegret(self):
        matrix = [
            [8, 9, 10, 11],
            [11, 10, 7, 8],
            [13, 8, 14, 7]
        ]
        coef = 0.5
        true_hurwiczs = [2]

        model = RegretModel(matrix)
        hurwiczs = model.HurwiczsCriterionRegret(coef)
        assert array_equal(true_hurwiczs, hurwiczs) == True


if __name__ == "__main__":
    unittest.main()