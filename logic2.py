import random as rand


class Taffy:
    def __init__(self):
        self.min = 1  # int(input("Minimum Value?"))
        self.max = 1  # int(input("Maximum Value?"))
        self.r1 = rand.randint(0, self.max - self.min) + self.min
        self.r2 = rand.randint(0, self.max - self.min) + self.min
        self.false_value = 0
        self.true_value = 0
        self.expression =""

    def correct_answer(self):
        true_value = self.r1 * self.r2  # real value
        return true_value


    def slightly_wrong(self):  # r1, r2, true_
        approx1 = self.r1 * rand.uniform(1.01, 1.03)
        approx2 = self.r2 * rand.uniform(1.01, 1.03)
        temp_false_value = int(approx1 * approx2)

        if temp_false_value == self.correct_answer():
            temp_false_value = temp_false_value + rand.randint(1, 5)
            # print("Real {},{},{} Fake {},{},{}".format(r1, r2, true, approx1, approx2, false_value))
            self.false_value = temp_false_value
        else:
            self.false_value = temp_false_value

    def math(self):


        given = rand.randint(1, 2)
        if given == 1:
            gValue = self.true_value
        elif given == 2:
            gValue = self.false_value
        else:
            print("Something went wrong")

        self.expression = "{} * {} = {}".format(self.r1, self.r2, gValue)
        # print(expression)
        #return (expression, true_value, false_value, gValue)

    def workhorse(self):
        t = Taffy()
        for x in range(10):
            t.math(1)
