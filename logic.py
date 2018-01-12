import random as rand

class Taffy():
    def __init__(self):
        self.min = 4
        self.max = 30
        self.r1 = rand.randint(0, self.max - self.min) + self.min
        self.r2 = rand.randint(0 , self.max - self.min) + self.min
        rand.randint
        self.primes = [5,7,11]


    def math(self, sign):

        if sign==1:
            seed1 = rand.randint(0,len(self.primes)-1)
            seed2 = rand.randint(0,len(self.primes)-1)

            tValue = self.r1 * self.r2  #real value
            fValue = int(((tValue + self.primes[seed1]) / 2 * 1.8 + self.primes[seed2]))

            given = rand.randint(1,2)
            if given==1:
                gValue = tValue
            elif given==2:
                gValue = fValue
            else:
                print("Something went wrong")

            expression = "{} * {} = {}".format(self.r1, self.r2, gValue)
            print(expression)

        elif sign==2:  #division to be fixed later
            seed1 = rand.randint(1, len(self.primes))
            seed2 = rand.randint(1, len(self.primes))

            tValue = self.r1 * self.r2  # real value
            fValue = int(((tValue + self.primes[seed1]) / 2 * 1.8 + self.primes[seed2]))

            given = rand.randint(1, 2)
            if given == 1:
                gValue = tValue
            elif given == 2:
                gValue = fValue
            else:
                print("Something went wrong")

            expression = self.r1 + " / " + self.r2 + " =\n " + gValue;
            print(expression)

def workhorse():
    for x in range(10):
        t = Taffy()
        t.math(1)
workhorse()