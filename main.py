import json 

def import_rules():
    rule_file = 'rules/rules.json'
    with open(rule_file, 'r') as f:
        rules = json.load(f)
        return rules

def import_facts():
    facts = {'Freeway', 'Three lanes',
             'Middle lane', 'Safety distance 100 meters'}
    return facts

def import_cases():
    cases_file = 'cases/tests.json'
    with open(cases_file, 'r') as f:
        cases = json.load(f)
        return cases

def match_rule(facts, rule):
    for condition in rule['IF']:
        if (condition not in facts):
            return False
    return True

