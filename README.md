# COVID Data

## Project Overview

### Description

COVID Data is a small ETL project that gets COVID-related data from the COVID-19 Data Repository by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University (https://github.com/CSSEGISandData/COVID-19/tree/master). 
This project uses Mage.AI for orchestration, DBT for transformation, Postgres for warehousing, and allows visualization of the data via Jupyter Notebook.

## Setup Instructions

### Running Mage and Postgres

1. Make sure you have Docker installed (https://www.docker.com/products/docker-desktop/)
2. Simply run `docker compose up` in the main directory
    - This will pull the Mage and Postgres docker images and run it within a container on your system
3. To access Mage, go to `http://localhost:6789` on your browser
4. Inside Mage you may:
    - Process a backfill for pipeline `csse_jhu_covid_data`	to load data for certain dates into raw tables (ends Mar 9, 2023)
    - Run pipeline `dbt_run` to process data from raw tables and publish them onto the main tables

### Running Jupyter Notebook
1. Make sure you have Pipenv installed (https://pipenv.pypa.io/en/latest/installation.html)
2. Go to the `notebooks` directory, and run `pipenv install`
    - This will install all the libraries and dependencies that jupyter notebook needs according to the Pipfile
3. Run `pipenv run jupyter notebook`
4. You may access the analysis file `COVID Data Analysis.ipynb`

## Technologies Used

1. **Mage AI:** I leveraged Mage AI for its powerful automation capabilities, which greatly streamlined our data extraction process.
3. **dbt (Data Build Tool):** dbt played a pivotal role in our data transformation phase. Its SQL-based modeling approach made it easy to define and manage our data transformations efficiently.
4. **PostgreSQL:** I opted for PostgreSQL as the database system due to its reliability, performance, and advanced SQL features. It's been instrumental in storing and managing the data retrieved from our source.
5. **Jupyter Notebook:** For data exploration, analysis, and prototyping, Jupyter Notebook was indispensable. Its interactive nature allowed us to experiment with data transformations and gain valuable insights before finalizing our ETL pipeline.

## Assumptions and Data Analysis

1. What are the top 5 US states with highest confirmed cases for a certain date?
    - The table shows the top 5 states with the highest confirmed cases on Sep 1, 2020. California has the highest number of confirmed cases at 717,892. Texas follows with 658,712 cases. Florida, New York and Georgia round out the top 5 with 631,040, 437,757 and 272,697 confirmed cases respectively.
![Highest Cases](./images/1.png)

2. What is the trend in number of active COVID cases over time?
    - The line graph depicts the trend of active COVID-19 cases in the United States from September 1st, 2020, to September 30th, 2020. The y-axis represents the number of active cases, ranging from 3.7 million to 4.2 million. The graph reveals a clear upward trend, signifying a continuous rise in active cases throughout the month. Despite some fluctuations, the overall pattern indicates a worsening of the situation during this period.
![Active Cases Trend](./images/2.png)

4. What is the correlation between confirmed cases and deaths? (by date)
    - Investigating the correlation between confirmed COVID-19 cases and deaths over a specific time period, the analysis revealed a very strong positive correlation, with a coefficient of 0.9983. The top line tracked the number of confirmed cases, while the bottom line represented deaths. Both lines displayed an upward trend, signifying a rise in both cases and deaths over time. There were minor fluctuations in daily counts, but the overall pattern suggested a clear connection: as confirmed cases increased, deaths also tended to increase.
![Correlation](./images/3.png)
