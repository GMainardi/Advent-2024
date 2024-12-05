def is_safe(report):
    MIN = 1
    MAX = 3
    

    prev = report[0]
    curr = report[1]

    INCRESING = curr - prev > 0

    for prev, curr in zip(report, report[1:]):

        if abs(curr-prev) > MAX or abs(curr-prev) < MIN:
            return False
        
        if INCRESING and curr - prev < 0:
            return False
        
        elif not INCRESING and curr - prev > 0:
            return False
        
    return True

reports = [list(map(int, line.strip().split(' '))) for line in open('day02/input.txt', 'r').readlines()]

safe_reports = list(filter(is_safe, reports))

print(len(safe_reports))