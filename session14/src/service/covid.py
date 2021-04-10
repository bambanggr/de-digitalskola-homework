import pandas as pd
import os
import sys


class Covid():

    def __init__(self):
        pass

    def get_meninggal(self):
            # print("Hello World!")
            # folder_name = "C:\/Users\/bamba\/Documents\/TrainingDE\/DigitalSkola\/de-digitalskola-homework\/session14\/files\/"    
            current_dir = os.path.abspath(os.path.dirname(__file__))
            # print(current_dir)
            sys.path.append(os.path.abspath(current_dir + "/../../files"))
            folder_name = sys.path[len(sys.path)-1]
            read_csv = pd.read_csv(folder_name+"\data-covid.csv")
            df = pd.DataFrame(read_csv)
            # print(df.head(2))
            # """Select Only Specific Column"""
            df_specific_column = df[['id_kel','nama_provinsi','nama_kota','nama_kecamatan','nama_kelurahan','positif','sembuh','meninggal']].copy()
            # """Adding new column presentase sembuh"""
            df_specific_column['presentase_sembuh'] = (df_specific_column['sembuh']/df_specific_column['positif']*100).round(2)
            # """Adding new column presentase meninggal"""
            df_specific_column['presentase_meninggal'] = (df_specific_column['meninggal']/df_specific_column['positif']*100).round(2)
            # """pandas set option to display all column"""
            pd.set_option('display.max_columns', None)
            # """Save output to variable"""
            final_output = df_specific_column[['id_kel','nama_provinsi','nama_kota','nama_kecamatan','nama_kelurahan','positif','sembuh','meninggal','presentase_sembuh','presentase_meninggal']].copy()
            # # print(final_output)
            return final_output