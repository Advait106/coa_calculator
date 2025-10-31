# calculator.py
def strip_leading_zeros(num):
    num = num.lstrip('0')
    return num if num != '' else '0'

def compare(num1, num2):
    num1, num2 = strip_leading_zeros(num1), strip_leading_zeros(num2)
    if len(num1) > len(num2): return 1
    if len(num1) < len(num2): return -1
    if num1 > num2: return 1
    if num1 < num2: return -1
    return 0

def add_strings(a, b):
    a, b = a[::-1], b[::-1]
    carry, res = 0, []
    for i in range(max(len(a), len(b))):
        d1 = int(a[i]) if i < len(a) else 0
        d2 = int(b[i]) if i < len(b) else 0
        s = d1 + d2 + carry
        res.append(str(s % 10))
        carry = s // 10
    if carry:
        res.append(str(carry))
    return ''.join(res[::-1])

def subtract_strings(a, b):
    a, b = a[::-1], b[::-1]
    res, borrow = [], 0
    for i in range(len(a)):
        d1 = int(a[i])
        d2 = int(b[i]) if i < len(b) else 0
        d1 -= borrow
        if d1 < d2:
            d1 += 10
            borrow = 1
        else:
            borrow = 0
        res.append(str(d1 - d2))
    return strip_leading_zeros(''.join(res[::-1]))

def multiply_strings(a, b):
    a, b = a[::-1], b[::-1]
    result = [0] * (len(a) + len(b))
    for i in range(len(a)):
        for j in range(len(b)):
            result[i + j] += int(a[i]) * int(b[j])
            if result[i + j] >= 10:
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return ''.join(map(str, result[::-1]))

def divide_strings(a, b, precision=20):
    if b == '0':
        return "Error: Division by zero"
    from decimal import Decimal, getcontext
    getcontext().prec = precision
    return str(Decimal(a) / Decimal(b))
