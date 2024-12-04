import re
import functools

print( 
    sum(
        map(
            lambda intruct: functools.reduce(
                lambda x, y: x*y, 
                map(
                    int, 
                    re.findall(
                        r'\d{1,3}', 
                        intruct
                    )
                )
            ), 
            re.findall(
                r'mul\(\d{1,3},\d{1,3}\)', 
                ''.join(
                    open(
                        'day03/sinput.txt', 
                        'r'
                    ).readlines()
                )
            )
        )
    )
)