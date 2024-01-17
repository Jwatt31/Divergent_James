

# lists and tulps
#append(item) = end of list add itesm
#insert(index,item) = add item to the #index of the list
#

#6-1 prime number checker



# function that prompts user for input of a number 1-5000 thats vaild

is_prime=0
def user_num():
    num = int(input("give me a number between 1-5000: "))
    if num >=1 and num <=  5000:
        print("valid")
        return num
    else: 
        print("not valid")


# get factors
def get_factors(num):
    factors = []
    for factor in range(1,num+1):
        factor = num % factor
        if factor == 0:
            factors.append(factor)
    # print(factor)
    return factors

# prime_checker()

def prime_checker(num, factors):
        if len(factors) == 2:
            print(f" fac")
        else:
            print(f"")
       
    



def main():
    # title in main loop
    print("Prime number checker")
    

    num = user_num()
    factors = get_factors
    prime_checker(num,factors)



if __name__ == "__main__":
    main()

# prime_checker(5)