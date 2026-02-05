def get_employees_by_lastname_and_age():
    filter_query = {
        "name": {"$regex": "(Nelson|Wright)$"},
        "age": {"$lt": 35},
    }
    projection = {"_id": 0, "name": 1, "age": 1, "job_role.department": 1}
    documents = collection.find(filter_query, projection)
    return list(documents)