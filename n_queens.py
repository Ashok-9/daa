def place(row, col):
    for i in range(row):
        if (x[i] == col) or abs(col-x[i]) == abs( row-i ):
            return False
    return True


def Print_Board(x):
    print(x)
    for i in range(len(x)):
        temp = [0] * (len(x))
        temp[x[i]] = i + 1
        print(temp)
    print("")


def nQueens(row, n):
    for col in range(n):
        if place(row, col):
            x[row] = col
            if row == n - 1:
               # Print_Board(x)
                print(x)
                break
            else:
                nQueens(row + 1, n)


n = int(input("Enter the number of Queens: "))
x = [-1] * (n)
print("The possible arrangement of Queens in chessboard are: ")
nQueens(0, n)