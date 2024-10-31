sr_arifm = lambda massiv: sum(massiv)/len(massiv)

def peremnogalka(om):
    um = 1
    for i in om:
        um *= i
    return um

g = 9.81
poln_meh_en = lambda m,v,h: (m * v ** 2) / 2 + m*g*h

def koran(a = 0,b =1,n = 5):
    znach = []
    for i in range(a,b,((b-a)/n)):
        znach.append(i * abs(i))
    return znach

