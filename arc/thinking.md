## version 1 local working version

### what was broken
- your `routs.py` was forwarding http requests back to the same app (`localhost:8000`), so it never called your mongo query code
- some of your `dal.py` functions return documents with `_id` which is an `ObjectId` and **fastapi can not json serialize it**
- your imports should be package-safe when running with `uvicorn app.main:app`

### update these files

#### `requirements.txt`
```txt
fastapi==0.115.6
uvicorn==0.30.6
pymongo==4.8.0
```

#### `app/main.py`
```python
from fastapi import FastAPI
from app.routs import router

app = FastAPI()
app.include_router(router)
```

#### `app/routs.py`
```python
from fastapi import APIRouter
from app import dal

router = APIRouter()


@router.get("/employees/engineering/high-salary")
def employees_engineering_high_salary():
    return dal.get_engineering_high_salary_employees()


@router.get("/employees/by-age-and-role")
def employees_by_age_and_role():
    return dal.get_employees_by_age_and_role()


@router.get("/employees/top-seniority")
def employees_top_seniority():
    return dal.get_top_seniority_employees_excluding_hr()


@router.get("/employees/age-or-seniority")
def employees_age_or_seniority():
    return dal.get_employees_by_age_or_seniority()


@router.get("/employees/managers/excluding-departments")
def employees_managers_excluding_departments():
    return dal.get_managers_excluding_departments()


@router.get("/employees/by-lastname-and-age")
def employees_by_lastname_and_age():
    return dal.get_employees_by_lastname_and_age()
```

#### `app/connection.py`
```python
from os import getenv
from pymongo import MongoClient

mongo_uri = getenv("MONGO_URI", "mongodb://localhost:27017/")
mongo_db = getenv("MONGO_DB", "testdb")
mongo_collection = getenv("MONGO_COLLECTION", "testcollection")

client = MongoClient(mongo_uri)
db = client[mongo_db]
collection = db[mongo_collection]
```

#### `app/dal.py`
```python
from app.connection import collection

# 1 -----------------
def get_engineering_high_salary_employees():
    filter_query = {"job_role.department": "Engineering", "salary": {"$gt": 65000}}
    projection = {"_id": 0, "employee_id": 1, "name": 1, "salary": 1}
    documents = collection.find(filter_query, projection)
    return list(documents)

# 2 -----------------
def get_employees_by_age_and_role():
    filter_query = {
        "age": {"$gte": 30, "$lte": 45},
        "job_role.title": {"$in": ["Engineer", "Specialist"]},
    }
    projection = {"_id": 0}
    documents = collection.find(filter_query, projection)
    return list(documents)

# 3 -----------------
def get_top_seniority_employees_excluding_hr():
    filter_query = {"job_role.department": {"$ne": "HR"}}
    projection = {"_id": 0}
    documents = collection.find(filter_query, projection).sort("years_at_company", -1).limit(7)
    return list(documents)

# 4 -----------------
def get_employees_by_age_or_seniority():
    filter_query = {
        "$or": [
            {"age": {"$gt": 50}},
            {"years_at_company": {"$lt": 3}},
        ]
    }
    projection = {"_id": 0, "employee_id": 1, "name": 1, "age": 1, "years_at_company": 1}
    documents = collection.find(filter_query, projection)
    return list(documents)

# 5 -----------------
def get_managers_excluding_departments():
    filter_query = {
        "job_role.title": "Manager",
        "job_role.department": {"$nin": ["Sales", "Marketing"]},
    }
    projection = {"_id": 0}
    documents = collection.find(filter_query, projection)
    return list(documents)

# 6 -----------------
def get_employees_by_lastname_and_age():
    filter_query = {
        "$or": [
            {"name": {"$regex": "Wright$"}},
            {"name": {"$regex": "Nelson$"}},
        ],
        "age": {"$lt": 35},
    }
    projection = {"_id": 0, "name": 1, "age": 1, "job_role.department": 1}
    documents = collection.find(filter_query, projection)
    return list(documents)
```

### how to run locally

1) start mongodb
```bash
docker run --name mongodb -p 27017:27017 -d mongo:7
```

2) load your json (uses your existing loader)
```bash
export MONGO_URI="mongodb://localhost:27017/"
export MONGO_DB="testdb"
export MONGO_COLLECTION="testcollection"
export JSON_FILE_PATH="./employee_data_advanced.json"
python app/local_load.py
```

3) run the api
```bash
export MONGO_URI="mongodb://localhost:27017/"
export MONGO_DB="testdb"
export MONGO_COLLECTION="testcollection"
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

4) test one endpoint
```bash
curl -s http://localhost:8000/employees/top-seniority
```

============

## version 2 changes to make for openshift

### 1) do not use localhost for mongodb
- in openshift, `localhost` inside the pod means the **pod itself**
- set `MONGO_URI` to the mongodb service dns name inside the cluster, for example
  - `mongodb://mongodb:27017/` if your service is named `mongodb`

what to change
- in your openshift `Deployment` yaml for the app, add env vars
  - `MONGO_URI=mongodb://mongodb:27017/`
  - `MONGO_DB=testdb`
  - `MONGO_COLLECTION=testcollection`

### 2) make sure mongodb is reachable inside the cluster
- you need a mongodb `Deployment` (or `StatefulSet`) and a `Service` named `mongodb`
- your `mongodb.yaml` should create the service on port `27017`

quick validation commands
```bash
oc get pods
oc get svc
```

### 3) expose the fastapi service (route)
- create a `Service` for your app (port 8000 targetPort 8000)
- then create an openshift `Route` that targets that service
- after that you can call the public url from your browser or curl

commands you will use
```bash
oc get route
oc expose svc/<service-name>
```

### 4) images in openshift must be resolvable
- if your `app.yaml` uses `image: app:latest`, openshift will not magically have that image unless you build and push it somewhere
- choose one approach
  - build and push to a registry you can pull from, then update `image:` to that full name
  - or use openshift build configs if that is what your course expects

### 5) if you keep a script like `json_to_mongo.py`
- do not hardcode an external mongodb host
- use `MONGO_URI` from env so you can point it to the internal service in openshift
- if you need to load json into the mongodb running in openshift, run the loader as
  - a one time job pod, or
  - run it locally with `oc port-forward` to mongodb, then load through the forwarded port

if you paste your current `k8s/app.yaml` and `k8s/mongodb.yaml` contents, i will tell you the exact minimal edits needed for your specific yamls so the app pod connects to mongodb and gets a working route.