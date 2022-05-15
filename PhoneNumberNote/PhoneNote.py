
from sqlite3 import Error
import sqlite3
import random as rd

def iscontinue():
    print('Do You Want to Exit : yes/no')
    sel=input()
    if sel=='yes':
        return 1
    else:
        MainMenu()


def sql_connection():
    try:
        global con
        con=sqlite3.connect('PhoneNumber.db')
        print('DataBase was seccessfuly created.')
    except :
        print(Error)
    finally:
        cursor=con.cursor()
        cursor.execute('CREATE TABLE member(id int , name char(60),phonenumber char(15),address char (100))')
        con.commit()
        con.close()


def AddMember():
    
    print('please enter the "name" of your member:')
    name=input() 
    print('please enter the "phone number" of your member:')
    phone=input()
    print('please enter the "address" of your member:')
    address=input()
    randnum=rd.randrange(1000,2000)  # set random num between 1000 to 2000
    con=sqlite3.connect('PhoneNumber.db')
    cursor=con.cursor() #set cursor
    inset_str=f'''INSERT INTO member(id,name,phonenumber,address)
                VALUES
                ({randnum},'{name}','{phone}','{address}') ;
                                                            ''' #pass values to member
    cursor.execute(inset_str) # pass insert_str to execute
    con.commit()  # Save changes
    con.close()
    iscontinue()

def SearchMember():
    print('please enter "name" of member you search for:')
    name=input()
    con=sqlite3.connect('PhoneNumber.db')
    cur=con.cursor()   
    insert_str=f'''SELECT * FROM  member
                   WHERE member.name='{name}';
    '''
    recordd=cur.execute(insert_str)
    print(type(recordd),recordd)
    if recordd:
        print('--------------------------------------')
        for row in recordd:
            print("ID:",row[0])
            print("Name:",row[1])
            print("Phone:",row[2])
            print("Address:",row[3])
            print('--------------------------------------')
        con.close()
        iscontinue()
    else:
        print('Sorry your member you search for is not exist :(  .')
        con.close()
        iscontinue()

def DeleteMember():
    print('please enter "name" of member you want to Delete:')
    name=input()
    con=sqlite3.connect('PhoneNumber.db')
    cur=con.cursor()
    insert_str=f'''DELETE FROM member WHERE name='{name}';
    '''
    cur.execute(insert_str)
    con.commit()
    con.close()
    iscontinue()


def MainMenu():   
    print('1)Add Member \n2)Search Member \n3)Delete Member \n4)Exit')
    sel=int(input('Please enter number of option : '))
    if sel==1:
        AddMember()
    elif sel==2:
        SearchMember()
    elif sel==3:
        DeleteMember()
    elif sel==4:
        return 0

MainMenu()


