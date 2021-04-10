import os
import sys

current_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.abspath(current_dir + "/../service"))

from covid import Covid

if __name__=="__main__":
    # print("Hello World!")
    obj_covid = Covid()
    var_meninggal = obj_covid.get_meninggal()
    print(var_meninggal)
