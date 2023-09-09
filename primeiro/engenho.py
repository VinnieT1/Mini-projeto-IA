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

# def set_facts(propositions: dict[str, bool]) -> None:
#     script_dir = os.path.dirname(os.path.abspath(__file__))
#     file_path = os.path.join(script_dir, 'facts.json')

#     with open(file_path) as file:
#         facts = json.load(file)['facts']
    
#     for fact in facts:
#         propositions[fact] = True

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

def evaluate_condition(conditions: list[str], propositions: dict[str, bool]) -> bool:
    condition_values = conditions.copy()
    for idx, condition in enumerate(condition_values):
        if 'nao' in condition and condition.removeprefix('nao ') in propositions:
                propositions[condition] = not propositions[condition.removeprefix('nao ')]

        if 'nao' not in condition and ('nao ' + condition) in propositions and propositions[condition]:
            propositions['nao ' + condition] = False

        condition_values[idx] = propositions[condition]

    return False not in condition_values

def natural_and(and_conditions: list[str]) -> None:
    res = ""

    for condition in and_conditions:
        res += condition + " e "

    return res[:-3]

def forwards(propositions: dict[str, bool], conditions: dict[str, list[list[str]]]) -> None:
    conclusions = list(conditions.keys())
    conclusions_len = len(conclusions)
    i = 0 # index iterating over each conclusion

    while i < conclusions_len:
        if propositions[conclusions[i]]:    # if the conclusion is already True, continue to next one
            i += 1                          # else, check if now can be set to True
            continue                                    

        conclusion = conclusions[i] # conclusion we're evaluating

        for condition in conditions[conclusion]:
            evaluated_condition = evaluate_condition(condition, propositions)
            if evaluated_condition:
                propositions[conclusion] = True
                i = -1

        i += 1

def backwards(propositions: dict[str, bool], conditions: dict[str, list[list[str]]]) -> None:
    idx = 1
    for conclusion in conditions:
        if propositions[conclusion]:
            is_fact = True
            for and_conditions in conditions[conclusion]:
                if evaluate_condition(and_conditions, propositions):
                    print(f'{idx}. {conclusion} porque {natural_and(and_conditions)}')
                    is_fact = False
                    idx = idx + 1
                    break
            
            if is_fact:
                print(conclusion, "é fato")

def get_final_conclusions(file_name: str) -> list[str]:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)

    with open(file_path) as file:
        final_conclusions = json.load(file)['final']

    return final_conclusions

def is_worth_asking(proposition: str, propositions: dict[str, bool], conditions: dict[str, list[list[str]]]) -> bool:
    for condition in conditions:
        or_conditions = conditions[condition]

        for and_conditions in or_conditions:
            if proposition in and_conditions and not propositions[condition]:
                return True
        
    return False

def questions(propositions: dict[str, bool], conditions: dict[str, list[list[str]]], final_conclusions: list[str]):
    propositions_for_question = [x for x in propositions if x not in conditions]

    for proposition in propositions_for_question:
        if 'nao' in proposition.split(' '):
            continue

        if not is_worth_asking(proposition, propositions, conditions):
            continue

        ans = str(input(f"seu animal {proposition}? (s/n): "))
        
        while ans not in ["s", "n"]:
            print('Input invalido (s/n)')
            ans = str(input(f"seu animal {proposition}? (s/n): "))
        
        propositions[proposition] = (ans == 's')
         
        forwards(propositions, conditions)
        #checa se alguma final ta true
        for final_conclusion in final_conclusions:
            if propositions[final_conclusion]:
                print(f'\nSeu animal: {final_conclusion.upper()}!\n')
                print("Justificativa:")
                backwards(propositions, conditions)
                return

if __name__ == '__main__':
    rules = extract_rules_from_file('rules.json') # rules.json as default
    propositions = get_propositions(rules)
    conditions = get_conditions(rules)
    final_conclusions = get_final_conclusions('final.json') # rules.json as default

    # Each key is a conclusion of the specified rules, and its value is a list of lists.
    # Each inner list is a list of propositions that, if all are True, than the conclusion is True.
    # That means that, if at least one list of the inner lists evaluates to True, than the
    # conclusion is True. Otherwise, it's False.
    
    questions(propositions, conditions, final_conclusions)
