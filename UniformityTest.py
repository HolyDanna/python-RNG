import LCRandom as LC
import LRRandom as LR
import random
import math

lc_rand = LC.LCR()
lr_rand = LR.LRR()

def run_test(test_size = 1000000, separation=0):
    value_lc = [[0 for i in range(100)] for j in range(100)]
    value_lr = [[0 for i in range(100)] for j in range(100)]
    value_py = [[0 for i in range(100)] for j in range(100)]

    for i in range(test_size):
        x_lc = lc_rand.randint(100)
        for j in range(separation):
            lc_rand.rand()
        y_lc = lc_rand.randint(100)
        value_lc[x_lc][y_lc] += 1
        x_lr = lr_rand.randint(100)
        for j in range(separation):
            lr_rand.rand()
        y_lr = lr_rand.randint(100)
        value_lr[x_lr][y_lr] += 1
        value_py[random.randint(0,99)][random.randint(0,99)] += 1

    deviation_lc = 0
    deviation_lr = 0
    deviation_py = 0

    for i in range(100):
        for j in range(100):
            deviation_lc += abs(test_size/10000 - value_lc[i][j])
            deviation_lr += abs(test_size/10000 - value_lr[i][j])
            deviation_py += abs(test_size/10000 - value_py[i][j])

    deviation_lc = deviation_lc / 10000
    deviation_lr = deviation_lr / 10000
    deviation_py = deviation_py / 10000

    print("Ditribution aléatoire dans un tableau de 100x100")
    print("Il y a en moyenne "+str(test_size/10000)+" éléments par case")
    print("L'écart moyen dans le cadre de la congruence linéaire est de "+str(deviation_lc))
    print("L'écart moyen dans le cadre de la récursivité linéaire est de "+str(deviation_lr))
    print("L'écart moyen dans le cadre de l'implémentation native' est de "+str(deviation_py))

def parameters_change1():
    global lc_rand
    global lr_rand
    lc_rand = LC.LCR(m=2**23-15, a=653276)
    lr_rand = LR.LRR(m=2**24-3, a1=4408741, a2=5637643)

def parameters_change2():
    global lc_rand
    global lr_rand
    lc_rand = LC.LCR(m=2**28-57, a=29908911)
    lr_rand = LR.LRR(m=2**27-39, a1=3162696, a2=88641177)

def parameters_change3():
    global lc_rand
    global lr_rand
    lc_rand = LC.LCR(m=2**30-35, a=771645345)
    lr_rand = LR.LRR(m=2**29-3, a1=520332806, a2=530877178)
