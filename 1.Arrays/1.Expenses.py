# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,

# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
expenses = []
expenses.insert(0,2200)
expenses.insert(1,2350)
expenses.insert(2,2600)
expenses.insert(3,2130)
expenses.insert(4,2190)

# 1. In Feb, how many dollars you spent extra compare to January?
print("\n", expenses[1]-expenses[0])

# 2. Find out your total expense in first quarter (first three months) of the year.
total_expense = 0
for i in range(3):
    total_expense += expenses[i]
print("\n", total_expense)

# 3. Find out if you spent exactly 2000 dollars in any month
print("\n", 2000 in expenses)

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
#** expenses.insert(len(expenses), 1980)
expenses.append(1980)
print("\n", expenses)

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
expenses[3] -= 200
print("\n", expenses)