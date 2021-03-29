# TDD (Test Driven Development) EXERCISE - PYTHON

## <u>Exercise 1: TDD Bread Factory!</u>

TDD bread factory is the latest bread brand in Py Land. It always produces the best bread because it has the best testing strategy! What they do is before they make any new bread, they make a test to make sure the end ouput is correct. Then they adjust the recipe until it's just right!
You are going to do the same with bread! This is called Test Driven Development.

***__Tasks__***:

This exercise is going to bring together lots of concepts.

- Learning outcomes:
1. git
2. github
3. functions
4. TDD
5. Separation of concerns - this is important do not ignore!
6. DRY code
7. DOD
- Installing and running:

To run the naan factory do the following:
````python
import naan_factory
run_factory()
````
- TDD - test driven developmeent:
1. Write the test
2. Run it, and read the error
3. Code and make it pass the test

This helps with:
- Stop over engineering
- Maintainable code
- Reduce technical debt
- Goes well with agile and working code
- errors can be your guide in complex systems

How it works is that we write unit tests.

- Unit Test:

Test single pieces of code. Like a function.<br/>
Base of a test, usually has 3 phases:
1. setup phase (know variables)
2. calling of the function / piece of code with know variables
3. asserting for expect output

- User stories for Naan Factory:
1. As a user, I can use the make dough with 'water' and 'flour' to make 'dough'.
2. As a user, I can use the bake dough with dough to get naan.
3. As a user, I can use the run factory with water and flour and get naan.

***__Acceptance Criteria__***:

- You have written tests.
- Test pass.
- You have written more test to make sure everything works as indented.
- All user stories are satisfied.
- Code does not break.
- Code has exit condition.
- DOD if followed.

## ***__Solution__***:

1. We need to create tests for `naan_factory.p` in `test_unittest_naan_factory.py`:
````python
import naan_factory
# importing the file and class where we would write our code

import unittest
# importing unittest to inherit TestCase to create our tests against the code

class NaanFactoryTest(unittest.TestCase):

    naan = naan_factory.NaanFactory() # Creating an object of our NaanFactory() class

    def test_make_dough(self):
        self.assertEqual(self.naan.make_dough("water", "flour"), "dough")
        # this test is checking if the words are water and flour to make dough

    def test_bake_dough(self):
        self.assertEqual(self.naan.bake_dough("dough"), "naan")
        # this test is checking if the word match with dough to make bake dough -> naan as result

    def test_run_factory(self):
        self.assertEqual(self.naan.run_factory("water", "flour"), "naan")
        # this test is checking if all the program works properly. We make dough and bake dough to get naan as a result
````
2. We need to create the class NaanFactory in the file `naan_factory.py` to create the tests that will be running:
````python
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
````
3. Finally, let's run the following command to check if it will get over all the tests:
````commandline
python -m pytest
````
````
========================================================================================================== test session starts ===========================================================================================================
platform win32 -- Python 3.9.2, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
rootdir: C:\Users\alfonso\PycharmProjects\TDD_python_exercise
collected 3 items                                                                                                                                                                                                                         

test_unittest_naan_factory.py ...                                                                                                                                                                                                   [100%]

=========================================================================================================== 3 passed in 0.77s ============================================================================================================
````
