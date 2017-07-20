import LCRandom as LC
import LRRandom as LR
import random
import math
import time

lc_rand = LC.LCR()
lr_rand = LR.LRR()

def run_test(test_size = 1000000):

    start_lc = time.time()
    for i in range(test_size):
        lc_rand.rand()
    stop_lc = time.time()

    start_lr = time.time()
    for i in range(test_size):
        lr_rand.rand()
    stop_lr = time.time()

    start_py = time.time()
    for i in range(test_size):
        random.random()
    stop_py = time.time()

    print("Temps nécessaire pour effectuer la génération de "+str(test_size)+" de nombres aléatoires")
    print("La génération a pris "+str(stop_lc - start_lc)+" pour la congruence linéaire")
    print("La génération a pris "+str(stop_lr - start_lr)+" pour la récursivité linéaire")
    print("La génération a pris "+str(stop_py - start_py)+" pour l'implémentation native")

def parameters_change1():
    global lc_rand
    global lr_rand
    lc_rand = LC.LCR(m=9191, a=1716)

def parameters_change2():
    global lc_rand
    global lr_rand
    lc_rand = LC.LCR(m=65521, a=17364)

def parameters_change3():
    global lc_rand
    global lr_rand
    lc_rand = LC.LCR(m=29223, a=131071)
