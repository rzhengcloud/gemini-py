def my_generator():
    print("starting generator")
    yield 1
    print("after yielding 1")
    yield 2
    print("after yielding 2")
    yield 3
    print("after yielding 3")

def my_func():
    yield 4
    return "lol"
gen = my_generator()
fun = my_func()
print(gen)

print(my_func())
print(my_func)
print(next(gen))  # Output: starting generator \n 1
print(next(gen))  # Output: after yielding 1 \n 2