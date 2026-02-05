----------------------------------------
app/main.py
----------------------------------------
```python
from fastapi import FastAPI

from app.routs import router
from app.seed import seed_data_if_empty

app = FastAPI()
app.include_router(router)


@app.on_event("startup")
def startup():
    seed_data_if_empty()
```

----------------------------------------
app/routs.py
----------------------------------------
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

----------------------------------------
app/connection.py
----------------------------------------
```python
from os import getenv

from pymongo import MongoClient

mongo_uri = getenv("MONGO_URI", "mongodb://mongodb:27017/")
mongo_db = getenv("MONGO_DB", "testdb")
mongo_collection = getenv("MONGO_COLLECTION", "testcollection")

client = MongoClient(mongo_uri)
db = client[mongo_db]
collection = db[mongo_collection]
```

----------------------------------------
app/dal.py
----------------------------------------
```python
from app.connection import collection


def get_engineering_high_salary_employees():
    filter_query = {"job_role.department": "Engineering", "salary": {"$gt": 65000}}
    projection = {"_id": 0, "employee_id": 1, "name": 1, "salary": 1}
    documents = collection.find(filter_query, projection)
    return list(documents)


def get_employees_by_age_and_role():
    filter_query = {
        "age": {"$gte": 30, "$lte": 45},
        "job_role.title": {"$in": ["Engineer", "Specialist"]},
    }
    projection = {"_id": 0}
    documents = collection.find(filter_query, projection)
    return list(documents)


def get_top_seniority_employees_excluding_hr():
    filter_query = {"job_role.department": {"$ne": "HR"}}
    projection = {"_id": 0}
    documents = collection.find(filter_query, projection).sort("years_at_company", -1).limit(7)
    return list(documents)


def get_employees_by_age_or_seniority():
    filter_query = {"$or": [{"age": {"$gt": 50}}, {"years_at_company": {"$lt": 3}}]}
    projection = {"_id": 0, "employee_id": 1, "name": 1, "age": 1, "years_at_company": 1}
    documents = collection.find(filter_query, projection)
    return list(documents)


def get_managers_excluding_departments():
    filter_query = {"job_role.title": "Manager", "job_role.department": {"$nin": ["Sales", "Marketing"]}}
    projection = {"_id": 0}
    documents = collection.find(filter_query, projection)
    return list(documents)


def get_employees_by_lastname_and_age():
    filter_query = {
        "$or": [{"name": {"$regex": "Wright$"}}, {"name": {"$regex": "Nelson$"}}],
        "age": {"$lt": 35},
    }
    projection = {"_id": 0, "name": 1, "age": 1, "job_role.department": 1}
    documents = collection.find(filter_query, projection)
    return list(documents)
```

----------------------------------------
app/seed.py
----------------------------------------
```python
import json
from os import getenv

from app.connection import collection


def seed_data_if_empty():
    json_file_path = getenv("JSON_FILE_PATH", "/app/employee_data_advanced.json")

    if collection.count_documents({}) == 0:
        with open(json_file_path, "r", encoding="utf-8") as file:
            file_data = json.load(file)

        collection.insert_many(file_data)
```

----------------------------------------
Dockerfile
----------------------------------------
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY employee_data_advanced.json ./employee_data_advanced.json

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

----------------------------------------
k8s/app-deployment.yaml
----------------------------------------
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mongo-api-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: mongo-api
  template:
    metadata:
      labels:
        app: mongo-api
    spec:
      containers:
        - name: mongo-api
          image: aharonsegal/mongo-container:latest
          imagePullPolicy: Always
          ports:
            - containerPort: 8000
```

----------------------------------------
k8s/app-service.yaml
----------------------------------------
```yaml
apiVersion: v1
kind: Service
metadata:
  name: mongo-api-service
spec:
  type: ClusterIP
  selector:
    app: mongo-api
  ports:
    - name: http
      port: 8000
      targetPort: 8000
```

----------------------------------------
k8s/app-route.yaml
----------------------------------------
```yaml
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: mongo-api
spec:
  to:
    kind: Service
    name: mongo-api-service
  port:
    targetPort: http
```

----------------------------------------
k8s/mongo-service.yaml
----------------------------------------
```yaml
apiVersion: v1
kind: Service
metadata:
  name: mongodb
spec:
  clusterIP: None
  selector:
    app: mongodb
  ports:
    - name: mongo
      port: 27017
      targetPort: 27017
```

----------------------------------------
k8s/mongo-statefulset.yaml
----------------------------------------
```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: mongodb
spec:
  serviceName: mongodb
  replicas: 1
  selector:
    matchLabels:
      app: mongodb
  template:
    metadata:
      labels:
        app: mongodb
    spec:
      containers:
        - name: mongodb
          image: docker.io/library/mongo:7
          imagePullPolicy: IfNotPresent
          ports:
            - containerPort: 27017
          args: ["--bind_ip_all"]
          volumeMounts:
            - name: mongo-data
              mountPath: /data/db
      volumes:
        - name: mongo-data
          emptyDir: {}
```

----------------------------------------
build and push image
----------------------------------------
```bash
docker build -t aharonsegal/mongo-container:latest .
docker push aharonsegal/mongo-container:latest
```

----------------------------------------
openshift commands
----------------------------------------
```bash
oc project aharon-segal-dev

oc apply -f k8s/

oc rollout restart deploy/mongo-api-deployment
oc rollout restart statefulset/mongodb

oc get pods
oc get svc
oc get statefulset
oc get route

oc logs deploy/mongo-api-deployment
oc logs statefulset/mongodb

oc describe pod mongodb-0
```

Would you like me to continue by reading your **current** `app/main.py` and `app/routs.py` exactly as they are in your repo (paste them), and then I will give you the **minimal diff-only edits** so you can copy-paste without changing anything else?