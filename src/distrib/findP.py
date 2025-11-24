def findInferredP(probs):
    known = [p for p in probs if p is not None]
    inferred = 1 - sum(known)
    return inferred
