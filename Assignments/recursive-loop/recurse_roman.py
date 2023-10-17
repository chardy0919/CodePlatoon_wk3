# make this recursive
def to_roman(num, answer= ""):
    # write your code here!
    # {4: "IV", 9: "IX", 40: "XL", 90: "XC", 400: "CD", 900: "CM"}
    numerals ={
        "M" : 1000,
        "CM": 900,
        "D" : 500,
        "CD": 400,
        "C" : 100,
        "XC": 90,
        "L" : 50,
        "XL": 40,
        "X" : 10,
        "IX": 9,
        "V" : 5,
        "IV": 4,
        "I" : 1,
    }
    if num == 0:
        return answer
    for numeral, val in numerals.items():
        if num >= val:
            print(num, answer)
            return to_roman(num=num%val, answer = answer + numeral*(num//val))

print(to_roman(699))


# def bottle_song(bottles):
# 	if bottles > 2:
# 		print(f"""{bottles} bottles of beer on the wall, {bottles} bottles of beer.
# Take one down and pass it around, {bottles - 1} bottles of beer on the wall.""")
# 		bottle_song(bottles-1)	
# 	return f"""2 bottles of beer on the wall, 2 bottles of beer.
# Take one down and pass it around, 1 bottle of beer on the wall.
# 1 bottle of beer on the wall, 1 bottle of beer.
# Take one down and pass it around, no more bottles of beer on the wall.
# No more bottles of beer on the wall, no more bottles of beer.
# Go to the store and buy some more, 99 bottles of beer on the wall."""

# print(bottle_song(69))

# def factorial(n):
#     if n == 1:
#         return 1
#     return n*factorial(n-1)

# print(factorial(5))

def fibo(num, value1=0, value2=1):
    if num <= 1:
        return value2
    print(value1, value2)
    return fibo(num-1, value1= value2, value2 = value1+value2)
    
print(fibo(81))

def fibo(num):
    if num <= 1:
        return num
    print((num - 1),(num -2), (num - 1)+(num -2))
    return fibo(num - 1) + fibo(num -2)

print(fibo(81))

