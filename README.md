# DAG Airflow Pipeline ETL Simple

## Prérequis

Docker et Docker Compose installés sur la machine.

## Lancer l'environnement airflow

```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml'
mkdir -p ./dags ./logs ./plugins
echo "AIRFLOW_UID=$(id -u)" > .env
docker compose up airflow-init
docker compose up -d
```

Le service est accessible à l'adresse http://localhost:8080.
Identifiants par défaut : airflow / airflow.

## Déployer le DAG

Copier le fichier `first_dag.py` dans le dossier `dags/` :

```bash
cp first_dag.py ./dags/
```

Airflow détecte automatiquement les nouveaux fichiers dans ce répertoire. Le DAG apparaît dans l'interface sous le nom `pipeline_etl_simple`.

## Structure du DAG

Le pipeline suit un flux ETL séquentiel en trois étapes :

**extraction** récupère les données depuis une source. Dans cet exemple la tâche simule une lecture et affiche le nombre de lignes obtenues.

**transformation** prend les données brutes et applique les règles de nettoyage et de normalisation. Elle s'exécute uniquement après la réussite de l'extraction.

**chargement** insère les données transformées dans la destination finale. Elle s'exécute uniquement après la réussite de la transformation.

La dépendance entre les tâches est déclarée explicitement à la fin du fichier :

```python
extraction >> transformation >> chargement
```

Cela garantit qu'une tâche échouée interrompt le reste du pipeline.

## Lancer le DAG manuellement

Dans l'interface web, activer le DAG via le toggle, puis cliquer sur le bouton "Trigger DAG".

En ligne de commande :

```bash
docker compose exec airflow-webserver airflow dags trigger pipeline_etl_simple
```

## Consulter les logs d'une tache

Dans l'interface web, ouvrir la vue "Grid", cliquer sur un carré de tâche, puis sur "Log".

En ligne de commande :

```bash
docker compose exec airflow-webserver airflow tasks logs pipeline_etl_simple extraction <date_execution>
```

## Arrêter l'environnement

```bash
docker compose down
```

Pour supprimer également les volumes et repartir de zéro :

```bash
docker compose down --volumes --remove-orphans
```
"# Airflow-TP2" 
