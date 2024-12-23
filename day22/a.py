def mix(value, secret_number):
    return value ^ secret_number

def prune(secret_number):
    return secret_number % 16777216

def next_secret_number(secret_number):
    first = prune(mix(secret_number * 64, secret_number))
    second = prune(mix(first // 32, first))    
    third = prune(mix(second * 2048, second))

    return third
    
def apply_secret_number(value, times):
    for _ in range(times):
        value = next_secret_number(value)
    return value
    
buyer_numbers = list(map(int,open('day22/input.txt', 'r').split('\n')))

total = 0
for buyer_number in buyer_numbers:
    secret_number = apply_secret_number(buyer_number, 2000)
    total += secret_number