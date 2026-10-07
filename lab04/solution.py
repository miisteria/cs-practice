def winner(names, scores):
    max_score = max(scores)
    index = scores.index(max_score)
    return names[index]
def average(scores):
    if len(scores) == 0:
        return 0.0
    return round(sum(scores) / len(scores), 2)