def yahtzee_upper(dice_rolls):
    score_dict = {}
    for roll in dice_rolls:
        if roll in score_dict:
            score_dict[roll] = score_dict[roll] + roll
        else:
            score_dict[roll] = roll
    return max(score_dict.values())


def yahtzee_upper_nlogn(dice_rolls):
    dice_rolls = sorted(dice_rolls)
    previous = None
    running_total = 0
    scores = []
    for roll in dice_rolls:
        if previous is None:
            running_total += roll
        elif roll == previous:
            running_total += roll
        else:
            scores.append(running_total)
            running_total = roll
        previous = roll
    scores.append(running_total)
    return max(scores)
