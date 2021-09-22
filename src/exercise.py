def main():
    #write your code below this line
    num = int(input())
    print_from_number_to_one(num)

def print_from_number_to_one(num):
    while (num > 0):
        print(num)
        num -= 1

if __name__ == '__main__':
    main()
