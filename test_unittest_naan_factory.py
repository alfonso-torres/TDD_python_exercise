# Exercise TDD Bread Factory!

# User stories for Naan Factory to test:
# 1. As a user, I can use the make dough with 'water' and 'flour' to make 'dough'.
# 2. As a user, I can use the bake dough with dough to get naan.
# 3. As a user, I can use the run factory with water and flour and get naan.

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

