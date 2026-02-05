# PROJECT TREE

```
arc/ [subfolders: 0, files: 3, total files: 3]
    Git_Commands.md
    imports.py
    thinking.md
```

# PROJECT STATS

- Total folders: 1
- Total files  : 3

## File types

| Extension | Files | Lines (utf-8 text only) |
|---|---:|---:|
| `.md` | 2 | 291 |
| `.py` | 1 | 128 |

---

# FILE CONTENTS

## arc/Git_Commands.md

```markdown
# ╔══════════════════════════════════════════════════════╗
# ║   GIT BASH ENVIRONMENT SETUP (WINDOWS)               ║
# ╚══════════════════════════════════════════════════════╝

git clone <url>                 # Clone from remote

git init
python -m venv venv
source venv/Scripts/activate
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
pip freeze > requirements.txt
git add .  
git commit -m "initial commit"
git push -u origin main

pip install fastapi uvicorn[standard]

# ╔══════════════════════════════════════════════════════╗
# ║   BASIC GIT COMMANDS                                 ║
# ╚══════════════════════════════════════════════════════╝
"""
git add .                    
git commit -m "dev merge"      
git push                     

uvicorn main:app --reload
uvicorn app.main:app --reload

# ╔══════════════════════════════════════════════════════╗
# ║   GIT BRANCH WORKFLOW                                ║
# ╚══════════════════════════════════════════════════════╝
"""
# Check current branch
git branch

# Create a new branch
git checkout -b aharon/k8s
git checkout main

# Stage changes
git add .

# Commit changes
git commit -m "Descriptive commit message"

# Push branch to remote
git push -u origin title/branch_purpose
git push -u origin aharon/server-b

# Switch between branches
git checkout main
git checkout title/branch_purpose

# Merge branch into main
git checkout main
git pull                  # ensure main is up-to-date
git merge aharon/dev

# Delete branch (optional)
git branch -d title/branch_purpose        # local
git push origin --delete title/branch_purpose  # remote

# Useful commands
git status                      # View changes
git log --oneline               # Condensed history
git remote -v                   # Show remote URL
"""
# ╔══════════════════════════════════════════════════════╗
# ║   TEAM WORKFLOW – REMOTE BRANCHES                    ║
# ╚══════════════════════════════════════════════════════╝

# Fetch latest data from remote (does NOT change your code)
git fetch origin

# View all remote branches
git branch -r

# View both local + remote branches
git branch -a

# View remote branches with last commit info
git branch -r -v

# ------------------------------------------------------

# Check out a teammate’s remote branch locally
git checkout -b feature/login origin/feature/login

# (Shortcut – Git creates the local branch automatically)
git checkout feature/login
git checkout feature/create-basic-files

# ------------------------------------------------------

# Pull latest changes for your current branch
git pull

# Pull a specific remote branch into your current branch
git pull origin feature/login

# ------------------------------------------------------

# Review changes BEFORE merging
git log origin/feature/login --oneline
git diff main..origin/feature/login

# ------------------------------------------------------

# Merge teammate’s branch into your branch
git merge origin/feature/login

# ------------------------------------------------------

# Standard merge flow into main
git checkout main
git pull origin main
git merge feature/login

# Resolve conflicts if needed
git status
# edit files → fix conflicts
git add .
git commit

# ------------------------------------------------------

# Push updated main to remote
git push origin main

# ------------------------------------------------------

# Clean up branches after merge
git branch -d feature/login                # delete local
git push origin --delete feature/login     # delete remote

# ------------------------------------------------------

# Useful team commands
git show origin/feature/login              # inspect last commit
git log --graph --oneline --all            # visualize branch graph
git blame file.py                          # see who changed what

# ╔══════════════════════════════════════════════════════╗
# ║   GIT: GO BACK TO OLD VERSIONS & PUSH TO GITHUB      ║
# ╚══════════════════════════════════════════════════════╝
"""
# Save current work
git status
git add .
git commit -m "Current working version"

# View commit history
git log --oneline

## ✅ Option A — Revert (Keep History, Create New Commit)
git revert <old_commit_hash>..HEAD
# Example:
git revert 8a61c0c8360841b8ef1a5f47f41854adc48f12d3..HEAD
git push

# Abort if stuck
git revert --abort

## 🔴 Option B — Reset (Full Move Back, No Conflicts)
git reset --hard <old_commit_hash>
git push --force

## Push project to GitHub
git init
git remote add origin https://github.com/AharonSegal/..
git add .
git commit -m "Initial Push"
git branch -M main          # Rename master → main
git push -u origin main

# If push fails due to remote changes
git pull origin main --rebase
git push -u origin main


# ╔══════════════════════════════════════════════════════╗
# ║   GIT LOGGING & VIEWING HISTORY                       ║
# ╚══════════════════════════════════════════════════════╝
"""
# View current branch status
git status

# View full commit history
git log

# View condensed history (one line per commit)
git log --oneline

# Show commits with graph
git log --oneline --graph --decorate --all

# View last N commits
git log -n 5

# View changes in a commit
git show <commit-hash>

# View differences in working directory
git diff

# View staged changes
git diff --cached

# Show remote repositories
git remote -v

# View detailed commit history for a file
git log -- <file-path>
"""
```

## arc/imports.py

```python
"""
pip install fastapi
pip install pydantic
pip install 'pydantic[email]'
pip install SQLAlchemy
pip install sqlmodel
pip install uvicorn
pip install requests
pip install python-dotenv
pip install numpy pandas
pip install matplotlib
pip install seaborn
pip install termseparator
pip install pymongo
"""

# ---------------------------------------
#  Standard Library (built into Python)
# ---------------------------------------

import os
import sys
import json
import datetime
import pathlib
import logging

# Extra commonly used imports
from pathlib import Path                # Object-oriented filesystem paths
from logging import getLogger           # Quick logger access
from datetime import timedelta, date     # Useful time objects


# ---------------------------------------
#  Databases
# ---------------------------------------

import sqlite3
import sqlalchemy
import sqlmodel
from pymongo import MongoClient


# Common SQLAlchemy imports
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    ForeignKey,
    select,
)

from sqlalchemy.orm import (
    Session,
    declarative_base,
    relationship,
)

# SQLModel essentials
from sqlmodel import (
    SQLModel,
    Field,
    Session as SQLSession,
    create_engine,
)


# ---------------------------------------
#  Web & APIs
# ---------------------------------------

import requests
from fastapi import FastAPI

# Common requests helpers
from requests import Session as RequestSession

# Typical FastAPI imports
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)

# ---------------------------------------
#  Pydantic & Validation
# ---------------------------------------

from pydantic import BaseModel, Field, EmailStr, HttpUrl, ValidationError
from typing import Optional, List, Dict
from datetime import datetime

# ---------------------------------------
#  Environment & Configuration
# ---------------------------------------

from dotenv import load_dotenv
import configparser

# Typical configparser helpers
from configparser import ConfigParser

# ---------------------------------------
#  Data Analysis & Numerical Computing
# ---------------------------------------
import numpy as np        # Powerful numerical computations
import pandas as pd       # Data manipulation and analysis
import matplotlib.pyplot as plt # Plotting and visualization 
import seaborn as sns     # Statistical data visualization

# ---------------------------------------
#  Utilities
# ---------------------------------------

import functools
import itertools
import random
import termseparator as ts       # terminal separator for clear output

# Convenient direct imports
from functools import lru_cache, partial
from itertools import groupby, chain
from random import randint, choice

```

## arc/thinking.md

```markdown
apiVersion: apps/v1
kind: Deployment
metadata:
  name: test-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: test-app
  template:
    metadata:
      labels:
        app: test-app
    spec:
      containers:
        - name: test-app
          image: test-app:latest
          imagePullPolicy: IfNotPresent
          ports:
            - containerPort: 8002
          env:
            - name: MONGO_URI
              value: mongodb://mongodb:27017/
            - name: MONGO_DB
              value: testdb
            - name: MONGO_COLLECTION
              value: testcollection
---
apiVersion: v1
kind: Service
metadata:
  name: test-app
spec:
  selector:
    app: test-app
  ports:
    - name: http
      port: 8002
      targetPort: 8002


      apiVersion: apps/v1
kind: Deployment
metadata:
  name: mongodb
spec:
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
---
apiVersion: v1
kind: Service
metadata:
  name: mongodb
spec:
  selector:
    app: mongodb
  ports:
    - name: mongo
      port: 27017
      targetPort: 27017


remake all the code and files then give comaands to build and push docker image and all i need to run openshift 
```

