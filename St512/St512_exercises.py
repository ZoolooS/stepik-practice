def uniq_obj_counter(objects=list):
    print(len(set([id(el) for el in objects])))

#uniq_obj_counter(objects)

##===================================================================##
def closest_mod_5(x):
    for i in range(5):
        if (x + i) % 5 == 0:
            print(x + i)
            return x + i
    return "I don't know :("

#closest_mod_5(x)
#closest_mod_5(11)
#closest_mod_5(10)
#closest_mod_5(114)

##===================================================================##
def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)

#print(fib(5))
#fib()

##===================================================================##
def numbers_of_combinations():
    from math import factorial
    n, k = map(int, input().split())

    noc = factorial(n) // (factorial(k) * factorial(n - k))
    print(noc)

numbers_of_combinations()

##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##