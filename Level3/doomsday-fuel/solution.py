import math
from fractions import Fraction

maps = {}

def transposeMatrix(m):
    return map(list,zip(*m))

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors

def find_absorption_state(matrix):
    for state in range(len(matrix)):
        if sum(matrix[state]) == 0:
            maps.update({state : 0})
        else:
            maps.update({state : 1})

def find_RQ_matrix(matrix):
    r_matrix = []
    q_matrix = []
    for state in range(len(matrix)):
        if maps.get(state) == 1:
            denominator = sum(matrix[state]) 
            r_matrix.append([])
            q_matrix.append([])
            for col_state in range(len(matrix[state])):
                if maps.get(col_state) == 0:
                    r_matrix[-1].append(matrix[state][col_state]/denominator)
                else:
                    q_matrix[-1].append(matrix[state][col_state]/denominator)

    return r_matrix, q_matrix

def find_i_matrix(dimension):
    i_matrix = [[0 for _ in range(dimension)] for _ in range(dimension)]
    for index in range(dimension):
        i_matrix[index][index] = 1
    return i_matrix

def find_f_matrix(i_matrix, q_matrix):
    diff_matrix = []
    for row in range(len(i_matrix)):
        diff_matrix.append([])
        for col in range(len(i_matrix[row])):
            diff_matrix[-1].append(i_matrix[row][col] - q_matrix[row][col])
    return getMatrixInverse(diff_matrix)

def multiply_matrix(f_matrix, r_matrix):
    fr_matrix = [[0 for _ in range(len(r_matrix[0]))] for _ in range(len(f_matrix))]
    for row in range(len(fr_matrix)):
        for col in range(len(fr_matrix[0])):
            for n in range(len(r_matrix)):
                fr_matrix[row][col] += f_matrix[row][n] * r_matrix[n][col]
    return fr_matrix

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def find_lcm(arr):
    lcm_result = 1
    for num in arr:
        int_num = int(num * (10 ** 10)) // (10 ** 10)
        lcm_result = lcm(lcm_result, int_num)
    return lcm_result

def solution(m):
    find_absorption_state(m)
    r_matrix, q_matrix = find_RQ_matrix(m)
    i_matrix = find_i_matrix(len(q_matrix))
    f_matrix = find_f_matrix(i_matrix, q_matrix)
    fr_matrix = multiply_matrix(f_matrix, r_matrix)
    fraction_nums = [Fraction(num).limit_denominator() for num in fr_matrix[0]]
    denominators = []
    for f in fraction_nums:
        denominators.append(int(f.denominator))
    lcm = find_lcm(denominators)
    for i in range(len(fr_matrix[0])):
        fr_matrix[0][i] = math.ceil(lcm * fr_matrix[0][i])
    fr_matrix[0].append(lcm)
    return fr_matrix[0]


print(solution(
    [
        [0, 1, 0, 0, 0, 1],
        [4, 0, 0, 3, 2, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
))

print(solution(
    [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]
))