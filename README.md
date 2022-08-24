# Project Goals
This repository has a end-to-end Data Science project, about climate predictions. It's a particular project that I'm working just myself, to improve my engineering and data analysis-science skills. The main goal is to create a pipeline that always show to the user what is the probability of raining in the next hour.

# Project Description
In resume, this project was splited into this parts:
  - Env: Google Cloud Plataform
  - Data Source: REST API (Rapid API)
  - Tools: Python, Cloud Functions, Cloud Scheduler, Cloud Storage, BigQuery

![arquitetura_projeto](https://user-images.githubusercontent.com/69798348/183543416-efae124b-27f0-45ab-bcd6-4abb1d2b5a46.PNG)

# Documentation

# Data Source Info:
This API bring the climate info about some region passed in the parameters. For example, if you pass "London", then you receive London Climate info, as Temp, Wind direction, kpm wind, sky condition, etc. The API refresh this info every 15 minutes, thus you have 4 registers per hour about the region you want.

# get_data.py:
Runs every 15 minutes. Just collect the data from the API, store at google cloud storage as a parquet file and insert it into a bigquery table.

# model_pipeline.py:
Run once per day. Runs a pipeline that train a random forest algorithm (best evaluated model based on AUC with CV), witch best parameters were already choosed and store it at cloud storage as a pickle file.

# gen_predictions.py:
Runs every 15 minutes. Take the last model trained, the last data collected, generate predictions and save those predictions as a parquet file on cloud storage.

# api_predictions.py:
Endpoint with predictions results with climate condiction in the next hour that updates every 15 minutes.
Endpoint: https://api-predictions-ujarjpjbzq-uc.a.run.app/predictions
Type: Get
Authentication: No

# Simple dashboard about the data colleted:

Dashboard link - https://datastudio.google.com/s/p268nZ5P8DM (Ps: This dash has a default date filter, it always bring the last 14 days. It can be changed by clicking on filter box)

# Next Steps!
- Use spark dataframes to speed up this proccess.
- Create an API endpoint to delivery predictions.
