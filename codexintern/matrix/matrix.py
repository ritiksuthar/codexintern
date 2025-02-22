import numpy as np

def input_matrix(rows, cols):
    print(f"Enter {rows} rows with {cols} cols space-separated numbers each:")
    matrix = []
    for i in range(rows):
        row = list(map(int, input().split()))
        #print(row)
        if len(row) != cols:
            print("Invalid input")
            return None
        matrix.append(row)
    return np.array(matrix)

def add_matrix(matrix1, matrix2):
    return np.add(matrix1, matrix2)

def subtract_matrix(matrix1, matrix2):
    return np.subtract(matrix1, matrix2)

def multiply_matrix(matrix1, matrix2):
    return np.dot(matrix1, matrix2)

def transpose_matrix(matrix):
    return np.transpose(matrix)

def detrminant_matrix(matrix):
    return np.linalg.det(matrix)    


def main():
    print("welcome the matrix opration tool")
    rows = int(input("Enter rows: "))
    cols = int(input("Enter cols: "))

    matrix1 = input_matrix(rows, cols)
    print(matrix1)
    if matrix1 is None:
        return
    
    choice = input("Do you want to enter  second  matrix..?(y/n)").strip().lower()
    matrix2=  None
    if choice == "y" or choice == "Y":
        matrix2 = input_matrix(rows, cols) 
        print(matrix2)
        if matrix2 is None:
            return
        
    while True:
        print("******************************Start of the program**********************************")
        print("\n choose an opration")
        print("\n1. addition")
        print("\n2. substraction")
        print("\n3. multiplication")
        print("\n4. transpose")
        print("\n5. determine")
        print("\n6. exit")


        option =int(input("Enter your Choice: "))

        if option ==1 and matrix2 is not None:
            print("result:\n", add_matrix(matrix1, matrix2))
        elif option ==2 and matrix2 is not None:
            print("result:\n", subtract_matrix(matrix1, matrix2))
        elif option ==3 and matrix2 is not None:
            print("result:\n", multiply_matrix(matrix1, matrix2))
        elif option ==4:
            print("result:\n", transpose_matrix(matrix1))
        elif option ==5:
            print("result:\n", detrminant_matrix(matrix1))
        elif option ==6:
            print("exiting...")
            break
        else:
            print("invalid input_3")
        print("******************************End of the program**********************************")

if __name__ == "__main__":
    main()  




