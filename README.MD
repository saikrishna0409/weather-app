# Weather Data Pipeline
# 🌦️ Real‑Time Weather Data Pipeline

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![Airflow](https://img.shields.io/badge/Airflow-Orchestration-orange.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)


This project automates the extraction, transformation, and loading (ETL) of weather data. Built by Sai Krishna — Real-time Weather Data Pipeline using Python & Airflow.

## Project Structure
- `dags/`: Airflow DAGs
- `src/`: Source code for ETL
- `config/`: Configuration files
- `tests/`: Unit tests
- `data/`: Raw and processed data
- `great_expectations/`: Data validation
- `dashboard/`: Visualization and reporting

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Run Airflow: `docker-compose up`

## Usage
- Airflow DAGs will automate the pipeline.
- Source code in `src/` handles ETL logic.

## Contributing
Feel free to submit issues or pull requests.
