import random

# the function that help user to guess number
def help(snum,score):
    print('--------------------------------------------')
    print('help :')
    print("1) odd or even --- cost : 5\n2) The remainder is divided by '10' --- cost : 10")
    print('3) is less than from a number ? --- cost : 15\n4) range of numbers --- cost : 25 ')
    print(f'your remaning score is : {score}')
    print('--------------------------------------------')   
    sel=int(input('Please input your choise :'))
    if sel==1:
        print('--------------------------------------------')
        smod=snum%2
        if smod == 0:
            print('the number is "even"')
        else:
            print('the number is "odd"')
        score-=5
        print('--------------------------------------------')
    elif sel==2:
        print('--------------------------------------------')
        smod10=snum%10
        print(f"mod of number to '10' is : {smod10}")
        score-=10
        print('--------------------------------------------')
    elif sel==3:
        print('--------------------------------------------')
        lessnum=int(input("Please enter your selected number :"))
        if snum < lessnum:
            print('Yes')
        else:
            print('No')
        score-=15
        print('--------------------------------------------')
    elif sel==4:
        print('--------------------------------------------')
        up=int(input("please input upper bound :"))
        low=int(input("please input lower bound :"))
        if snum >= low and snum <= up :
            print(f'the number is between {low} and {up}')
        else:
            print('the number is out of range !!!')
        score-=25
        print('--------------------------------------------')
    else:
        print('invalid number !!!')
        help(snum)
        print('--------------------------------------------')
    return score

# the main function to handel project
# in this at first you have 100 points . if you use help the points will be decrease . and if your points are 0 you lose
def menu():
    print('--------------------------------------------')
    print("Wellcome to the guess number game !!!")
    print('in this game you will guess a number between "1" to "100"')
    print('we set a number between specified range .')
    print('you can guess twenty times and at first you have 100 point !!! ')
    setnum=random.randint(1,100) #set random number from 1 to 100
    score=100
    times=1
    #print(setnum)
    while times<21:
        geussnum=int(input('please enter your guess number :'))
        if setnum == geussnum :
            print(" < you guessed correctly the number >")
            print(f'the time of try is : ({times}) and your point is : ({score})')
            break
        else:
            times+=1
            ishelp=int(input('Do you want Help ? please enter 1(Yes) 2(No) :'))
            if ishelp == 1:
                score=help(setnum,score)
            else:
                if score <=0 :
                    print('you lose all of your points !!!')
                    break

menu()



