# Convert the following values to binary using “divide by 2.” Show the stack of remainders.

# 17

# 45

# 96

def divide2(num):
    ans = []
    while(num != 0):
        if (num % 2 != 0):
            ans.insert(0, 1)
        else:
            ans.insert(0, 0)
        num = num//2
    return ans


print(divide2(45))
# Convert the following infix expressions to prefix (use full parentheses):

# (A+B)*(C+D)*(E+F)
print("**+AB+CD+EF")
# A+((B+C)*(D+E))
print("+A*+BC+DE")
# A*B*C*D+E+F
print("++***ABCDEF")
# Convert the above infix expressions to postfix (use full parentheses).
print("AB+CD+EF+**")
print("ABC+DE+*+")
print("++***ABCDEF")
# Convert the above infix expressions to postfix using the direct conversion algorithm. Show the stack as the conversion takes place.

# Evaluate the following postfix expressions. Show the stack as each operand and operator is processed.

# 2 3 * 4 +

# 1 2 + 3 + 4 + 5 +

# 1 2 3 4 5 * + * +

# The alternative implementation of the Queue ADT is to use a list such that the rear of the queue is at the end of the list. What would this mean for Big-O performance?
# N
# What is the result of carrying out both steps of the linked list add method in reverse order? What kind of reference results? What types of problems may result?

# Explain how the linked list remove method works when the item to be removed is in the last node.
# It'll have to iterate through each node to reach the end and it will be reach the end to remove it
# Explain how the remove method works when the item is in the only node in the linked list.
