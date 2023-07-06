from cashflower import variable

from tutorials.life_insurance.whole_life.input import main
from tutorials.life_insurance.whole_life.settings import settings

INTEREST_RATE = 0.005
DEATH_PROB = 0.003


@variable()
def survival_rate(t):
    if t == 0:
        return 1 - DEATH_PROB
    else:
        return survival_rate(t-1) * (1 - DEATH_PROB)


@variable()
def expected_benefit(t):
    sum_assured = main.get("sum_assured")
    if t == settings["T_MAX_CALCULATION"]:
        return survival_rate(t-1) * sum_assured
    return survival_rate(t-1) * DEATH_PROB * sum_assured


@variable()
def net_single_premium(t):
    if t == settings["T_MAX_CALCULATION"]:
        return expected_benefit(t)
    return expected_benefit(t) + net_single_premium(t+1) * 1/(1+INTEREST_RATE)
