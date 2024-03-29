#!/usr/bin/env python
# coding: utf-8
# %%

# %%


import pandas as pd
from flask import Flask, jsonify, render_template, request
import threading

app = Flask(__name__)

# Read the dataset from Excel
def read_dataset_from_excel(filename):
    try:
        dataset = pd.read_excel(filename)
        return dataset
    except Exception as e:
        print("Error:", e)
        return None

# Define the file path
excel_file_path = 'D:/PhD/Data Science/sesame_final_dataset1.xlsx'

# Read the dataset
dataset = read_dataset_from_excel(excel_file_path)

# Define API endpoints

# Endpoint to get all data
@app.route('/api/data', methods=['GET'])
def get_all_data():
    if dataset is not None:
        return jsonify(dataset.to_dict(orient='records'))
    else:
        return jsonify({"error": "Failed to read dataset from Excel file."}), 500

# Endpoint to get data by symbol
@app.route('/api/data/<symbol>', methods=['GET'])
def get_data_by_symbol(symbol):
    if dataset is not None:
        filtered_data = dataset[dataset['Symbol'] == symbol]
        return jsonify(filtered_data.to_dict(orient='records'))
    else:
        return jsonify({"error": "Failed to read dataset from Excel file."}), 500

# Endpoint to get data by warehouse
@app.route('/api/data/warehouse/<warehouse>', methods=['GET'])
def get_data_by_warehouse(warehouse):
    if dataset is not None:
        filtered_data = dataset[dataset['Warehouse'] == warehouse]
        return jsonify(filtered_data.to_dict(orient='records'))
    else:
        return jsonify({"error": "Failed to read dataset from Excel file."}), 500

# Endpoint to render index.html
@app.route('/', methods=['GET'])
def render_index():
    return render_template('index.html')

# Run the Flask app in a separate thread
def run_flask_app():
    app.run(debug=True, use_reloader=False)

if __name__ == '__main__':
    threading.Thread(target=run_flask_app).start()

