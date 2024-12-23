def mix(value, secret_number):
    return value ^ secret_number


def prune(secret_number):
    return secret_number % 16777216


def next_secret_number(secret_number):
    first = prune(mix(secret_number * 64, secret_number))
    second = prune(mix(first // 32, first))
    third = prune(mix(second * 2048, second))

    return third


def get_price(value):
    return int(str(value)[-1])


def apply_secret_number(value, times):
    prices = [get_price(value)]
    for _ in range(times):
        value = next_secret_number(value)
        prices.append(get_price(value))
    return prices


def get_price_sequencies(prices):
    changes = [curr - prev for prev, curr in zip(prices[:-1], prices[1:])]
    it = 4
    price_change_sequencies = {}
    for price_change_seq in zip(changes[:-3], changes[1:-2], changes[2:-1],
                                changes[3:]):
        if price_change_seq not in price_change_sequencies:
            price_change_sequencies[price_change_seq] = prices[it]
        it += 1
    return price_change_sequencies


def merge_price_seqs(price_seq1, price_seq2):
    new_price_seq = price_seq1.copy()
    for seq, price in price_seq2.items():
        new_price_seq[seq] = new_price_seq.get(seq, 0) + price
    return new_price_seq


def get_best_seq(price_change_sequencies):
    return max(price_change_sequencies.items(), key=lambda x: x[1])


buyer_numbers = list(map(int, open('day22/input.txt', 'r').split('\n')))

price_change_sequencies = {}
for buyer_number in buyer_numbers:
    prices = apply_secret_number(buyer_number, 2000)
    price_change_sequencies = merge_price_seqs(price_change_sequencies,
                                               get_price_sequencies(prices))

print(get_best_seq(price_change_sequencies))