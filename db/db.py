import pymongo
from pymongo import MongoClient
import json

client = MongoClient("mongodb://localhost:27017/")

db = client["db_traffic_highway"]
col_rules = db["rules"]
col_cases = db["cases"]

def import_rules():
    rule_file = 'rules/rules.json'
    with open(rule_file, 'r') as f:
        rules = json.load(f)
        return rules

def import_cases():
    cases_file = 'cases/tests.json'
    with open(cases_file, 'r') as f:
        cases = json.load(f)
        return cases

rules = import_rules()
cases = import_cases()

# col_rules.insert_many(rules)
# col_cases.insert_many(cases)

def get_rules():
    rules = []
    rules_rs = col_rules.find()
    for rule in rules_rs:
        rules.append(rule)
    return rules
    
def get_cases():
    cases = []
    cases_rs = col_cases.find()
    for case in cases_rs:
        cases.append(case)
    return cases