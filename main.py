multiples = "Multiples of 3"
print(multiples)
message = "Here we are going to show you the multiples of 3 to 200"
print(message)

def getMultiples(num, number_of_multiples):
    for i in range(200, (1), -1):
        if i % 3 == 0:
            print(i)

getMultiples(3,66);



