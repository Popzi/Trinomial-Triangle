def triangle(rows):
    row = [1]
    for _ in range(rows):
        print(row)
        row = [sum(t) for t in zip([0,0]+row, [0]+row+[0], row+[0,0])]

def A():
 a, b, n = 1, 1, 1
 yield a
 while True:
    yield b
    n += 1
    a, b = b, ((3*(n-1))*a+(2*n-1)*b)//n

number = int(input("How many rows do you want printed? "))
print("Printing Triangle\n\n")
triangle(number)
print("\n\nPrinting Trinomial Coefficients\n")
coeff = A()
print([next(coeff) for _ in range(number)])
