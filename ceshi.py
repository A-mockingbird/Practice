p=[1,2]
n=3
def miHomeGiftBag(p,n):
    for x in p:
        if p == n:
            return 1
    if len(p) == 1:
        print(p)
        return 0
    for i in range(len(p)):
        if p[i] == n:
            return 1
        else:
            if i == 0:
                continue
            else:
                q = p[i:]
                q[0] = p[i] + p[0]
                miHomeGiftBag(p, n)
print(1)
miHomeGiftBag(p, n)

print(2)