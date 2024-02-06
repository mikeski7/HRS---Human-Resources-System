class MyClass:
    def __init__(self):
        self.attr1 = None
        self.attr2 = None
        self.attr3 = None
        self.attr4 = None
        self.attr5 = None

    def get_attributes(self):
        self.attr1 = input("Enter value for attribute 1: ")
        self.attr2 = input("Enter value for attribute 2: ")
        self.attr3 = input("Enter value for attribute 3: ")
        self.attr4 = input("Enter value for attribute 4: ")
        self.attr5 = input("Enter value for attribute 5: ")


# Create an instance of the class
my_object = MyClass()

# Call the get_attributes() method in a loop to prompt the user for input
while True:
    my_object.get_attributes()
    confirm = input("Do you want to enter values again? (y/n): ")
    if confirm.lower() != "y":
        break