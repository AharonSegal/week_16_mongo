from os import getenv

import requests
from fastapi import APIRouter

router = APIRouter()

test_app_url = getenv("test_app_URL", "http://localhost:8000")

def forward_get(path):
    url = test_app_url.rstrip("/") + path
    print("THE URL , "  , {url})
    response = requests.get(url)
    return response.json()


@router.get("/employees/engineering/high-salary")
def employees_engineering_high_salary():
    print("STARTING HIGHT SALARY======")
    return forward_get("/employees/engineering/high-salary")


@router.get("/employees/by-age-and-role")
def employees_by_age_and_role():
    return forward_get("/employees/by-age-and-role")


@router.get("/employees/top-seniority")
def employees_top_seniority():
    return forward_get("/employees/top-seniority")


@router.get("/employees/age-or-seniority")
def employees_age_or_seniority():
    return forward_get("/employees/age-or-seniority")


@router.get("/employees/managers/excluding-departments")
def employees_managers_excluding_departments():
    return forward_get("/employees/managers/excluding-departments")


@router.get("/employees/by-lastname-and-age")
def employees_by_lastname_and_age():
    return forward_get("/employees/by-lastname-and-age")