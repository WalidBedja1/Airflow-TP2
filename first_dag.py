from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def extraire_donnees():
    print("Extraction des données depuis la source")
    print("Données brutes récupérées : 100 lignes")


def transformer_donnees():
    print("Transformation des données en cours")
    print("Nettoyage et normalisation appliqués")


def charger_donnees():
    print("Chargement des données dans la destination")
    print("100 lignes insérées avec succès")


with DAG(
    dag_id="pipeline_etl_simple",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    extraction = PythonOperator(
        task_id="extraction",
        python_callable=extraire_donnees,
    )

    transformation = PythonOperator(
        task_id="transformation",
        python_callable=transformer_donnees,
    )

    chargement = PythonOperator(
        task_id="chargement",
        python_callable=charger_donnees,
    )

    extraction >> transformation >> chargement
