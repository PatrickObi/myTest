# def slicingstrings():
#     word = "abcdefghijk"
#     return word[0:4:1] ##start, stop(up to, but not inclusive), step

# print(slicingstrings())

# def reversestring():
#     word = "abcdefghijk"
#     word.capitalize
#     return word[::-1] ##start, stop(up to, but not inclusive), step

# print(reversestring())

# def splitstring():
#     word = "Hi there, my name is Patrick"
#     return word.split(" ")
# print(splitstring())

# LISTS

# my_list = [1,2,3]
# print(my_list[1:])
# print(my_list[0:2])
# my_list.append(4)
# my_list.pop()
# print(my_list)
# from datetime import datetime

# day = datetime.now().isoweekday()


# my_dict2 = {
#     "1" : "Monday",
#     "2": "Tuesday",
#     "3": "Wednesday",
#     "4": "Thursday",
#     "5": "Friday",
#     "6": "Saturday",
#     "7": ["Sunday",{
#     "7am" : "Wake Up",
#     "8am": "Gym",
#     "11am": "Work",
#     "7pm": "end work"
# } ],
# }



# daytime = input("Enter a time: ")
# if str(day) in my_dict2:
#     print(my_dict2[str(day)][1][daytime])

# my_list = ["a", "a", "b", "b", "b"]
# print(my_list.count("b"))

#Tuples are basically Immutable arrays

# my_set = {1, 2, 3, 4}
# # my_set.pop() #Set is last in first out
# my_set.remove(2)
# print(my_set)

#new skill

# from datetime import datetime

# with open("myFile.txt", "w") as file:
#     file.write("{}".format(datetime.now().date()))

# from datetime import datetime

# with open("myFile.txt", "w+") as file:
#     file.write("This is the first line\n")
#     file.write("THis is the second line\n")
#     file.write("This is the third line\n")
#     file.write("Todays day is {}".format(datetime.now().date()))

#     file.seek(0)

#     content = file.read()

# print(content)

# content = 199
# with open("myFile.txt", "w+") as file:
#     file.write(str(content))

# with open("myFile.txt", "w+") as file:
#     file.write("hello world")

# mylist = list(range(1, 10))
# print(mylist)

# x = 1000000000
# while x < 10000000000:
#     print("hello world")
#     x += 1

#pass - does nothing at all/ a placeholder
#continue - goes back to the top enclosing loop - skipping that index
#break - breaks/stops the top enclosing loop
#zip 

# for i in range(1, 10):
#     if i == 6:
#         continue
#     print(i)

# from random import shuffle

# # myList = list(range(10))
# # random = shuffle(myList)
# # print(myList)

# from random import randint

# print(randint(0, 10))

# st = "Print only the words that start with s in this sentence"
# myList = st.split()

# for i in myList:
#     if i.startswith('s'):
#         print(i)

# for i in range(1, 11):
#     if i % 2 == 0:
#         print(i)

# myList = [x for x in range(0, 51) if x % 3 == 0]
# print(myList)

# st = "Print only the words that start with s in this sentence"
# myList = st.split()

# for i in myList:
#     if len(i) % 2 == 0:
#         print("Even")
    

# for i in range(0, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 5 == 0:
#         print("Buzz")
#     elif i % 3 == 0:
#         print("Fizz")


# st = "Create a list of the first letter of every word in this string"

# myList = st.split()
# ans = [x[0] for x in myList ]

# print(ans)



#create something that uses the current date, a random integer and puts it in a txt file

# from datetime import datetime
# from random import randint

# with open("myFile.txt", "w+") as file:
#     file.write("The random int I get is {} \n".format(randint(1, 100)))
#     file.write("The random current time is {} \n".format(datetime.now().time()))

    
# with open("myFile.txt", "a") as file:
#     file.write("The random int I get is {} \n".format(randint(1, 100)))
#     file.write("The random current time is {}".format(datetime.now().time()))


#Methods
# my_list = list(range(1, 10))
# my_list.append() append is a method

# functions

# name = input("what is your name: ")

# def print_name(n):
#     print("Hello there, {}".format(n))

# print_name(name)

# def even_function(num):
#     return num % 2 ==

# print(even_function(2))

# def evenn_in_list(arr):
#     nums = []
#     for i in arr:
#         if i % 2 == 0:
#             nums.append(i)
            
#     return nums

# print(evenn_in_list([3, 5, 7, 8]))

# work_hours = [("Abby", 100), ("Billy", 400), ("Cassie", 80)]

# def employee_of_the_month(nums):
#     count = 0
#     name = ""
#     for name, hours in nums:
#         if count < hours:
#             count = hours
#         else:
#             pass

#     return hours


# print(employee_of_the_month(work_hours))



# work_hours = [("Abby", 100), ("Billy", 4000), ("Cassie", 800)]

# def employee_month(list_):
#     emp_name = ""
#     max_hours = 0
#     for name, hours in list_:
#         if max_hours < hours:
#             max_hours = hours
#             emp_name = name
#         else:
#             pass
#     return (emp_name, max_hours)

# name, hours = employee_month(work_hours)
# print(hours)

# from random import shuffle


# list_ = [" ", "O", " "]

# def shuffle_list(list_):
#     shuffle(list_)
#     return list_

# def user_input():
    
#     guess = ""
#     while guess not in ["0", "1", "2"]:
#         guess = input("Place a guess, either 0, 1, 2: ")

#     return int(guess)

# def play_game(guess, list):
#     print(list)
#     if list[guess] == "O":
#         print("You have WON")
#     else:
#         print("You loose")
#         print(list)

# list = shuffle_list(list_)
# guess = user_input()
# play_game(guess, list)


# def myfunc(name):
#     print("Hello " + name)

# myfunc("Patrick")
# day = False
# def myfunc(day):
#     if day == True:
#         return "Hello"
#     else:
#         return "Goodbye"

# print(myfunc(day))

# z = True
# y = "Hello"
# x = "Goodbye"
# def myfunc(x,y,z):
#     if z == True:
#         return x
#     else:
#         return y
    
# print(myfunc(x, y, z))

# x = 10
# y = 20
# def myfunc(x, y):
#     return x+ y

# print(myfunc(x, y))

# def myfunc(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False
    
# print(myfunc(3))

# def myfunc(x, y):
#     if x > y:
#         return True
#     else:
#         return False
    
# print(myfunc(20, 20))

# def myfunc(**kwargs):
#     print(kwargs)

# print(myfunc(name="Patrick"))

# def myfunc(*args):
#     return sum(args)

# def myfunc(*args):
#     list_value = []
#     for i in args:
#         if i % 2 == 0:
#             list_value.append(i)
#         else:
#             pass
#     return list_value


# print(myfunc(1, 2, 3, 4, 5, 6, 7, 8, 9))


# def myfunc(s):
#     string_value = ""
#     count = 0
#     for i, value in enumerate(s):
#         count += 1
#         if i % 2 == 0:
#             string_value += value.upper()
#         else:
#             string_value += value

#     return string_value

# def myfunc(word):
#     count = 0
#     a = ""
#     for i in word:
#         count += 1
#         if count % 2 == 0:
#             a += i.upper()
#         else:
#             a += i.lower()
#     return a

# print(myfunc("Anthropomorphism"))



# def lesser_of_two_evens(a,b):
#     if a % 2 == 0 and b % 2 == 0:
#         return min(a, b)
#     elif  a % 2 != 0 or b % 2 != 0:
#         return max(a, b)



# print(lesser_of_two_evens(2,4))
# print(lesser_of_two_evens(2,5))

# def animal_crackers(text):
#     text = text.split()
#     if text[0][0] == text[1][0]:
#         return True
#     else:
#         return False

# print(animal_crackers('Levelheaded Llama'))
# print(animal_crackers('Crazy Kangaroo'))

# def makes_twenty(n1,n2):
#     if n1 == 20 or n2 == 20:
#         return True
#     elif n1 + n2 == 20:
#         return True
#     else:
#         return False
    
# print(makes_twenty(20,10))
# print(makes_twenty(12,8))
# print(makes_twenty(2,3))


# def old_macdonald(name):
#     cap_name = ""
#     for i, value in enumerate(name):
#         if i == 0 or i == 3:
#             cap_name += value.upper()
#         else:
#             cap_name += value
#     return cap_name

# print(old_macdonald('macdonald'))

# def master_yoda(text):
#     text = text.split()
#     valid_text = text[::-1]
#     return " ".join(valid_text)

# print(master_yoda('I am home'))
# print(master_yoda('We are ready'))
        
            
# def almost_there(n):
#     if n in range(90, 110) or n in range(190, 210):
#         return True
#     else:
#         return False
    
# print(almost_there(90))
# print(almost_there(104))
# print(almost_there(150))
# print(almost_there(209))


# def has_33(nums):
#     if nums.count(3) == 1:
#         return False
    
#     return nums.index(3)
# print(has_33([1, 3, 3]))

# def paper_doll(text):
#     ans_value = ""
#     for i in text:
#         ans_value += i*3
#     return ans_value

# print(paper_doll('Hello'))
# print(paper_doll('Mississippi'))

# def count_primes(num):
#     count = 2
#     for i in range(1, num+1):
#         if i % 2 != 0 and i % 3 != 0:
#             count += 1
#     return count
    
# print(count_primes(100))

# def blackjack(a,b,c):
#     sum_values = a + b + c
#     if sum_values <= 21:
#         return sum_values
#     elif sum_values > 21 and a == 11 or b == 11 or c == 11:
#         sum_values = sum_values - 10
#         if sum_values > 21:
#             return "BUST"
#         else:
#             return sum_values
#     else:
#         return "BUST"

    

# print(blackjack(5,6,7))
# print(blackjack(9,9,9))
# print(blackjack(9,9,11))\

# def summer_69(arr):
#     count = 0
#     sum_values = 0
#     for i in arr:
#         if i == 6:
#             count += 1
#             continue
#         elif i == 9:
#             count -= 1
#             continue
        
#         if count == 0:
#             sum_values += i
#     return sum_values
        

# print(summer_69([1, 3, 5]))
# print(summer_69([4, 5, 6, 7, 8, 9]))
# print(summer_69([2, 1, 6, 9, 11]))
 

# def spy_game(nums):
#     answer_array = ["0", "0", "7", "X"]
#     for i in nums:
#         if str(i) == answer_array[0]:
#             answer_array.pop(0)
#         else:
#             continue
#     if len(answer_array) <= 1:
#         return True
#     else:
#         return False

# print(spy_game([1,2,4,0,0,7,5]))
# print(spy_game([1,0,2,4,0,5,7]))
# print(spy_game([1,7,2,0,4,5,0]))

# def myfunc(num):
#     return num**2

# my_nums = [1, 2, 3, 4, 5, 6]

# print(list(map(myfunc, my_nums)))

#filter

# def check_even(num):
#     return num%2 == 0

# my_nums = [1, 2, 3, 4, 5, 6]

# print(list(filter(check_even, my_nums)))

#Lamda expressions
# square = lambda num : num**2
# print(square(2))

# from math import pi
# def vol(rad):
#     return (4/3) * pi * rad**3

# print(vol(2))

# def ran_check(num, low, high):
#     if num >= low and num <= high:
#         print("{} is in the range of {} and {}".format(num, low, high))
#     else:
#         return None
    

# print(ran_check(3,1,10))


# s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
# def up_low(s):
#     upper = 0
#     lower = 0
#     for i in s:
#         if i.isalpha() and i.isupper():
#             upper += 1
#         elif i.isalpha() and i.islower():
#             lower += 1
    
#     return (upper, lower)


# upper, lower = up_low(s)

# print("No. of Upper case characters : {}".format(upper))
# print("No. of Upper case characters : {}".format(lower))


# def unique_list(lst):
#     return set(lst)

# print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))


# def multiply(numbers):  
#     ans = 1
#     for i in numbers:
#         ans *= i
    
#     return ans


# print(multiply([1,2,3,-4]))


# def palindrome(s):
#     return s == s[::-1]

# print(palindrome('nurses run'))


# def ispangram(str1):
#     hash = {}
#     for i in str1:
#         if i.isalpha():
#             if i in hash:
#                 hash[i.lower()] += 1
            
            
#             hash[i.lower()] = 1
#     return len(hash.keys() )== 26

# print(ispangram("leetcode"))

#####Tic tac toe game

# def user_input():
#     valids = ["X", "O"]
#     userValue1 = ""
#     while userValue1.upper() not in valids:
#         userValue1 = input("Player 1: Do you wasnt to be X or O: ").upper(x)

#     return userValue1
       
    

# def player_input():
#     player1 = user_input()
#     if player1 == "X":
#         player2 = "O"
#     elif player1 == "O":
#         player2 = "X"

#     return (player1, player2)

# def board(arr):
    
#     print(" {}  | {}  | {}".format(arr[0], arr[1], arr[2]))
#     print("----|----|--------")
#     print(" {}  | {}  | {}" .format(arr[3], arr[4], arr[5]))
#     print("----|----|--------")
#     print(" {}  | {}  | {}".format(arr[6], arr[7], arr[8]))



# # def check_wins(arr):
# #     if arr[0] == arr[3] ==arr[6] == "X":


# # def main():
# #     arr =[""]*9
    

# print(board(['#','X','O','X','O','X','O','X','O','X']))



#Object oriented programming



#Tic Tac Toe game

#game starts by asking if they would like to X or O
#using plyaers input they would be that and would have to go first
#show board
#ask player wher they tould like to move
#populate it on thhe board and display it
#ask the player where they would like to move again - using the while loop
#create a win function
#Done

def player_input():
    marker = ""
    playerinput = ""
    while playerinput not in ("X", "O"):
        playerinput = input("Please select what you would like to be X or O: ").upper()

    if playerinput == "X":
        return ("X", "O")
    elif playerinput == "O":
        return ("O", "X")
    
def board(arr):
    
    print(" {}  | {}  | {}".format(arr[0], arr[1], arr[2]))
    print("----|----|--------")
    print(" {}  | {}  | {}" .format(arr[3], arr[4], arr[5]))
    print("----|----|--------")
    print(" {}  | {}  | {}".format(arr[6], arr[7], arr[8]))


def check_win(arr, mark):
    if arr[0] and arr[3] and arr[6] == mark or arr[0] and arr[1] and arr[2] == mark or arr[3] and arr[4] and arr[5] == mark or arr[6] and arr[7] and arr[8] == mark or arr[1] and arr[4] and arr[7] == mark or arr[2] and arr[5] and arr[8] == mark or arr[0] and arr[4] and arr[8] == mark or arr[2] and arr[4] and arr[6] == mark:
        print("YOU WIN")
        return True

if __name__ == "__main__":
    
    arr = [" "]*9
    player1, player2 = player_input()
    
    turn = "player1"
    while True:
        position = int(input("Where would ypou like to play- choose from 0-8: "))

        if turn == "player1":
            arr[position] = player1
            
            board(arr)
            if check_win(arr, player1) == True:
                break
            
            turn = "player2"
        elif turn == "player2":
            
            arr[position] = player2
            
            board(arr)
            if check_win(arr, player2) == True:
                break
            
            turn = "player1"


    
    

