import random as rand


class Taffy:
    def __init__(self):
        self.min = 0 #int(input("Minimum Value?"))
        self.max = 0 #int(input("Maximum Value?"))
        self.r1 = 0 #rand.randint(0, self.max - self.min) + self.min
        self.r2 = 0 #rand.randint(0, self.max - self.min) + self.min
        self.incorrect_value = 0
        self.correct_value = 0
        self.expression = ""
        self.correct_count = 0
        self.incorrect_count = 0
        self.gValue = 0

    def correct_answer(self):
        self.r1 = rand.randint(0, self.max - self.min) + self.min
        self.r2 = rand.randint(0, self.max - self.min) + self.min
        self.correct_value = self.r1 * self.r2  # real value


    def incorrect_answer(self):  # r1, r2, true_
        approx1 = self.r1 * rand.uniform(1.01, 1.03)
        approx2 = self.r2 * rand.uniform(1.01, 1.03)
        temp_false_value = int(approx1 * approx2)

        if temp_false_value == self.correct_answer:
            temp_false_value = temp_false_value + rand.randint(1, 5)
            #does this always happen?
            self.incorrect_value = temp_false_value
        else:
            self.incorrect_value = temp_false_value


    def math(self):
        given = rand.randint(1, 2)
        if given == 1:
            self.gValue = self.correct_value
        elif given == 2:
            self.gValue = self.incorrect_value
        else:
            print("Something went wrong")

        self.expression = "{} * {} = {}".format(self.r1, self.r2, self.gValue)

    def workhorse(self):
        self.min = 3#int(input("Minimum Value?:idk "))
        #print("Minimum:", self.min)
        self.max = 14#int(input("Maximum Value?: "))
        #print("Maximum:", self.max)

        self.correct_answer()
        #print("Seed values:", self.r1, self.r2)
        #print("Correct Answer:", self.correct_value)
        self.incorrect_answer()
        #print("Incorrect Answer:", self.incorrect_value)

        self.math()

        print("Kratos", self.expression)

        # for x in range(10):
        #     t.math(1)

#test = Taffy().workhorse()