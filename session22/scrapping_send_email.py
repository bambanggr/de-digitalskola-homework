import pandas as pd
import os
import sys
from airflow.utils.dates import days_ago
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.email_operator import EmailOperator


args = {
    'owner': 'Airflow',
    'start_date': days_ago(2),
}

dag = DAG(
    dag_id='list_orang_terkaya_indonesia',
    default_args=args,
    schedule_interval=None,
    tags=['orang kaya', 'indonesia']
)

def scrapper():
    URL = "https://id.wikipedia.org/wiki/Daftar_orang_terkaya_di_Indonesia"
    dfs = pd.read_html(URL)
    columns_mapping = {
            "Nomor Urut": "nomor_urut",
            "Nama": "nama",
            "Perusahaan": "perusahaan",
            "Kekayaan Bersih (US$)": "kekayaan_bersih_usd"
        }
    renamed_df = dfs[7].rename(columns=columns_mapping)
    # print(renamed_df)
    current_dir = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(os.path.abspath(current_dir + "/../files"))
    folder_name = sys.path[len(sys.path)-1]
    full_file_path = folder_name+'/list_orang_terkaya_di_indonesia.csv'
    # print(folder_name)
    renamed_df.to_csv(full_file_path,index=False)
    # print(current_dir)
    return full_file_path

scrape_website = PythonOperator(
    task_id='scrape_website',
    python_callable=scrapper,
    dag=dag,
)

send_email = EmailOperator(
        task_id='send_email',
        to='fia.digitalskola@gmail.com',
        subject='Bambang_DigitalSkola_Airflow',
        html_content=""" <h3>Homework 3 Week 8</h3> """,
        files=['/usr/local/airflow/files/list_orang_terkaya_di_indonesia.csv'],
        dag=dag
)

scrape_website >> send_email