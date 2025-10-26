from src.main import DatabaseConnector
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime   


dag = DAG(
    dag_id='duckdb_to_postgres_etl',
    schedule_interval='@daily',
    start_date=datetime(2025, 11, 1),
    catchup=False
)

def etl_task():
    duckdb_path = '/opt/airflow/data/my_duckdb.db'
    pg_config = {
        'host': 'postgres',
        'database': 'airflow'
    }

