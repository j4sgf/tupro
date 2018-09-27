import random
import math
x1 = random.randint(-10, 10)
x2 = random.randint(-10, 10)
n1, n2 = x1, x2
cs = float
bsf = float
sin = math.sin
cos = math.cos
exp = math.exp

initial_state = (x1-x2)
cs = initial_state
bsf = cs
batas = 1000
dingin = random.randint(1, 100)

print("Mencari nilai Minimum dari:")
print("f(x1, x2)=(-abs((sin(x1) * cos(x2) * exp(abs(1-(((x1**2+x2**2)**1/2)/3.14))))")
print("Dengan -10<=x1<=10 dan -10<=x2<=10")
print("Tekan enter untuk memulai")
input()
print("Curent State : ", cs)
while batas > 0:
    n1 = random.randint(-10, 10)
    n2 = random.randint(-10, 10)
    ns = (n1-n2)
    delta_state = ns-cs
    if delta_state < 0:
        x1 = n1
        x2 = n2
        if ns < bsf:

            bsf = ns
            cs = bsf
            a1 = n1
            a2 = n2

            print("Best so far : ", bsf)
            print("Curent State : ", cs)
            print("Dengan x1 : ", a1, "dan x2 : ", a2)
            print()

            j1 = a1
            j2 = a2

            batas = batas - dingin

    else:
        import math
        r = random.uniform(0, 10)
        if(r < math.exp(-delta_state/initial_state)):
            cs = ns
            a1 = n1
            a2 = n2
            ns = (n1-n2)
            print("Best so far : ", bsf)
            print("Curent State : ", cs)
            print("Dengan x1 : ", a1, "dan x2 : ", a2)
            print()

            batas = batas - dingin


print("-------------------------------")
print("Nilai minimum adalah : ", bsf)
print("Dengan x1 : ", j1, "dan x2 : ", j2)
input()
