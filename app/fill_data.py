import json
from os import getenv

from app.connection import collection

def fill_data_if_empty():
    json_file_path = getenv("JSON_FILE_PATH", "app\employee_data_advanced.json")

    if collection.count_documents({}) == 0:
        with open(json_file_path, "r", encoding="utf-8") as file:
            file_data = json.load(file)

        ins_result = collection.insert_many(file_data)
        print(f"Data inserted to MongoDB. Documents inserted: {len(ins_result.inserted_ids)}")