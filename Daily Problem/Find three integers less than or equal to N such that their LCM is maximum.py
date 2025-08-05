def lcm(n):
    if n < 3:
        return n
    if n%2!=0:
        return n *(n-1)*(n-2)
    if n%3!=0:
        return n * (n-1) * (n-3)
    return n * (n-1) * (n-2)

n = int(input("Enter a number: "))
Lcm = lcm(n)
print(Lcm)