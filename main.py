#The algorithmic steps for implementing recursio in a function are as follows:

#step1 - Define a base case: Identify the simplest case for which the soultion is known or trivial
# This is the stopping condition for the recursion.
# as it prevents the function from infinitely calling itself

#step2 -  Define a recursive case: Define the problem in terms of similar subproblems
# break the problem down into similar versions of itself, and call the function recursively to solve each subproblem

#step3 - Ensure the recursion terminiates: Make sure that the recursive function eventually reaches the base case,
# and does not enter an infinite loop


# step4- combine the solutions: Combine the soultions of the subproblems to solve the original problem.

"""
#in the recursive program, the solution to the base case is provided
#and the solution to the bigger problem is expressed in terms of smaller problems

int fact(int n)
{
    if (n < = 1) // base case
        return 1;
    else
        return n*fact(n-1);
}
#in the above example, the base case for n < = 1 is defined and the larger value of a number can be solved
#by converting to a smaller one till the base case is reached.
"""


"""
#Writing a program using the concepts of recursion to find the factorial of the non negative integer number
3
def factorial(n):
    #base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    #recursive case: factorial of n is n * factorial of (n-1)
    else:
        return n * factorial(n-1)

#Input from user
num = int(input("enter a non-negative integer to calculate its factorial: "))

#Check if the number is negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(num)
    print(f"The factorial of {num} is: {result}")
"""
    

"""
What is the difference between direct and indirect recursion?

A function fun is called direct recursive if it calls the same function fun
A function fun is called indirect resursive if it called another function
say fun_new and fun_new  calls fun directly or indirectly.
The difference between direct and indirect recursion has been illustrated in Table 1.

//An example of direct recursion void directRecfun()
{
    // Some code...

    directRecFun();

    //Some code...
}

// An example of indirect recursion
void indirectRecFun1()
{
    //Some code...

    indirectRecFun2():

    //Some code...
}
void indirectRecFun2()
{
    //Some code...
6
    indirectRecFun1();

    //Some code...
}
"""


#Fibonacci Sequence

def fibonacci(n):
    """Generate the  nth Fibonacci number using recursion."""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
#Example usage:
term = 6
print(f"The {term}th Fibonacci number is {fibonacci(term - 1)}") #term-1 because Fibonacci starts from the 0th index


#Sum of List Elements
def sum_list(lst):
    """Calculate the sum of elements in a list using recursion"""
    if not lst:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])

#example usage
my_list = [1, 2, 3, 4, 5]
print(f"The sum of the elements in the list is {sum_list(my_list)}")
