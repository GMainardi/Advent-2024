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

def check_page(pages_rules, page):
    for page_number1, page_number2 in zip(page, page[1:]):
        if page_number1 in pages_rules.get(page_number2, []):
            return False
    return True

def get_middle_element(page):
    middle_index = len(page) // 2
    return page[middle_index]

def get_free_number(pages_rules, page):

    if not len(page):
        return 0
    
    for page_number in page:
        if not any(page_number in pages_rules[key] for key in page if key in pages_rules):
            return page_number
    return page[0]
    
def sort_page(pages_rules, page):
    sorted_page = []

    while get_free_number(pages_rules, page):
        free_number = get_free_number(pages_rules, page)
        sorted_page.append(free_number)
        page.remove(free_number)
    return sorted_page
    

valid_pages_middle_numbers_sum = 0
for page in pages_produced:
    
    if not check_page(pages_rules, page):
        valid_pages_middle_numbers_sum += get_middle_element(sort_page(pages_rules, page))

print(valid_pages_middle_numbers_sum)