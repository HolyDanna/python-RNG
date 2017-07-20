# Just a small function to be able to know if the m we'll use is prime or not
def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True


class LCR(object):
    def __init__(self, m = 2**31-1, a = 16807, z=891):
        # It is possible to change the default values by specifying the values
        # for the parameters
        # note that if the given m value is not prime, we'll use the prime number
        # 2^31-1
        # The values of a and z are also kept below the value of m
        super(LCR, self).__init__()
        if isprime(m):
            self.m = m
        else:
            self.m = 2**31-1
        self.a = a % self.m
        if self.a == 0 or self.a == 1:
            self.a = 16807
        self.z = z % self.m
        if self.z == 0:
            self.z = 891
        # We do not check if the number will be too high as Python does not have
        # a defined MAX_INT value, thus not creating problem in the a*z multiplication

    # returns a random number between 0 and 1 (strictly different from both)
    def rand(self):
        self.z = self.z*self.a % self.m
        return self.z/self.m

    # returns a random integer between 0 and i-1
    def randint(self, i):
        self.z = self.z*self.a % self.m
        return int(self.z*i/self.m)
