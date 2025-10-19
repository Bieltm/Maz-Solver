laberint = [
    [1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 1, 0, 0, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 1, 0, 1, 2, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1]
]
moves = ["U", "D", "R", "L"] #UP DOWN RIGHT LEFT
cols = len(laberint)
rows = len(laberint[0])
col = 0, row = 0
        
def find_ceros():
    ceros = [0]*len(laberint[0])
    for i in range(0, len(laberint[0])):
        if (i == 0):
            ceros[j] = i
            j=j+1
    return ceros
