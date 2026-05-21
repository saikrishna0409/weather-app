from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
sys.path.insert(0, '/opt/airflow/src')
from extract import extract_data
from transform import transform_data
from load import load_data

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

default_dag = DAG(
    'weather_data_pipeline',
    default_args=default_args,
    description='ETL pipeline for weather data',
    schedule_interval='@daily',
    catchup=False,
)

extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=default_dag,
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=default_dag,
)

load_task = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    dag=default_dag,
)

extract_task >> transform_task >> load_task
