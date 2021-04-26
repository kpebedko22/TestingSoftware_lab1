

class RegretModel:

    def __init__(self, payoff_matrix):
        """
        Инициализация матрицы выигрышей и матрицы рисков
        """

        # матрица выигрышей
        self.payoff_matrix = [[payoff_matrix[i][j] for j in range(len(payoff_matrix[0]))] for i in range(len(payoff_matrix))]

        # кол-во строк матрицы
        self.num_actions = len(self.payoff_matrix)

        # кол-во столбцов матрицы
        self.num_events = len(self.payoff_matrix[0])

        # матрица рисков
        self.regret_matrix = self._get_regret_matrix()

    def _get_regret_matrix(self):
        """
        Сформировать матрицу рисков на основе матрицы выигрышей
        1. для каждого столбца выбрать максимальное значение
        2. из найденного максимума вычесть элементы данного столбца
        """

        regret_matrix = [[0 for j in range(self.num_events)] for i in range(self.num_actions)]

        for i in range(self.num_events):
            max_el_col = max([self.payoff_matrix[j][i] for j in range(self.num_actions)])

            for j in range(self.num_actions):
                regret_matrix[j][i] = max_el_col - self.payoff_matrix[j][i]

        return regret_matrix

    def PartialUncertainty(self, probabilities):
        """
        Критерий, основанный на известных вероятностях условий
        """

        avgR = []

        for i in range(self.num_actions):
            s = 0
            for j in range(self.num_events):
                s += probabilities[j] * self.regret_matrix[i][j]
            avgR.append(s)

        minR = min(avgR)

        res = [i for i in range(self.num_actions) if avgR[i] == minR]

        return res

    def WaldsCriterion(self):
        """
        Критерий Вальда (максимин)
        1. выбирается минимум для каждой строки матрицы выигрышей
        2. выбирается максимум из п.1

        Args:
            none

        Return:
            res - список номеров действий (необходимо +1, т.к. нумерация с нуля)
        """

        minA = [min(self.payoff_matrix[i]) for i in range(self.num_actions)]
        maxminA = max(minA)
        res = [i for i in range(self.num_actions) if minA[i] == maxminA]

        return res

    def SavagesCriterion(self):
        """
        Критерий Сэвиджа
        1. выбирается максимум для каждой строки матрицы рисков
        2. выбирается минимум из п.1

        Args:
            none

        Return:
            res - список номеров действий (необходимо +1, т.к. нумерация с нуля)
        """

        maxR = [max(self.regret_matrix[i]) for i in range(self.num_actions)]
        minmaxR = min(maxR)
        res = [i for i in range(self.num_actions) if maxR[i] == minmaxR]
        
        return res

    def HurwiczsCriterionPayoff(self, coef):
        """
        Критерий Гурвица на основе выигрыша
        1. для каждой строки (матрицы выигрыша) выбирается минимум и максимум
        2. для каждой строки вычисляется формула
            min * coef + max * (1 - coef)
        3. выбирается максимальное из вычисленных значений

        Args:
            coef - коэффициент 0 <= coef <= 1
            если coef = 0, то получаем критерий Вальда
            если coef = 1, То получаем критерий "крайнего оптимизма"

        Return:
            res - список номеров действий (необходимо +1, т.к. нумерация с нуля)
        """
        minA = [min(self.payoff_matrix[i]) for i in range(self.num_actions)]
        maxA = [max(self.payoff_matrix[i]) for i in range(self.num_actions)]

        values = [minA[i] * coef + maxA[i] * (1 - coef) for i in range(self.num_actions)]

        max_value = max(values)

        res = [i for i in range(self.num_actions) if values[i] == max_value]

        return res

    def HurwiczsCriterionRegret(self, coef):
        """
        Критерий Гурвица на основе риска
        1. для каждой строки (матрицы риска) выбирается минимум и максимум
        2. для каждой строки вычисляется формула
            max * coef + min * (1 - coef)
        3. выбирается минимальное из вычисленных значений

        Args:
            coef - коэффициент 0 <= coef <= 1
            если coef = 0, то получаем критерий Сэвиджа
            если coef = 1, То получаем критерий "крайнего оптимизма"

        Return:
            res - список номеров действий (необходимо +1, т.к. нумерация с нуля)
        """

        minR = [min(self.regret_matrix[i]) for i in range(self.num_actions)]
        maxR = [max(self.regret_matrix[i]) for i in range(self.num_actions)]

        values = [maxR[i] * coef + minR[i] * (1 - coef) for i in range(self.num_actions)]

        min_value = min(values)

        res = [i for i in range(self.num_actions) if values[i] == min_value]

        return res




