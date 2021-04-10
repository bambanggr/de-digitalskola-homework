import pandas as pd
import unittest
import os
import sys

current_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.abspath(current_dir + "/../../src/service"))

from covid import Covid

colnames = ['id_kel','nama_provinsi','nama_kota','nama_kecamatan','nama_kelurahan','positif','sembuh','meninggal','presentase_sembuh','presentase_meninggal']

class DfTests(unittest.TestCase):
    def setUp(self):
        try:
            # current_dir = os.path.abspath(os.path.dirname(__file__))
            # # print(current_dir)
            # sys.path.append(os.path.abspath(current_dir + "/../files"))
            # folder_name = sys.path[len(sys.path)-1]
            # data = pd.read_csv(folder_name+"\data-covid.csv")
            obj_covid = Covid()
            # print(obj_covid.get_meninggal())
            self.fixture = obj_covid.get_meninggal()
        except IOError as e:
            print(e)

    def test_colnames(self):
        self.assertListEqual(list(self.fixture.columns), colnames)
        pass


if __name__ == "__main__":
    unittest.main()