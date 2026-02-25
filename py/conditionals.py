# import sys


# TODO: conditionals -> if-else, match-case

# if-else
ans = int(input("Make a guess between 1-5 (inc both): ")) # ! input always return a string
# ans = int(ans)
if(ans == 5):
    print("you guessed the rihgt number!")
else:
    print("Try again")


# match-case
isMale = True
gender = input("Enter your gender (M for male and F for female): ")[0]
match(gender):
    # case 'M':
    #     isMale = True
    # case 'm':
    #     isMale = True
    # case 'f':
    #     isMale = False
    # case 'F':
    #     isMale = False
    case 'M' | 'm':
        isMale = True
    case 'F' | 'f':
        isMale = False
    case _:
        print("invalid gender type exiting..")

        # sys.exit()
        exit()

print("Male") if isMale else print("Female")