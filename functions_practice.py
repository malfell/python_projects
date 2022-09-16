# 1
# A function named hello() that prints a greeting to the user. 
#This function should accept no arguments and returns nothing.

def hello():
    print("Hello and greetings to you, mortal.")

hello()

# 2
# A function named pack() that accepts three arguments, 
#and returns a single list with the three arguments inside as list elements.

def pack(item1, item2, item3):
    return [item1, item2, item3]

print("The items packed are:", pack("apple", "sandwich", "cookie"))

# 3
# A function called eat_lunch(). 
# This function should accept a list of any length, 
# and print out a series of strings that say "First I eat __" 
# (the first element of the list), and "Next I eat ___" 
# (for the following elements in the list). 
# If the list is empty, print "My lunchbox is empty!". The function should not return anything.

def eat_lunch(list):
    # use len() to check the number of elements in the list
    # if len() is 0, then lunchbox is empty. If not empty, move to else.
    if len(list) == 0:
        print("My lunchbox is empty!")
    else:
        # if there is food here, the first prints as "first" automatically
        print("First I eat", list[0])
        # then switch to range for the rest
        # Range begins at 1 (so the list item after the first one)
        # Range continues for length of list
        for item in range(1, len(list)):
            print("Next I eat", list[item])

my_list = ["apple", "sandwich", "cookie"]
my_list2 = []
eat_lunch(my_list)
eat_lunch(my_list2)