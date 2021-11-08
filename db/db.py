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

def get_rules():
    rules = []
    rules_rs = col_rules.find()
    for rule in rules_rs:
        rules.append(rule)
    return rules

def get_one_rule(name_rule):
    rule = col_rules.find_one({"IF": name_rule})
    return rule
    
def get_cases():
    cases = []
    cases_rs = col_cases.find()
    for case in cases_rs:
        cases.append(case)
    return cases

def json_data(rule,max_sp,min_sp, advice):
    data = {
        'IF': rule,
        'THEN': {'Max': max_sp, 'Min': min_sp, 'Advice': advice}
    }
    return data

def add_rule(data):
    col_rules.insert_one(data)

def delete_rule(name_rule):
    col_rules.delete_one({"IF": name_rule})

def update_rule(name_rule, max_sp, min_sp, advice):
    col_rules.update_one(
        {"IF": name_rule},
        {
            "$set": {"THEN.Max": max_sp, "THEN.Min": min_sp, "THEN.Advice": advice}
        }
    )
