from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from etl.spark_etl import *

default_args = {
    "owner": "data_engineer",
    "start_date": datetime(2024,1,1)
}

dag = DAG(
    "healthcare_edi_pipeline",
    default_args=default_args,
    schedule_interval="@daily"
)

run_etl = PythonOperator(
    task_id="run_edi_pipeline",
    python_callable=lambda: print("Run Spark ETL"),
    dag=dag
)