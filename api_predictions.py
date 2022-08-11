from flask import Flask, jsonify
from google.cloud import bigquery
from google.oauth2 import service_account
import os
import pandas as pd

app = Flask(__name__)

@app.get("/predictions")

def get_predictions():
    try:
        bq_client = bigquery.Client()
    except:
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"C:\Users\Phelipe\Downloads\weather-project-305419-fc9b2230cc12.json"
        bq_client = bigquery.Client()

    df = (
        bq_client.query("SELECT * FROM `weather-project-305419.Daily_Weather.predictions` LIMIT 10")
        .result()
        .to_dataframe()
    )

    return jsonify(df.to_dict()), 200

if __name__ == '__main__':
    app.run(debug=True, port=8000, use_reloader=False)