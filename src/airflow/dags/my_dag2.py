from datetime import datetime

import airflow
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'start_date': datetime(2019, 1, 1),
}

dag = DAG(
    dag_id='my_dag_long2',
    default_args=default_args,
    schedule_interval='50 * * * *',
)

for i in range(3):
    task = BashOperator(
        task_id='runme_' + str(i),
        bash_command='echo "{{ task_instance_key_str }}" && sleep 1800 && echo "done"',
        dag=dag,
    )
