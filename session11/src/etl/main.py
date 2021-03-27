import os
import sys

current_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.abspath(current_dir + "/../service"))

from operand import Operand

if __name__ == "__main__":
    # obj_operand = Operand(2,10,'kuadrat')
    # obj_operand = Operand(2,10,'plus1')
    obj_operand = Operand(2,10,'kuadrat')
    print(obj_operand.fnc_plus1())
    print(obj_operand.fnc_kuadrat())
    print(obj_operand.fnc_fibonacci())