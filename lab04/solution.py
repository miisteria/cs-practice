def winner(names, scores):
    max_score = max(scores)
    index = scores.index(max_score)
    return names[index]
