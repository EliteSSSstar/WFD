
import unittest
from PartA import pet, cat

# test class and functions
class TestPet(unittest.TestCase):
    def setUp(self): # set up pet attributes and test
        self.pet = pet("Bella", 3, "Female", 1111)


    def test_print_attributes(self):


        # test attributes for pet
        self.assertEqual(self.pet.name, "Bella")
        self.assertEqual(self.pet.name, "42")
        self.assertEqual(self.pet.age, 3)

        self.assertEqual(self.pet.age, 2.433)

        self.assertEqual(self.pet.sex, "Female")
        self.assertEqual(self.pet.petID, 1111)

# test update functions
    def test_update_name(self):
        self.pet.update_name("Max")
        self.assertEqual(self.pet.name, "Max")

    def test_update_age(self):
        self.pet.update_age(4)
        self.assertEqual(self.pet.age, 4)

        self.pet.update_age(-2)
        self.assertEqual(self.pet.age, -2) # test negative age(raise error)


    def test_update_sex(self):
        self.pet.update_sex("Male")
        self.assertEqual(self.pet.sex, "Male")

    def test_update_petID(self):
        self.pet.update_petID(2222)
        self.assertEqual(self.pet.petID, 2222)

        self.pet.update_petID(-1.13)
        self.assertEqual(self.pet.petID, -1.13) # test negative petID()

class TestCat(unittest.TestCase):
    def setUp(self):
        self.cat = cat("Tom", 2, "Male", 2222, "snowshoe")

    def test_print_attributes(self):
        # test attributes for cat
        self.assertEqual(self.cat.name, "tom")
        self.assertEqual(self.cat.age, 2)
        self.assertEqual(self.cat.sex, "Male")
        self.assertEqual(self.cat.petID, 2222)
        self.assertEqual(self.cat.breed, "snowshoe")
        self.assertEqual(self.cat.breed, "burger") # invalid bread

    def test_update_breed(self):
        self.cat.update_breed("Bread")
        self.assertEqual(self.cat.breed, "Bread") # should be Bread

    def test_update_age(self):
        self.cat.update_age(3)
        self.assertEqual(self.cat.age, 3)
        self.cat.update_age(10000000000)
        self.assertEqual(self.cat.age, 10000000000) # cat will not live this long


if __name__ == '__main__':
    unittest.main()