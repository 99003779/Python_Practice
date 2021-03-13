import sys

if __name__ == '__main__':
    n = int(input().strip())
if (n % 2 != 0):
    print("Weird")
elif (n % 2 == 0 or range(2, 5)):
    print("Not Weird")
elif n % 2 == 0 or range(6, 20):
    print("Weird")
elif (n % 2 == 0 or n > 20):
    print("Not Weird")
