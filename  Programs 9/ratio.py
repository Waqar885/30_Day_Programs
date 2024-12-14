def plusMinus(arr):
    length = len(arr)
    positive = []
    negetive = []
    zero = []
    
    for i in arr:
        if i > 0:
            positive.append(i) 
        elif i < 0:
            negetive.append(i) 
        else:
            zero.append(i)
            
    calculation_positive = len(positive)/length
    calculation_negetive = len(negetive)/length
    calculation_Zero = len(zero)/length
    print(f"{calculation_positive:.6f}")
    print(f"{calculation_negetive:.6f}")
    print(f"{calculation_Zero:.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input("Enter list of number: ").rstrip().split()))

    plusMinus(arr)
