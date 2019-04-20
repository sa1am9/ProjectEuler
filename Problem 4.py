def search():
    max = 0
    for i in range(900,1000): #just i know that this numbers more than 900
        for j in range(900,1000): # of course i can start from 1
            if str(i*j)==str(i*j)[::-1] and i*j>max:
                max = i*j
    return max
print(search())
