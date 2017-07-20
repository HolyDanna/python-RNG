import LCRandom as LC
import LRRandom as LR
import random
import math

lc_rand = LC.LCR()
lr_rand = LR.LRR()

def run_test(test_size = 100000, radius=0.4):
    value_lc = 0
    value_lr = 0
    value_py = 0

    for i in range(test_size):
        if math.sqrt((lc_rand.rand()**2 + lc_rand.rand()**2)) <= radius:
            value_lc += 1
        if math.sqrt((lr_rand.rand()**2 + lr_rand.rand()**2)) <= radius:
            value_lr += 1
        if math.sqrt((random.random()**2 + random.random()**2)) <= radius:
            value_py += 1

    value_lc = value_lc/test_size
    value_lr = value_lr/test_size
    value_py = value_py/test_size
    area = math.pi*(radius**2)/4

    print("The area of the circle is : "+str(area))
    print("Percentage of elements in area for self implemented Linear Congruent RNG : "+str(value_lc))
    print("Percentage of elements in area for self implemented Linear Recursive RNG : "+str(value_lr))
    print("Percentage of elements in area for python's RNG : "+str(value_py))
    print("")
    print("Percentage of error for LC RNG : "+str(math.fabs(area-value_lc)/area))
    print("Percentage of error for LR RNG : "+str(math.fabs(area-value_lr)/area))
    print("Percentage of error for Python's RNG : "+str(math.fabs(area-value_py)/area))

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
