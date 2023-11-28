from itertools import combinations

# Choice menu
def choiceMenu():
    print("What do you want to do?\n"
    "1) Enter a new list of numbers\n"
    "2) Edit the list of numbers\n"
    "3) Find combinations of numbers\n"
    "4) enter the desired sum\n"
    "5) Check for combinations that add up to the desired sum\n"
    "0) Exit")
    choice = input("Enter your choice: ")
    return choice


# 1) Give list
def giveList():
    while True:
        try:
            numbers = list(map(int, input("Enter the numbers you want to use, separated by spaces: ").split()))
            break
        except ValueError:
            print("Please enter only numbers separated by spaces.")
    return numbers


# 2) Edit list
def editList(numbers):
    while True:
        print("What do you want to do?\n"
        "1) Add a number to the list\n"
        "2) Remove a number from the list\n"
        "3) edit a number in the list\n"
        "0) Exit\n")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                numbers.append(int(input("Enter the number you want to add: ")))
            elif choice == "2":
                numbers.pop(int(input("Enter the index of the number you want to remove: ")))
            elif choice == "3":
                numbers[int(input("Enter the index of the number you want to edit: "))] = int(input("Enter the new number: "))
            elif choice == "0":
                break
            else:
                print("Please enter a valid choice.")
        except ValueError:
            print("Please enter only numbers.")
    return numbers


# 3) Finding combinations of  numbers
def findCombinations(numbers):
    try:
        amount = int(input("Enter the amount of numbers you want to combine: "))
        combs = combinations(numbers, amount)
    except ValueError:
        print("Please enter only numbers.")
    return combs


# 4) Asking for the sum to be found
def sumToBeFound():
    while True:
        try:
            sumToBeFound = int(input("Enter the sum you want to find: "))
            break
        except ValueError:
            print("Please enter only numbers.")
    return sumToBeFound


# 5) Checking for combinations that add up to the desired sum
def checkCombination(combs, SumToBeFound):
    for comb in combs:
        if sum(comb) == SumToBeFound:
            print("The combination that adds up to", SumToBeFound, "is:", comb)
            break
        else:
            print("There is no combination that adds up to", SumToBeFound, "in the list of numbers.")


##################################################################################################### Main
def main():
    print("Welcome to the combination finder!")
    print("You can use this program to find combinations of numbers that add up to a desired sum.")
    numbers = []
    combs = []
    SumToBeFound = 0

    while True:
        print("The current list of numbers is:", numbers)
        choice = choiceMenu()
        print()
        if choice == "1":
            numbers = giveList()
        elif choice == "2":
            numbers = editList(numbers)
        elif choice == "3":
            combs = findCombinations(numbers)
        elif choice == "4":
            SumToBeFound = sumToBeFound()
        elif choice == "5":
            if combs == []:
                print("You have to find the combinations first.")
            elif SumToBeFound == 0:
                print("You have to enter the desired sum first.")
            else:
                checkCombination(combs, SumToBeFound)
        elif choice == "0":
            break
        else:
            print("Please enter a valid choice.")
        print()

main()
