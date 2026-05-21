# Weather Data Pipeline

This project automates the extraction, transformation, and loading (ETL) of weather data.

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
