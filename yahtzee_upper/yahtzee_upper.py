from functools import  reduce

def yahtzee_upper(dice_rolls):
    sorted(dice_rolls)
    scores = [get_score(dice_rolls, x) for x in dice_rolls]
    return max(scores)

def get_score(dice_rolls, choice):
    filter_rolls = filter(lambda x: (x == choice), dice_rolls)
    return sum(filter_rolls)