import json, os

def extract_rules_from_file(file_name: str) -> list[str]:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)
    with open(file_path) as file:
        return json.load(file)['rules']

def get_propositions(rules: list[str]) -> dict[str, bool]:
    propositions = {}

    for rule in rules:
        composite_condition, conclusion = tuple(rule.split(' entao '))
        composite_condition = composite_condition[3:] # 3 because it's len('se ')
        and_conditions = composite_condition.split(' e ')

        for condition in and_conditions:
            if condition not in propositions:
                propositions[condition] = False

        if conclusion not in propositions:
            propositions[conclusion] = False

    return propositions

def set_facts(propositions: dict[str, bool]) -> None:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'facts.json')

    with open(file_path) as file:
        facts = json.load(file)['facts']
    
    for fact in facts:
        propositions[fact] = True

def get_conditions(rules: list[str]) -> dict[str, list]:
    conditions: dict[str, list] = {}

    for rule in rules:
        composite_condition, conclusion = tuple(rule.split(' entao '))
        composite_condition = composite_condition[3:] # 3 because it's len('se ')
        and_conditions = composite_condition.split(' e ')

        if conclusion not in conditions:
            conditions[conclusion] = []
    
        conditions[conclusion].append(and_conditions)

    return conditions

def evaluate_condition(conditions: list[str], propositions: dict[str, bool], conclusion: str) -> bool:
    condition_values = conditions.copy()
    for idx, condition in enumerate(condition_values):
        condition_values[idx] = propositions[condition]

    return False not in condition_values

def infere(rules: list[str], propositions: dict[str, bool], conditions: dict[str, list[list[str]]]):
    conclusions = list(conditions.keys())
    print('conclusions are', conclusions)
    conclusions_len = len(conclusions)
    i = 0 # index iterating over each conclusion

    while i < conclusions_len:
        if propositions[conclusions[i]]:    # if the conclusion is already True, continue to next one
            i += 1                          # else, check if now can be set to True
            continue                                    

        conclusion = conclusions[i] # conclusion we're evaluating

        for condition in conditions[conclusion]:
            evaluated_condition = evaluate_condition(condition, propositions, conclusion)
            if evaluated_condition:
                propositions[conclusion] = True
                i = -1

        i += 1
            
if __name__ == '__main__':
    rules = extract_rules_from_file('rules.json') # rules.json as default
    propositions = get_propositions(rules)
    conditions = get_conditions(rules)
    set_facts(propositions)

    # Each key is a conclusion of the specified rules, and its value is a list of lists.
    # Each inner list is a list of propositions that, if all are True, than the conclusion is True.
    # That means that, if at least one list of the inner lists evaluates to True, than the
    # conclusion is True. Otherwise, it's False.

    print('rules =', rules)
    print('propositions initially =', propositions)
    print('conditions =', conditions)
    
    infere(rules, propositions, conditions)

    print('propositions after inference =', propositions)