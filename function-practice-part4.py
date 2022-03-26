def max_num(a, b, c):
    if a >= b and a >= c:
        return(a)
    elif b >= a and b >= c:
        return(b)
    elif c >= a and c >= b:
        return(c)
print(f"Max of the three nums: {max_num(6.1, 6, 6)}")

def mult_list(*num):
    x = 1
    for i in num:
        x = (x*i)
    return(x)
    
num = [4, 5, 7, 4, 5, 2]
print(f"This is the product of all the numbers in the list: {mult_list(*num)}")

def rev_string(string):
    return(string[::-1])
string = "hey hows it going?"
print(rev_string(string))


def nth_num(num):
    def fib(n):
        if n < 0:
            return("Negative numbers not accepted")
        elif n <= 1:
            return(n)
        else:
            return(fib(n-1)+fib(n-2))
    return(fib(num-1))

num = 6
print(nth_num(num))
    
def num_within(a, b, c):
    for i in range(b, c+1):
        if a == i:
            return True
    if num_within != True:
        return(False)
        
a = 5
b = 3
c =18

print(f"It is {num_within(a, b, c)} that {a} is within the range of {b} and {c}")

def pascal(num):
    rows = []
    for row in range(1, num+1):
        rows.append(1)
        for j in range(row - 2, 0, -1):
            rows[j] += rows[j-1]
        print(rows)
    return rows


pascal(9)