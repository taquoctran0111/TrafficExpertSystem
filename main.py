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
