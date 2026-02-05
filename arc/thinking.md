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

apiVersion: v1
kind: Service
metadata:
  name: mongodb-headless
spec:
  clusterIP: None
  selector:
    app: mongodb
  ports:
    - name: mongo
      port: 27017
      targetPort: 27017

apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: mongodb
spec:
  serviceName: mongodb-headless
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


these are my yamls 

do i really nee dthe rout yaml
what is it for 

is what i have good?

