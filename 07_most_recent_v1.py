# Get data from user and store it in a list, then
# display the most resent three entries

# set up empty list
all_calculations = []

# Get five items of data
for item in range(0, 5):
    get_item = input("Enter an item")
    all_calculations.append(get_item)

# show that everything made it to the list
print()
print("*** The Full List ***")
print(all_calculations)

print()

print("*** Most Recent 3 ***")
# print items starting at the END of the list
for item in range (0,3):
    print(all_calculations[len(all_calculations) - item - 1])