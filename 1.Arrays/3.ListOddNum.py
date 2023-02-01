# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

from pickletools import int4


def OddNum(maxNum):
    odd_num = []
    for i in range(maxNum):
        if(i%2 != 0):
            odd_num.append(i)
    print(odd_num)

max = int(input("Please enter a max number: "))
OddNum(max)