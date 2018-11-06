"""
    Exercise 2.4

    Assume that we execute the following assignment statements:
        width = 17
        height = 12.0

    For each of the following expressions, write the value of the expression and the type (of the value of the expression).
        1. width/2
        2. width/2.0
        3. height/3
        4. 1 + 2 * 5

    Use the Python interpreter to check your answers.
"""
width = 17
height = 12.0

print("Width type: [%s]; Height type: [%s];" % (type(width), type(height)))

print("width/2 = [%s] | [%s]" % (width/2, type(width/2)))
print("width/2.0 = [%s] | [%s]" % (width/2.0, type(width/2.0)))
print("height/3 = [%s] | [%s]" % (height/3, type(height/3)))
print("1 + 2 * 5 = [%s] | [%s]" % (1 + 2 * 5, type(1 + 2 * 5)))