---
layout: default
title: "Apache Airflow"
---

<div class="learning-content">

# Apache Airflow - Production Workflow Orchestration

Apache Airflow is a powerful, open-source platform to programmatically author, schedule, and monitor workflows. It's the industry standard for data pipeline orchestration.

## Table of Contents

1. [Core Concepts](#core-concepts)
2. [Getting Started](#getting-started)
3. [Building DAGs](#building-dags)
4. [Operators & Tasks](#operators--tasks)
5. [Advanced Features](#advanced-features)
6. [Best Practices](#best-practices)

---

## Core Concepts

### What is Apache Airflow?

Airflow is a workflow orchestration tool that allows you to:
- **Define workflows as code** - Python-based DAGs for version control
- **Schedule tasks** - Cron-like scheduling with flexibility
- **Monitor execution** - Beautiful UI with rich logging
- **Handle failures** - Retry mechanisms and error callbacks
- **Scale horizontally** - Distributed execution with Executors

### Key Terminology

**DAG (Directed Acyclic Graph)**: A collection of tasks organized with dependencies  
**Task**: A unit of work (operator instance)  
**Operator**: A Python class that defines what a task does  
**Task Instance**: A specific run of a task for a given DAG run  
**Executor**: What runs tasks (Local, Celery, Kubernetes, etc.)  

---

## Getting Started

### Installation and Setup

```bash
# Install Airflow
pip install apache-airflow==2.6.0

# Set AIRFLOW_HOME environment variable
export AIRFLOW_HOME=~/airflow

# Initialize the database
airflow db init

# Create admin user
airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com

# Start the web server
airflow webserver --port 8080

# Start the scheduler (in another terminal)
airflow scheduler
```

### Basic Directory Structure

```
airflow_home/
├── dags/                 # DAG definitions
├── logs/                 # Task logs
├── plugins/              # Custom operators/hooks
├── airflow.cfg          # Configuration file
└── airflow.db           # SQLite metadata database
```

---

## Building DAGs

### Simple DAG Example

```python
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

# Define default arguments
default_args = {
    'owner': 'data-team',
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2024, 1, 1),
    'email': ['alert@example.com'],
    'email_on_failure': True,
}

# Create DAG
dag = DAG(
    'simple_etl_pipeline',
    default_args=default_args,
    description='A simple ETL pipeline',
    schedule_interval='@daily',  # Run daily
    catchup=False,               # Don't backfill
)

# Define Python functions
def extract_data():
    print("Extracting data from API...")
    return {"rows": 1000}

def transform_data(**context):
    ti = context['task_instance']
    data = ti.xcom_pull(task_ids='extract')
    print(f"Transforming {data['rows']} rows...")
    return f"Transformed {data['rows']} rows"

# Define tasks
extract_task = PythonOperator(
    task_id='extract',
    python_callable=extract_data,
    dag=dag,
)

# Define tasks
extract_task = PythonOperator(
    task_id='extract',
    python_callable=extract_data,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform',
    python_callable=transform_data,
    provide_context=True,
    dag=dag,
)

load_task = BashOperator(
    task_id='load',
    bash_command='echo "Loading data into warehouse..."',
    dag=dag,
)

# Set dependencies
extract_task >> transform_task >> load_task
```

### DAG with Error Handling

```python
def task_failure_callback(context):
    """Called when a task fails"""
    task_instance = context['task_instance']
    print(f"Task {task_instance.task_id} failed!")
    # Send alert, log error, etc.

def task_success_callback(context):
    """Called when a task succeeds"""
    task_instance = context['task_instance']
    print(f"Task {task_instance.task_id} succeeded!")

task = PythonOperator(
    task_id='risky_task',
    python_callable=risky_function,
    on_failure_callback=task_failure_callback,
    on_success_callback=task_success_callback,
    dag=dag,
)
```

---

## Operators & Tasks

### Common Operators

```python
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.operators.email import EmailOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.operators.dummy import DummyOperator

# Python Operator
python_task = PythonOperator(
    task_id='python_task',
    python_callable=my_function,
)

# Bash Operator
bash_task = BashOperator(
    task_id='bash_task',
    bash_command='python /scripts/etl.py',
)

# Email Operator
email_task = EmailOperator(
    task_id='send_email',
    to='user@example.com',
    subject='Pipeline Complete',
    html_content='<p>ETL pipeline completed successfully</p>',
)

# Trigger another DAG
trigger_task = TriggerDagRunOperator(
    task_id='trigger_downstream',
    trigger_dag_id='downstream_dag_id',
)
```

### Working with XCom (Cross Communication)

```python
def extract_task():
    return [1, 2, 3, 4, 5]

def transform_task(**context):
    # Pull data from upstream task
    data = context['task_instance'].xcom_pull(task_ids='extract')
    print(f"Received data: {data}")
    # Push data for downstream tasks
    return sum(data)

extract = PythonOperator(
    task_id='extract',
    python_callable=extract_task,
    dag=dag,
)

transform = PythonOperator(
    task_id='transform',
    python_callable=transform_task,
    provide_context=True,
    dag=dag,
)

extract >> transform
```

---

## Advanced Features

### Branching Logic

```python
from airflow.operators.python import BranchPythonOperator

def decide_branch(**context):
    if some_condition:
        return 'task_a'
    else:
        return 'task_b'

branch_task = BranchPythonOperator(
    task_id='branch',
    python_callable=decide_branch,
    provide_context=True,
    dag=dag,
)

task_a = PythonOperator(task_id='task_a', ...)
task_b = PythonOperator(task_id='task_b', ...)
end_task = DummyOperator(task_id='end')

branch_task >> [task_a, task_b] >> end_task
```

### Dynamic Task Generation

```python
from airflow.models import Variable

# Get list of tables to process
tables = ['users', 'orders', 'products']

# Create tasks dynamically
for table in tables:
    process_table = PythonOperator(
        task_id=f'process_{table}',
        python_callable=process_table_func,
        op_kwargs={'table': table},
        dag=dag,
    )

    extract_task >> process_table >> load_task
```

### Passing Configuration

```python
# DAG with parameters
dag = DAG(
    'configurable_dag',
    params={
        'environment': 'production',
        'job_id': 123,
    },
)

def run_job(**context):
    env = context['params']['environment']
    job_id = context['params']['job_id']
    print(f"Running job {job_id} in {env}")
```

---

## Best Practices

### 1. **Idempotent Tasks**
Every task should produce the same result when run multiple times.

```python
def idempotent_load(**context):
    # Use MERGE or DELETE+INSERT instead of direct INSERT
    # or write to a timestamped partition
    execution_date = context['execution_date']
    partition = execution_date.strftime('%Y%m%d')
    # Load to /data/2024/01/15/ (idempotent)
```

### 2. **Proper Error Handling**
```python
from airflow.exceptions import AirflowException

def robust_task():
    try:
        result = perform_operation()
    except SpecificError as e:
        # Handle expected errors
        return None
    except Exception as e:
        raise AirflowException(f"Unexpected error: {str(e)}")
    return result
```

### 3. **Use Sensors for Waiting**
```python
from airflow.sensors.filesystem import FileSensor
from airflow.sensors.sql import SqlSensor

# Wait for file
wait_for_file = FileSensor(
    task_id='wait_for_file',
    filepath='/data/input.csv',
    poke_interval=60,
    timeout=300,
)

# Wait for query result
wait_for_data = SqlSensor(
    task_id='wait_for_data',
    conn_id='postgres_default',
    sql='SELECT COUNT(*) FROM table WHERE date = {{ ds }}',
    allowed_states=['success'],
)
```

### 4. **Implement Logging**
```python
import logging

logger = logging.getLogger(__name__)

def log_task():
    logger.info("Starting task execution")
    logger.error("An error occurred")
    logger.warning("Be careful!")
```

### 5. **Test Your DAGs Locally**
```bash
# Validate DAG syntax
airflow dags validate

# Test a specific task
airflow tasks test my_dag my_task 2024-01-01

# Dry run (tests task without executing)
airflow dags test my_dag 2024-01-01
```

---

## Resources

- **Official Documentation**: [airflow.apache.org](https://airflow.apache.org/)
- **Airflow Tutorial**: Comprehensive guide on Apache Airflow
- **Community**: Active Slack channel and GitHub discussions
- **Deployment**: Helm charts for Kubernetes deployment

---

**Last updated**: April 12, 2026  
**Difficulty**: Intermediate to Advanced  
**Prerequisites**: Python, understanding of ETL concepts

</div>
