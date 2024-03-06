from airflow import DAG
from datetime import timedelta, datetime
from airflow.operators.dummy_operator import DummyOperator

default_args = {
        'owner' : 'airflow',
        'start_date' : datetime(2024, 2, 6),

}

dag = DAG(dag_id='DAG-1',
        default_args=default_args,
        schedule_interval='@once', 
        catchup=False
    )

 start = DummyOperator(task_id = 'start', dag = dag)
 end = DummyOperator(task_id = 'end', dag = dag)

start >> end 
