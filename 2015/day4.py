from hashlib import md5
number = 0
while True:
    input_day4 = "iwrupvqb" + str(number)
    md5hash = md5(input_day4.encode('utf-8')).hexdigest()
    if md5hash[:6] == "000000":
        print(f"The hash: {md5hash}")
        break
    else:
        number +=1
print(f"Solution: {number}")