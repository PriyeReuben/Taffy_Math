import random as rand

class Taffy:
    def __init__(self):
        self.min = 3 # int(input("Minimum Value?"))
        self.max = 12 # int(input("Maximum Value?"))
        rand.randint


    def math(self):


        r1 = rand.randint(0, self.max - self.min) + self.min
        r2 = rand.randint(0, self.max - self.min) + self.min


        true_value = r1 * r2  #real value
        false_value = slightly_wrong(r1, r2, true_value)

        given = rand.randint(1,2)
        if given==1:
            gValue = true_value
        elif given==2:
            gValue = false_value
        else:
            print("Something went wrong")

        expression = "{} * {} = {}".format(r1, r2, gValue)
        #print(expression)
        return(expression,true_value,false_value, gValue)

def slightly_wrong(r1, r2, true):  # r1, r2, true_
    approx1 = r1 * rand.uniform(1.01, 1.03)
    approx2 = r2 * rand.uniform(1.01, 1.03)
    false_value = int(approx1 * approx2)

    if false_value == true:
        false_value = false_value + rand.randint(1, 4)
        #print("Real {},{},{} Fake {},{},{}".format(r1, r2, true, approx1, approx2, false_value))
        return false_value
    else:
        return false_value

def workhorse():
    t = Taffy()
    for x in range(10):
        t.math(1)
