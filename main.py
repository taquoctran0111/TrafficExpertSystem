import json
from db import db

def import_facts():
    facts = {'Freeway', 'Three lanes',
             'Middle lane', 'Safety distance 100 meters'}
    return facts


def match_rule(facts, rule):
    for condition in rule['IF']:
        if (condition not in facts):
            return False
    return True


def test_one_case(rules, facts):
    print('The facts are: ')
    print(facts)

    Max = 120
    Min = 0
    Advice = set()
    for rule in rules:
        if (match_rule(facts, rule)):
            print('Match rule: ' + str(rule['IF']) + str(rule['THEN']))
            conclusions = rule['THEN']
            if 'Max' in conclusions.keys():
                Max = min(Max, conclusions['Max'])
            if 'Min' in conclusions.keys():
                Min = max(Min, conclusions['Min'])
            if Max <= Min:
                Min = 0
            if 'Advice' in conclusions.keys():
                Advice = Advice | set(conclusions['Advice'])
    return Max, Min, Advice

if __name__ == "__main__":
    rules = db.get_rules()
    facts = import_facts()
    test_one_case(rules, facts)

    cases = db.get_cases()
    for case in cases:
        facts = case['Facts']
        conclusion = case['Conclusion']
        Max, Min, Advice = test_one_case(rules, facts)
        print('Max speed: ' + str(Max))
        print('Min speed: ' + str(Min))
        if len(Advice) > 0:
            print('Advice: ' + str(Advice))
        print()
