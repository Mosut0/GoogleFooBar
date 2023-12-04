def solution(xs):
    power = 1
    negative_power = 1
    for i in range(len(xs)):
        if xs[i] > 0:
            power *= xs[i]
        elif xs[i] < 0:
            negative_power *= xs[i]
    
    if negative_power > 0:
        power *= negative_power
    else:
        negative_power //= max([number for number in xs if number < 0])
        power *= negative_power
    
    return power

print(solution([2, 0, 2, 2, 0]))
print(solution([-2, -3, 4, -5]))
