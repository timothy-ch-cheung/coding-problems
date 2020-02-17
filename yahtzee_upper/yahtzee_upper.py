def yahtzee_upper(dice_rolls):
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
