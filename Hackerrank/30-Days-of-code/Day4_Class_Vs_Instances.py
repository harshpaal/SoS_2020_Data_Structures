class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        self.initialAge = initialAge
        if self.initialAge<0:
            self.initialAge = 0
            print("Age is not valid, setting age to 0.")

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.initialAge<13:
            print("You are young.")
        if self.initialAge>=13:
            if self.initialAge<18:
                print("You are a teenager.")
        if self.initialAge>=18:
            print("You are old.")


    def yearPasses(self):
        self.initialAge+=1

        # Increment the age of the person in here

