import timeit
import streamlit as st
import random
import matplotlib.pyplot as plt
import string

k_list=[]
time_list=[]

# Define the function to be tested
# def my_function(*args):#MAIN
#     # Perform some task that depends on the size of n
#     result = 0
#     for i in range(n):
#         for j in range(m):
#             result += i
#     return result

print("Running on basic time it lib:-")

print("Enter 1:Array , 2:string and 3:Integer")
check=int(input())
if(check==3):
    def my_function(n):#MAIN
        # Perform some task that depends on the size of n
        result = 0
        for i in range(n):
            for j in range(n):
                result += i
        return result
    
    print("Enter the starting and ending limit:")
    st_limit,end_limit=map(int,input().split())
    print("Enter the No of iterations")
    s=int(input())
    for n in range(s):
    # Measure the execution time
        k=random.randrange(st_limit, end_limit)
        time = timeit.timeit(lambda: my_function(k))
        # Print the input size and execution time
        print(f"n={n},k={k} time={time:.6f} seconds")
        k_list.append(k)
        time_list.append(time)
    plt.plot(k_list,time_list)
    # x axis ploting 
    plt.xlabel('x - axis')
    # y axis ploting
    plt.ylabel('y - axis')
    plt.title('My first graph!')
    plt.show()

    #scatter plot
    plt.scatter(k_list, time_list)
    plt.legend("A")
    plt.title("Code Analysis")
    plt.show()

elif(check==1):
    #User dependent
    # def my_function(*arg):
    #     #Enter the main program
    #     arg=list(args)
    #     print("Enter the first and last limit of the function:")
    #     st_limit,end_limit=map(int,input().split())
    #     read_list=[]
    #     for i in range(len(args)):
    #         k=random.randrange(st_limit, end_limit)
    #         read_list.append(k)
    def my_function(n):
        #Enter the main program
        res=0
        for i in n:
            for j in n:
                res+=j
        return res
    time_list=[]
    r_list=[]
    print("Enter the no of elements")
    n=int(input())
    print("Enter the first and last limit of the function:")
    st_limit,end_limit=map(int,input().split())
    read_list=[]
    for i in range(n):
        k=random.randrange(st_limit, end_limit)
        read_list.append(k)
    print("Enter the No of iterations:")
    for i in range(int(input())):
        time = timeit.timeit(lambda: my_function(read_list))#calling the function
        time_list.append(time)
        # Print the input size and execution time
        print(f"read_list={read_list} time={time:.6f} seconds")
        r_list.append(sum(read_list))
    plt.plot(r_list,time_list)
    # x axis ploting 
    plt.xlabel('x - axis')
    # y axis ploting
    plt.ylabel('y - axis')
    plt.title('The program analysis !')
    plt.show()

    #scatter plot
    plt.scatter(r_list, time_list)
    plt.legend("A")
    plt.title("Code Analysis")
    plt.show()


else:
    #Incase of the strings
    # def my_function(*args):
    #     #Main code by the user
    def my_function(s1,s2):
        #sample code for checking same element in both string
        c=0
        for i in s1:
            for j in s2:
                if(i==j):
                    c+=1
        return c
    
    time_list=[]
    s_list=[]
    for i in range(5):
        l1,l2=map(int,random.randrange(3, 10))
        s1= ''.join(random.choices(string.ascii_lowercase +string.ascii_uppercase, k=l1))
        s2= ''.join(random.choices(string.ascii_lowercase +string.ascii_uppercase, k=l2))
        time = timeit.timeit(lambda: my_function(s1,s2))
        print(f"s1={s1} ,s2={s2} time={time:.6f} seconds")
        s_list.append(s1)
        time_list.append(time)
    plt.plot(s_list,time_list)
    # x axis ploting 
    plt.xlabel('x - axis')
    # y axis ploting
    plt.ylabel('y - axis')
    plt.title('The program Analysis!')
    plt.show()

    #scatter plot
    plt.scatter(s_list, time_list)
    plt.legend("A")
    plt.title("Code Analysis")
    plt.show()