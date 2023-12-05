#Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.


def majorityElement(nums):
    candidate1, candidate2 = float('inf'), float('inf')
    count1, count2 = 0, 0

    # First pass: Find potential candidates
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1 = num
            count1 = 1
        elif count2 == 0:
            candidate2 = num
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1

    # Second pass: Count occurrences of potential candidates
    count1 = count2 = 0
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1

    result = []
    n = len(nums)

    if count1 > n // 3:
        result.append(candidate1)
    if count2 > n // 3:
        result.append(candidate2)

    return result

# Take input from the user as a string and convert it to a list
nums_input = input("nums = ")
nums = [int(num) for num in nums_input.strip("[]").split(',')]

# Find and print the majority elements
result = majorityElement(nums)
print("Majority Elements:", result)

#basic algo of the above code
"""
Initialize two candidate numbers (candidate1, candidate2) and their respective counts (count1, count2) to large values.
First pass: Find potential candidates based on their counts.
Second pass: Count occurrences of potential candidates.
If the count of a candidate is greater than one-third of the array length, it's a majority element.
 
usage:
User inputs a list of numbers.
The algorithm finds and prints majority elements.

time complexity is O(n).
"""