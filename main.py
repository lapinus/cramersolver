print("Welcome to Cramer solver!")
def twoeqsys():
    print("First equation")
    eq1x = float(input("X Coefficient = "))
    eq1y = float(input("Y Coefficient = "))
    eq1known = float(input("Known value = "))

    print("Second equation") 
    eq2x = float(input("X Coefficient = "))
    eq2y = float(input("Y Coefficient = "))
    eq2known = float(input("Known Value = "))

    # Let's define a few variables: the determinant of the 2x2 matrix, the determinant of the X variable and the determinant of the Y variable.
    det = eq1x * eq2y - eq1y * eq2x 
    detx = eq1known * eq2y - eq1y * eq2known
    dety = eq1x * eq2known - eq1known * eq2x

    # This if-cycle determines whether the system has a unique solution, infinite solutions, or no solutions. 
    if det != 0:
        x = detx/det
        y = dety/det
        print("The system has a unique solution; " "X =", x, "Y =", y)
    elif (det == 0 and detx*dety != 0):
        print("The system has no solutions")
    elif det == 0 and detx == 0 and dety == 0:
        print("The system has infinite solutions")

def threeeqsys():
    print("First equation")
    eq1x = float(input("X Coefficient = "))
    eq1y = float(input("Y Coefficient = "))
    eq1z = float(input("Z Coefficient = "))
    eq1known = float(input("Known value = "))

    print("Second equation") 
    eq2x = float(input("X Coefficient = "))
    eq2y = float(input("Y Coefficient = "))
    eq2z = float(input("Z Coefficient = "))
    eq2known = float(input("Known value = "))

    print("Third equation")
    eq3x = float(input("X Coefficient = "))
    eq3y = float(input("Y Coefficient = "))
    eq3z = float(input("Z Coefficient = "))
    eq3known = float(input("Known value = "))
    
    # Some variables 
    det = eq1x * eq2y * eq3z + eq1y * eq2z * eq3x + eq1z * eq2x * eq3y - (eq1z * eq2y * eq3x + eq1x * eq2z * eq3y + eq1y * eq2x * eq3z)
    detx = eq1known * eq2y * eq3z + eq1y * eq2z * eq3known + eq1z * eq2known * eq3y - (eq1z * eq2y * eq3known + eq1known * eq2z * eq3y + eq1y * eq2known * eq3z)
    dety = eq1x * eq2known * eq3z + eq1known * eq2z * eq3x + eq1z * eq2x * eq3known - (eq1z * eq2known * eq3x + eq1x * eq2z * eq3known + eq1known * eq2x * eq3z)
    detz = eq1x * eq2y * eq3known + eq1y * eq2known * eq3x + eq1z * eq2x * eq3y - (eq1known * eq2y * eq3x + eq1x * eq2known * eq3y + eq1y * eq2x * eq3known)
    
    # This if-cycle determines whether the system has a unique solution, infinite solutions, or no solutions. 
    if det != 0:
        x = detx/det
        y = dety/det
        z = detz/det
        print("The system has a unique solution; " "X =", x, "Y =", y, "Z =", z )
    elif (det == 0 and detx*dety*detz != 0):
        print("The system has no solutions")
    elif det == 0 and detx == 0 and dety == 0 and detz == 0:
        print("The system has infinite solutions")


systype = 0
while systype != 2 or systype != 3:
    systype = int(input("Press 2 for solving a 2-equation system, press 3 for solving a 3-equation system "))

    if systype == 2:
        print("2-equation system chosen.")
        twoeqsys()
        break
    elif systype == 3:
        threeeqsys()
        break
    else:
        print("Please choose either 2 or 3.")
