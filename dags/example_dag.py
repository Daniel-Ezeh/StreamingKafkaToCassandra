from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator


default_args = {
    'owner': 'Daniel',
    'start_date': datetime(2024, 6, 3, 10, 00)
}


with DAG(
    'Test',
    default_args=default_args,
    schedule='@daily',
    catchup=False
         ) as dag:
    
    t1 = EmptyOperator(task_id="start")
    
    # streaming_task = PythonOperator(
    #     task_id='streaming_data_from_api',
    #     python_callable=stream_data
    # )

