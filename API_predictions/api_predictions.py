from flask import Flask, jsonify
from google.cloud import storage
from google.oauth2 import service_account
import os
import pandas as pd


app = Flask(__name__)

@app.get("/predictions")

def get_predictions():
    try:
        storage_client = storage.Client()
    except:
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"C:\Users\Phelipe\Downloads\weather-project-305419-fc9b2230cc12.json"
        storage_client = storage.Client()

    bucket = storage_client.get_bucket('weather_prediction_files')
    all_blobs = list(storage_client.list_blobs(bucket))
    last_file_name = all_blobs[-1].name
    blob = bucket.get_blob(last_file_name)
    obj = blob.download_as_string()
    df = pd.read_parquet(f"gs://{'weather_prediction_files'}/{last_file_name}")

    return df.to_json(), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)), use_reloader=False)