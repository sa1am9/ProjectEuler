n = 2520
while True:
    ok = True
    for d in range(11,21):
        if n % d != 0:
            ok = False
            break
    if ok:
        break
    else:
        n += 20
print(n)