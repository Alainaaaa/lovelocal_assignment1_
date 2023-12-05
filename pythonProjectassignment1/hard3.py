#You are given a string s. You can convert s to a


def countDigitOne(n):
    count = 0
    factor = 1
    i = 1

    while i <= n:
        divider = i * 10
        count += (n // divider) * i + min(max(n % divider - i + 1, 0), i)
        i *= 10

    return count

# Take input from the user
n = int(input("n = "))

# Count and print the total number of digit 1
result = countDigitOne(n)
print("Total number of digit 1:", result)

#Algorithm
"""
Initialize Variables:
Set count to 0, factor to 1, and i to 1.
Iterate Through Digits:
While i is less than or equal to n:
Calculate divider as i * 10.
Update count based on the occurrences of digit 1 in the current digit place.
Multiply i by 10 for the next iteration.
Return Result:
The final value of count represents the total number of digit 1 in the range up to n.

Usage:
User inputs an integer n.
The algorithm counts and prints the total occurrences of digit 1.


time complexity of the given code is O(log n).

"""

