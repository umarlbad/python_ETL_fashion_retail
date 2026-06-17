# python_ETL_fashion_retail
Create an ETL Pipeline with fashion retail dataset from Dicoding's Project

# **Automated Fashion Retail ETL Pipeline**
## 1. Overview

This project demonstrates the development of an automated Extract, Transform, and Load (ETL) pipeline for fashion retail product data.

The pipeline extracts product information from a public e-commerce website, performs data cleaning and transformation processes, and loads the processed data into multiple storage destinations including CSV files, PostgreSQL databases, and Google Sheets.

The project was developed as part of the Dicoding Data Engineering learning path and follows software engineering best practices through modular architecture, automated testing, and reproducible data workflows.

## Key Features
- Automated web scraping for product data extraction
- Data cleaning and validation
- Data transformation and standardization
- Multi-destination data loading:
  - CSV
  - PostgreSQL
  - Google Sheets
- Automated unit testing using PyTest
- Modular ETL architecture

## 2. Tech Stack
- Python
- Pandas
- Requests
- BeautifulSoup
- PostgreSQL
- Google Sheets API
- PyTest

## 3. Workflow

Extract -> Transform -> Load -> Validation & Testing

## 4. Project Objectives
- Build a production-style ETL pipeline
- Apply data engineering best practices
- Ensure data quality through automated testing
- Demonstrate integration with multiple storage systems
---

## The Modular Programs
fashion-retail-etl-pipeline/
│
├── data/
├── utils/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── tests/
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_load.py
│
├── main.py
├── requirements.txt
├── submission.txt
└── README.md

---

## Portfolio Highlights

This project demonstrates:
* Data extraction from web sources using web scraping techniques.
* Data preprocessing and transformation using Pandas.
* Data loading into relational databases and cloud-based spreadsheets.
* Automated testing and validation using PyTest.
* Modular and maintainable Python project structure.
* End-to-end ETL workflow development commonly used in data engineering environments.

---
## Results

- Successfully extracted product data from multiple web pages.
- Cleaned and standardized product information.
- Loaded transformed data into PostgreSQL and Google Sheets.
- Achieved 69% automated test coverage using PyTest.
