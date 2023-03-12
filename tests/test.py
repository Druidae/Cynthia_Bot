from math import factorial

def polinoms_numbers():
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))

    for i in range(first_number, second_number + 1):
        i = str(i)
        revers_i = i[::-1]
        if i == revers_i:
            print(i)

def factorial_summ():
    n = int(input("Enter n value: "))
    fact_sum = 0
    fact = 1
    i = 0
    for j in range(1, n+1):
        fact = fact*j
        fact_sum += fact
        if i < n:
            i +=1
    
    print(fact_sum)
if __name__ == "__main__":
    # polinoms_numbers()
    factorial_summ()