import random as rand

class Taffy:
    def __init__(self):
        self.min = 3 # int(input("Minimum Value?"))
        self.max = 12 # int(input("Maximum Value?"))
        #self.r1 = rand.randint(0, self.max - self.min) + self.min
        #self.r2 = rand.randint(0 , self.max - self.min) + self.min
        rand.randint
        self.primes = [5,7,11]


    def math(self, sign):

        if sign==1:
            seed1 = rand.randint(0,len(self.primes)-1)
            seed2 = rand.randint(0,len(self.primes)-1)

            r1 = rand.randint(0, self.max - self.min) + self.min
            r2 = rand.randint(0, self.max - self.min) + self.min


            true_value = r1 * r2  #real value
            false_value = int(((true_value + self.primes[seed1]) / 2 * 1.8 + self.primes[seed2]))

            given = rand.randint(1,2)
            if given==1:
                gValue = true_value
            elif given==2:
                gValue = false_value
            else:
                print("Something went wrong")

            expression = "{} * {} = {}".format(r1, r2, gValue)
            print(expression)
            return(expression,true_value,false_value, gValue)

        elif sign==2:  #division to be fixed later
            seed1 = rand.randint(1, len(self.primes))
            seed2 = rand.randint(1, len(self.primes))

            true_value = self.r1 * self.r2  # real value
            false_value = int(((true_value + self.primes[seed1]) / 2 * 1.8 + self.primes[seed2]))

            given = rand.randint(1, 2)
            if given == 1:
                gValue = true_value
            elif given == 2:
                gValue = false_value
            else:
                print("Something went wrong")

            expression = self.r1 + " / " + self.r2 + " =\n " + gValue;
            print(expression)

def workhorse():
    t = Taffy()
    for x in range(10):
        t.math(1)
