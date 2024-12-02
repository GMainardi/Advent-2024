def is_level_safe(prev, curr, INCRESING):
    MIN = 1
    MAX = 3

    if abs(curr-prev) > MAX or abs(curr-prev) < MIN:
        return False
    
    if INCRESING and curr - prev < 0:
        return False
    elif not INCRESING and curr - prev > 0:
        return False
    
    return True

def is_report_safe(report):
    INCRESING = report[1] - report[0] > 0

    for prev, curr in zip(report, report[1:]):

        if not is_level_safe(prev, curr, INCRESING):
            return False
        
    return True

def is_safe_plus(report):
    
    for i in range(len(report)):
        if is_report_safe(report[:i] + report[i+1:]):
            return True
        
    return is_report_safe(report)
reports = [list(map(int, line.strip().split(' '))) for line in open('day02/input.txt', 'r').readlines()]

safe_reports = list(filter(is_safe_plus, reports))

print(len(safe_reports))