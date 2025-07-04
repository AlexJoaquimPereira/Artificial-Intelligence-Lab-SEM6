import itertools
import re

def format_bool(val):
    return 'T' if val else 'F'

def evaluate(expr, val_dict):
    for var, val in val_dict.items():
        expr = re.sub(rf'\b{var}\b', str(val), expr)
    expr = re.sub(r'~~(\w+)', r'\1', expr)
    expr = expr.replace('<->', '==')
    expr = expr.replace('~', ' not ')

    expr = expr.replace('&', ' and ')
    expr = expr.replace('|', ' or ')
    expr = re.sub(r'(\w+)\s*->\s*(\w+)', r'not \1 or \2', expr)
    try:
        return eval(expr)
    except:
        return False
    
def truth_table_full(expr, subparts):
    '''
    Extract variables (using regex to find alphanumeric words)
    '''
    variables = sorted(set(re.findall(r'\b\w+\b', expr)))
    all_exprs = subparts + [expr]
    col_width = 8
    divider = ' | '
    headers = [v.center(col_width) for v in variables]
    logic_headers = [e.center(col_width) for e in all_exprs]
    header_line = divider.join(headers) + " || " + divider.join(logic_headers)
    print(f"\nTruth Table for: {expr}")
    print(header_line)
    print("-" * len(header_line))
    all_results = []
    for combo in itertools.product([False, True], repeat=len(variables)):
        val_dict = dict(zip(variables, combo))
        row = divider.join(format_bool(val_dict[v]).center(col_width) for v in variables)
        results = []
        for part in all_exprs:
            result = evaluate(part, val_dict)
            results.append(result)
    logic_row = divider.join(format_bool(r).center(col_width) for r in results)
    print(row + " || " + logic_row)
    all_results.append(results[-1])
    print("\nFinal Result:")
    if all(r == True for r in all_results):
        print("=> The expression is a TAUTOLOGY (Always TRUE)")
    elif all(r == False for r in all_results):
        print("=> The expression is a CONTRADICTION (Always FALSE)")
    else:
        print("=> The expression is Not Valid (Sometimes TRUE, Sometimes FALSE)")
        

main_expr = input("Enter the main logical expression: ")
num_sub_exprs = int(input("Enter the number of sub-expressions: "))
sub_exprs = [input(f"Enter sub-expression {i+1}: ") for i in range(num_sub_exprs)]
truth_table_full(main_expr, sub_exprs)