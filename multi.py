
def multi(number):
    endnum = number
    i = 1
    while i < endnum + 1:
        j = 1
        while j < endnum + 1:
            result = i * j
            print(str(i) + "*" + str(j) + "=" + str(result))
            j += 1
        i += 1

multi(10)
