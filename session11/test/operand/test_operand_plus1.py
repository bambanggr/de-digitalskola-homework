import os
import sys
import unittest

current_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.abspath(current_dir + "/../../src/service"))

from operand import Operand

class OperandDefaultTest(unittest.TestCase):
    def setUp(self):
        self.obj_test = Operand(2,10)

    def test_default_plus1(self):
        actual_output = self.obj_test.fnc_plus1()
        print(actual_output)
        expected_output = [2, 3, 4, 5, 6, 7, 8, 9, 10]

        self.assertEqual(actual_output, expected_output)

    def test_default_kuadrat(self):
        actual_output = self.obj_test.fnc_kuadrat()
        print(actual_output)
        expected_output = [2, 4, 8]

        self.assertEqual(actual_output, expected_output)

    def test_default_fibonacci(self):
        actual_output = self.obj_test.fnc_fibonacci()
        print(actual_output)
        expected_output = [2, 3, 5, 8]

        self.assertEqual(actual_output, expected_output)


    # def test_with_argument(self):
    #     new_instance = StringTransformer("Belajar", "Skola")
    #     actual_output = new_instance.transform("Python")
    #     print(actual_output)
    #     expected_output = "Belajar_Python_Skola"

    #     self.assertEqual(actual_output,expected_output)
