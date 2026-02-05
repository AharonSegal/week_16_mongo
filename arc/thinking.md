You’re right: **for one MongoDB replica, you can simplify**.

### why i originally had 3 mongo resources
- **StatefulSet needs a “governing service”** named in `spec.serviceName`. In practice this is usually a **headless service** (`clusterIP: None`) so the StatefulSet gets stable pod dns names.
- The extra **normal ClusterIP `mongodb` service** is optional. People add it when they want a single stable name that load-balances across replicas. With **1 replica**, it’s not needed.

If you only want **one MongoDB instance** and **simple**, use **only**:
1) **one headless service** named `mongodb` (also acts as the governing service)
2) **one StatefulSet** named `mongodb`

Then your app connects to: `mongodb://mongodb:27017/`

---

## relevant code change (hardcoded openshift defaults)

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

---

## fixed simple yamls (mongo simplified)

### 1) mongo api deployment + service + route (keep as you had, just clean)
----------------------------------------
k8s/01-mongo-api.yaml
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
---
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
---
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

### 2) mongodb headless service + statefulset (only 2 resources, in 1 yaml file)
----------------------------------------
k8s/02-mongodb.yaml
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
---
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
          image: mongo:7
          ports:
            - containerPort: 27017
          args: ["--bind_ip_all"]
          volumeMounts:
            - name: mongo-data
              mountPath: /data/db
  volumeClaimTemplates:
    - metadata:
        name: mongo-data
      spec:
        accessModes: ["ReadWriteOnce"]
        resources:
          requests:
            storage: 1Gi
```

**that’s all you need for mongo** (no extra `mongodb` ClusterIP service).

---

## build and push the app image

```bash
docker build -t aharonsegal/mongo-container:latest .
docker push aharonsegal/mongo-container:latest
```

---

## openshift commands

```bash
# login with your existing oc login command

oc new-project mongo-api || oc project mongo-api

oc apply -f k8s/
oc delete -f k8s/

oc get pods
oc get svc
oc get statefulset
oc get route

oc logs deploy/mongo-api-deployment
oc logs statefulset/mongodb
```

If your mongodb pod stays in `pending`, it usually means **no default storage class** for the pvc; tell me the output of `oc get pvc` and i’ll give the minimal fix.