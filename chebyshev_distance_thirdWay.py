def chebyshev_distance(vec1, vec2):
    if len(vec1) != len(vec2):
        raise ValueError("Les vecteurs doivent avoir la même longueur")
    
    return max(abs(v1 - v2) for v1, v2 in zip(vec1, vec2))