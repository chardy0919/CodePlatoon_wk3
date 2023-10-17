def count_up(num, count = 0):
    if count == num:
        return count
    else:
        print(count)
        return count_up(num, count+1)
    
count_up(5)

def count_down(num):
    if num == 0:
        return num
    else:
        print(num)
        return count_down(num -1)

count_down(5)