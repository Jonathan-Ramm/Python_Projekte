

def fib(number):
    merke1, merke2 = 0, 1
    for i in range(2, number):
        merke3 = merke1 + merke2
        merke1 = merke2
        merke2 = merke3
    return merke2

a = 20000000
fibonacci = fib(a + 1)
print(fibonacci)


