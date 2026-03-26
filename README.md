# Healthcare EDI 837 Claims Data Pipeline

## Overview
This project demonstrates a healthcare data pipeline that processes EDI 837 healthcare claim files
and transforms them into analytics-ready datasets using a Bronze / Silver / Gold architecture.

## Architecture
![Architecture Diagram](architecture/architecture-diagram.png)
EDI 837 → AWS S3 → Lambda Trigger → AWS Glue / Spark → Bronze → Silver → Gold → Snowflake → BI Dashboard

## Technologies
- Python
- AWS S3
- AWS Lambda
- AWS Glue
- Apache Spark
- Snowflake
- Airflow
- SQL
- Delta Lake
- Power BI / Tableau

## Key Features
- EDI 837 healthcare claim ingestion
- Automated ETL pipeline
- Layered data architecture
- Data quality validation
- SQL analytics queries
