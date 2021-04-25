import os
import console_interact as CI

from regret_model import RegretModel

if __name__ == "__main__":
    os.system('cls')
    
    print('')

    choice = 1

    matrix, probs = CI.get_model(choice)

    if matrix is None or probs is None:
        exit()

    if sum(probs) > 1 or sum(probs) < 0:
        CI.print_list_probs(probs)
        print('Сумма вероятностей событий не равна 1')
        exit()

    model = RegretModel(matrix)
    model.print(payoff=True, regret=True)

    expect = model.PartialUncertainty(probs)
    CI.print_list_probs(probs)
    CI.print_list_strats(expect)

    wald = model.WaldsCriterion()
    CI.print_list_strats(wald)
    
    savage = model.SavagesCriterion()
    CI.print_list_strats(savage)

    coef = CI.safe_input_float('Критерий Гурвица на основе выигрыша\nКоэффициент ε = ')
    hurwicz_payoff = model.HurwiczsCriterionPayoff(coef)
    CI.print_list_strats(hurwicz_payoff)
    
    coef = CI.safe_input_float('Критерий Гурвица на основе риска\nКоэффициент λ = ')
    hurwicz_regret = model.HurwiczsCriterionRegret(coef)
    CI.print_list_strats(hurwicz_regret)
    
    print('\n')
