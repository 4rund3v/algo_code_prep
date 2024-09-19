"""
A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
"""


def check_happy_number(num: int) -> bool:
    def get_sum_of_squared_digits(_num: int) -> int:
        temp = 0
        res = 0
        while _num > 0:
            temp = _num % 10
            _num = _num // 10
            res = res + temp**2
        return res
    slow = num
    fast = get_sum_of_squared_digits(num)

    while fast != slow and fast != 1:
        slow = get_sum_of_squared_digits(slow)
        fast = get_sum_of_squared_digits(get_sum_of_squared_digits(fast))

    if fast == 1:
        return True
    return False

            

print("19", check_happy_number(19))
print("52", check_happy_number(52))
print("1049", check_happy_number(1049))
