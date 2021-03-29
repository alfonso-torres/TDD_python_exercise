# Exercise TDD Bread Factory!

import naan_factory
import unittest

class NaanFactoryTest(unittest.TestCase):

    naan = naan_factory.NaanFactory()

    def test_make_dough(self):
        self.assertEqual(self.naan.make_dough("water", "flour"), "dough")

    def test_bake_dough(self):
        self.assertEqual(self.naan.bake_dough("dough"), "naan")

    def test_run_factory(self):
        self.assertEqual(self.naan.run_factory("water", "flour"), "naan")

