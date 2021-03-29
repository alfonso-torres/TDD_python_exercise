class NaanFactory:
    # pass

    # This function check if the two values are water and flour to make dough
    def make_dough(self, value1, value2):
        if value1 == "water" and value2 == "flour":
            return "dough"
        elif value1 == "flour" and value2 == "water":
            return "dough"
        else:
            return "wrong words"

    # This function check if we have made a dough, so it is the word dough, to bake dough
    def bake_dough(self, value1):
        if value1 == "dough":
            return "naan"
        else:
            return "wrong words"

    # Function to check if all the program works correctly. We make dough and bake dough to get the result
    def run_factory(self, value1, value2):
        result1 = self.make_dough(value1, value2)
        result2 = self.bake_dough(result1)
        return result2

# Let's see what values want to add from the customer to make the dough
#print("WELCOME!")
#print("Let's go to check if you want to make naan!")
#run_program = True
#class_naan = NaanFactory()
#while run_program:
#    user_input = input("Would you like to continue? (GO/EXIT): ")
#    if user_input == "EXIT":  # If they want to exit
#        run_program = False
#    elif user_input == "GO":
#        value1 = input("Please enter the first value: ") # Ask the first value
#        value2 = input("Please enter the second value: ") # Ask the second value
#        print("The result is : ")
#        print(NaanFactory.run_factory(class_naan, value1, value2)) # Run factory to check if they get naan as a result
#    else:
#        print("Try again...")
