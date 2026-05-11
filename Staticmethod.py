#static method = A method that belong to a class rather than any object from that class
#    used for generally utility function
# Instance Method = Best for operation for instances of the class (object)


class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    #instance method
    # Isko object ka data chahiye
    # isliye self use ho raha hai
    def get_info(self):
        return f"{self.name} = {self.position}"
    

    # Static Method
    # Isko object ki jarurat nahi
    # bas checking karni hai
    @staticmethod
    def is_valid_position(position):
        valid_positions = {"Manager", "Cashier", "coock", "janitor"}
        return position in valid_positions 

employee1 = Employee("Eugune", "Manager")
employee2 = Employee("Squidward", "cashier")
employee3 = Employee("spongebob", "cook")

print(Employee.is_valid_position("Manager"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())