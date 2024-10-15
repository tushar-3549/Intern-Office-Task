# Compare Two JSON File (Rupantor)
# At updated file update/insert some areas that is check(which area insert at updated file)

import json
import os
import sys

temp_path = os.getcwd()
os.chdir('../Address_Parser')
sys.path.append(os.getcwd())
import DSU_Parser_Main as pu
sys.path.pop()

os.chdir('../Address_Parser_Prev')
sys.path.append(os.getcwd())
import DSU_Parser_Main as pb
os.chdir(temp_path)

def load_json_file(f_path):
    with open(f_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def compare_dicts(old, new, path=''):
    changes = {}

    for key in new.keys():
        new_p = f"{path}.{key}" if path else key
        if key not in old:
            changes[new_p] = {'status': 'added', 'value': new[key]}
        elif isinstance(new[key], dict) and isinstance(old[key], dict):
            nested_changes = compare_dicts(old[key], new[key], new_p)
            if nested_changes: 
                changes.update(nested_changes)
        elif old[key] != new[key]:
            changes[new_p] = {'status': 'changed', 'new_value': new[key]}

    return changes

def main():
    prev = load_json_file('prev.json')
    upd = load_json_file('updated.json')
    
    diff = compare_dicts(prev, upd)
    print(json.dumps(diff, indent=4))
    
    with open('diff_output2.json', 'w', encoding='utf-8') as output:
        json.dump(diff, output, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()
