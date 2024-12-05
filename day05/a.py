import functools

pages_rules = {}

with open('day05/input.txt', 'r') as file:
    data = file.read().split('\n\n')
    first_part = data[0]
    second_part = data[1]

    pages_rules = {}
    for rule in first_part.split('\n'):
        rule = rule.split('|')
        pages_rules[int(rule[0])] = pages_rules.get(int(rule[0]), []) + [int(rule[1])]

    pages_produced = [list(map(int, page.split(','))) for page in second_part.split('\n')]


valid_pages_middle_numbers_sum = 0
for page in pages_produced:
    
    for page_number1, page_number2 in zip(page, page[1:]):
        if page_number1 in pages_rules.get(page_number2, []):
            break
    else:
        print(page)
        middle_index = len(page) // 2
        middle_number = page[middle_index]
        valid_pages_middle_numbers_sum += middle_number


print(valid_pages_middle_numbers_sum)