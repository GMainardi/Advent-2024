def build_xmas(cross_words: list[str], start:complex, direction: complex) -> str:
    
    if not (0 <= start.real + 3 * direction.real < len(cross_words) and 0 <= start.imag + 3 * direction.imag < len(cross_words[0])):
        return ''
    
    return ''.join(
            cross_words[int(start.real + i * direction.real)][int(start.imag + i * direction.imag)] 
            for i in range(4)
        )

def search_xmas(cross_words: list[str], direction: complex):

    XMAS = 'XMAS'
    xmas_count = 0
    for y in range(len(cross_words)):
        for x in range(len(cross_words[y])):
            if cross_words[y][x] == 'X':
                if build_xmas(cross_words, complex(y, x), direction) == XMAS:
                    xmas_count += 1
    return xmas_count


DIRECTIONS = [
    0-1j,
    0+1j,
    1+0j,
    -1+0j,
    1-1j,
    1+1j,
    -1+1j,
    -1-1j
]

cross_words = [line.strip() for line in open('day04/input.txt', 'r').readlines()]
total_xmas = 0
for direction in DIRECTIONS:
    total_xmas += search_xmas(cross_words, direction)

print(total_xmas)
