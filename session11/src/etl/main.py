import os
import sys

current_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.abspath(current_dir + "/../service"))

from operand import Operand

if __name__ == "__main__":
    obj_operand = Operand()
    print(obj_operand.func(5,100,'plus1'))
    print(obj_operand.func(2,10,'KUADRAT'))
    print(obj_operand.func(43,1000,'fiboNacci'))
