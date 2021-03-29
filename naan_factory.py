class NaanFactory:
    # pass

    def make_dough(self, value1, value2):
        if value1 == "water" and value2 == "flour":
            return "dough"
        elif value1 == "flour" and value2 == "water":
            return "dough"
        else:
            return "wrong words"

    def bake_dough(self, value1):
        if value1 == "dough":
            return "naan"
        else:
            return "wrong words"

    def run_factory(self, value1, value2):
        result1 = self.make_dough(value1, value2)
        result2 = self.bake_dough(result1)
        return result2


print("WELCOME!")
print("Let's go to check if you want to make naan!")
run_program = True
class_naan = NaanFactory()
while run_program:
    user_input = input("Would you like to continue? (GO/EXIT): ")
    if user_input == "EXIT":  # If they want to exit
        run_program = False
    elif user_input == "GO":
        value1 = input("Please enter the first ingredient: ")
        value2 = input("Please enter the second ingredient: ")
        print("The result is : ")
        print(NaanFactory.run_factory(class_naan, value1, value2))
    else:
        print("Try again...")
