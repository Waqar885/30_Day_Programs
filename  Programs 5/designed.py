# Enter your code here. Read input from STDIN. Print output to 
def print_pattren(rows, columns):
    # Top half
    for i in range(1, rows // 2 + 1):
        pattern = '.|.' * (2 * i - 1)
        print(pattern.center(columns, '-'))
    
    # Center line
    print('WELCOME'.center(columns, '-'))
    
    # Bottom half
    for i in range(rows // 2,0, -1):
        pattern = '.|.' * (2*i -1)
        print(pattern.center(columns, '-'))

first = int(input("Enter the first num: "))
sec = int(input("Enter the first num:" ))
print_pattren(first, sec)