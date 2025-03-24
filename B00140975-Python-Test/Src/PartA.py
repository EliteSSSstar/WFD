# pet and attribute classes  name, age, sex , petID, OWNER name
from pyodbc import STRING

#forced String and ints
# Owner class
class owner():
    def __init__(self, owner_name):
        self.owner_name = owner_name # owner name

# pet class
class pet(): # parent class pet attributes
    def __init__(self, name, age, sex, petID):
        self.name = name
        self.age = age
        self.sex = sex
        self.petID = petID

    def print_attributes(self): # print attributes
        print(f"Name: {self.name}, age: {self.age,}, sex: {self.sex}, petID: {self.petID}")


    def update_name(self, new_name): # update name
        if isinstance(new_name, str):
            self.name = new_name

    # update age
    def update_age(self, new_age):
        if isinstance(new_age, int):
            self.age = new_age

    # update_sex
    def update_sex(self, new_sex):
        if isinstance(new_sex, str):
            self.sex = new_sex
    # update petID
    def update_petID(self, new_petID):
        if isinstance(new_petID, int):
            self.petID = new_petID

# cat class child inheriting from pet class
class cat(pet):
    def __init__(self, name, age, sex, petID, breed):
        super().__init__(name, age, sex, petID)
        self.breed = breed

    def print_attributes(self): # print attributes
        super().print_attributes()
        print(f"Breed: {self.breed}")

    def update_breed(self, new_breed): # update breed with self
        if isinstance(new_breed, str):
            self.breed = new_breed


# call pet class and give attributes
pet1 = pet("Bella", 3, "Female", 1111)
pet1.print_attributes() # initialise pet attributes

cat1 = cat ("Tom", 2, "Male", 2222, "snowshoe")
cat1.print_attributes() # initialise cat attributes


print("Enter Owner Name: ")
owner1 = str(owner(input())) # owner name input

print("pick pet")
print("Enter No.1 for dog, OR No.2 for cat")
animal = int(input()) # input for deciding animal input

if animal == "1": # if animal is 1 then do this
    # Using user input
    name = str(input("Enter pet name: "))
    age = int(input("Enter pet age: "))
    sex = str(("Enter pet sex: "))
    petID = int(input("Enter pet ID: "))

    pet1 = pet(name, age, sex, petID) # pet attributes
    pet1.print_attributes(), print("Owner: ", owner1.owner_name)


elif animal == "2":
    # Using user input
    name = str(input("Enter pet name: "))
    age = int(input("Enter pet age: "))
    sex = str(input("Enter pet sex: "))
    petID = int(input("Enter pet ID: "))
    pet_bread = str(input("Enter pet breed: "))

    cat1 = cat(name, age, sex, petID, pet_bread)
    cat1.print_attributes(),print("Owner: ", owner1.owner_name)







