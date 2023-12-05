#Given an integer numRows, return the first numRows of Pascal's triangle.


def generate_pascals_triangle(numRows):
    triangle = []

    for i in range(numRows):
        row = [1] * (i + 1)

        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle

def print_pascals_triangle(triangle):
    print("[", end="")
    for i in range(len(triangle)):
        print("[", end="")
        for j in range(len(triangle[i])):
            print(triangle[i][j], end="")
            if j < len(triangle[i]) - 1:
                print(",", end="")
        print("]", end="")
        if i < len(triangle) - 1:
            print(",", end="")
    print("]")

# Example usage
numRows = int(input("numRows : "))
result = generate_pascals_triangle(numRows)
print_pascals_triangle(result)


#basic algo of the code
"""
Generate Pascal's Triangle:

Create an empty triangle list.
Repeat for each row (from 0 to numRows - 1):
Create a row with i + 1 elements, all initially set to 1.
Update the row elements from the second to the second-to-last by adding the values above and to the left in the previous row.
Add the generated row to the triangle.
Print Pascal's Triangle:

Print Pascal's Triangle in a structured format.


"""