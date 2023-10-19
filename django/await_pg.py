#!/usr/bin/env python
"""Module to wait for Postgres to come up."""

import os
import sys
import time

import psycopg

MAX_RETRIES = 12
RETRY_DELAY = 10

username = os.environ.get("POSTGRES_USER")
password = os.environ.get("POSTGRES_PASSWORD")
host = os.environ.get("POSTGRES_HOST")
db_name = os.environ.get("POSTGRES_DB")

print("Waiting for postgres server", end="")

for _ in range(MAX_RETRIES):
    print(".", end="")
    try:
        con = psycopg.connect(dbname=db_name, user=username, password=password, host=host)
        print("connected!")
        sys.exit(0)
    except psycopg.Error:
        time.sleep(RETRY_DELAY)

print(f"Error: could not connect to server after {MAX_RETRIES} tries.")
sys.exit(1)
