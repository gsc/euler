def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return fibonacci(n-1) +fibonacci(n-2)

i = 2
acum = 0

while True:
    term = fibonacci(i)
    if term > 4000000:
        print('break at :'+str(i))
        break
    else:
        print('sum '+str(term)+' i:'+str(i))
        acum +=term        
        i += 3


