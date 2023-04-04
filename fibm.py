def fibm(n):
    if n <= 1:
        return n
    else:
        return fibm(n-1) + fibm(n-2)
