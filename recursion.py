def factorial(int):
    if int==1 : return 1
    return int*factorial(int-1)

result=factorial(4)
print(result)