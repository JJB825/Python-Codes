def fibonacci(n):
    for i in range(n):
        t1=(1/(5**0.5))*(((1+5**0.5)/2)**i+1)
        t2=(1/(5**0.5))*(((1-5**0.5)/2)**i+1)
        print(round(t1-t2),end=" ")
    print()

fibonacci(5)