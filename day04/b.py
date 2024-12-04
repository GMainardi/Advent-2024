UP_LEFT = complex(-1, -1)
UP_RIGHT = complex(-1, 1)
DOWN_LEFT = complex(1, -1)
DOWN_RIGHT = complex(1, 1)


def get_xmas_patterns() -> list[str]:

    possibilities = [
        '1122',
        '1212'
    ]

    return [*list(map(lambda x: x.replace('1', 'M').replace('2', 'S'), possibilities)), *list(map(lambda x: x.replace('1', 'S').replace('2', 'M'), possibilities))]

def is_xmas(cross_words: list[str], start:complex) -> str:
    
    DIRECTIONS = [
        UP_LEFT,
        UP_RIGHT,
        DOWN_LEFT,
        DOWN_RIGHT
    ]

    xmas = ''
    for direction in DIRECTIONS:

        char_pos = start + direction

        if not (0 <= char_pos.real < len(cross_words) and 0 <= char_pos.imag < len(cross_words[0])):
            return False
        
        xmas += cross_words[int(char_pos.real)][int(char_pos.imag)]

    return xmas in get_xmas_patterns()

    
def search_xmas(cross_words: list[str]):
    xmas_count = 0
    for y in range(len(cross_words)):
        for x in range(len(cross_words[y])):
            if cross_words[y][x] == 'A':
                xmas_count += is_xmas(cross_words, complex(y, x))
    return xmas_count


cross_words = [line.strip() for line in open('day04/input.txt', 'r').readlines()]

print(search_xmas(cross_words))