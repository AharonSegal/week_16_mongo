INGW64 ~/שולחן העבודה/week_16/week_16_mongo (aharon/k8s)
$ oc get pods
oc get svc
oc get statefulset
oc get route

oc logs deploy/mongo-api-deployment
oc logs statefulset/mongodb
NAME                                         READY   STATUS             RESTARTS      AGE
mongo-api-deployment-57ccd8bdf9-bwx22        0/1     Error              2 (24s ago)   31s
mongodb-0                                    0/1     ImagePullBackOff   0             29s
workspace53f5117cf7f34596-6b76645f78-4ssnp   2/2     Running            0             32m
NAME                                TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)                               AGE
modelmesh-serving                   ClusterIP   None            <none>        8033/TCP,8008/TCP,8443/TCP,2112/TCP   13d 
mongo-api-service                   ClusterIP   172.30.50.25    <none>        8000/TCP                              32s 
mongodb-headless                    ClusterIP   None            <none>        27017/TCP                             31s 
mysql-service                       ClusterIP   None            <none>        3306/TCP                              6d23h
sqlbasic-api-service                ClusterIP   172.30.56.238   <none>        8000/TCP                              6d23h
workspace53f5117cf7f34596-service   ClusterIP   172.30.95.59    <none>        4444/TCP                              32m 
NAME      READY   AGE
mongodb   0/1     32s
mysql     0/0     6d23h
NAME                   HOST/PORT                                                                  PATH   SERVICES               PORT   TERMINATION   WILDCARD
mongo-api              mongo-api-aharon-segal-dev.apps.rm2.thpm.p1.openshiftapps.com                     mongo-api-service      http                 None
sqlbasic-api-service   sqlbasic-api-service-aharon-segal-dev.apps.rm2.thpm.p1.openshiftapps.com          sqlbasic-api-service   8000                 None
Traceback (most recent call last):
  File "/usr/local/bin/uvicorn", line 8, in <module>
    sys.exit(main())
             ^^^^^^
  File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1485, in __call__
    return self.main(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1406, in main
    rv = self.invoke(ctx)
         ^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1269, in invoke
    return ctx.invoke(self.callback, **ctx.params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/click/core.py", line 824, in invoke
    return callback(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 424, in main
    run(
  File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 594, in run
    server.run()
  File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 67, in run
    return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/uvicorn/_compat.py", line 30, in asyncio_run
    return runner.run(main)
           ^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
    return self._loop.run_until_complete(task)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/asyncio/base_events.py", line 654, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 71, in serve
    await self._serve(sockets)
  File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 78, in _serve
    config.load()
  File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 439, in load
    self.loaded_app = import_from_string(self.app)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 22, in import_from_string
    raise exc from None
  File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1147, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 940, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/app/app/main.py", line 2, in <module>
    from routs import router
ModuleNotFoundError: No module named 'routs'
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1147, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 940, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/app/app/main.py", line 2, in <module>
    from routs import router
ModuleNotFoundError: No module named 'routs'
  File "/usr/local/lib/python3.11/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1147, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 940, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/app/app/main.py", line 2, in <module>
    from routs import router
ModuleNotFoundError: No module named 'routs'
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1147, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 940, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/app/app/main.py", line 2, in <module>
    from routs import router
ModuleNotFoundError: No module named 'routs'
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1147, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 940, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/app/app/main.py", line 2, in <module>
    from routs import router
ModuleNotFoundError: No module named 'routs'
  File "<frozen importlib._bootstrap_external>", line 940, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/app/app/main.py", line 2, in <module>
    from routs import router
ModuleNotFoundError: No module named 'routs'
ModuleNotFoundError: No module named 'routs'
Error from server (BadRequest): container "mongodb" in pod "mongodb-0" is waiting to start: image can't be pulled       
(venv)
a0527@Aharon MINGW64 ~/שולחן העבודה/week_16/week_16_mongo (aharon/k8s)
$



1 - fix the imports 

a0527@Aharon MINGW64 ~/שולחן העבודה/week_16/week_16_mongo (aharon/k8s)
$ python -u "c:\Users\a0527\שולחן העבודה\week_16\week_16_mongo\arc\project_overview.py"

================= PROJECT TREE =================

.gitignore
Dockerfile
README.md
app/ [subfolders: 0, files: 6, total files: 6]
    __init__.py
    connection.py
    dal.py
    json_to_mongo.py
    main.py
    routs.py
arc/ [subfolders: 0, files: 3, total files: 3]
    Git_Commands.md
    imports.py
    thinking.md
k8s/ [subfolders: 0, files: 5, total files: 5]
    app-deployment.yaml
    app-route.yaml
    app-service.yaml
    mongo-service.yaml
    mongo-statefulset.yaml
project_dump.md
requirements.txt

================= PROJECT STATS =================

Total folders: 3
Total files  : 19

File types:
  .md    ->    4 files,    847 lines
  .py    ->    7 files,    264 lines
  .txt   ->    1 files,     20 lines
  .yaml  ->    5 files,     86 lines
  no_ext ->    2 files,    226 lines
(venv)
a0527@Aharon MINGW64 ~/שולחן העבודה/week_16/week_16_mongo (aharon/k8s)
$


then implement in the code to use the import jason 


import json
from pymongo import MongoClient
from os import getenv


mongo_uri = getenv("MONGO_URI", "mongodb://mongodb-gerstnir-dev.apps.rm2.thpm.p1.openshiftapps.com:27017/")
mongo_db = getenv("MONGO_DB", "testdb")
mongo_collection = getenv("MONGO_COLLECTION", "testcollection")
file_path = 'employee_data_advanced.json'

# Making Connection
myclient = MongoClient(mongo_uri)

# database
db = myclient[mongo_db]

# Created or Switched to collection
# names: GeeksForGeeks
Collection = db[mongo_collection]

# Loading or Opening the json file
with open(file_path) as file:
    file_data = json.load(file)

# Inserting the loaded data in the Collection
ins_result = Collection.insert_many(file_data)
print(f"Data inserted to MongoDB. Documents inserted: {len(ins_result.inserted_ids)}")


























