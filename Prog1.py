def four_Num():
    num_a = float(input("First Number: "))
    num_b = float(input("Second Number: "))
    num_c = float(input("Third Number: "))
    num_d = float(input("Fourth Number: "))

# first number is the largest
    if num_a > num_b and num_a > num_c and num_a > num_d:
        if num_b > num_c and num_b > num_d:
            if num_c > num_d:
                four_Num = num_a, num_b, num_c, num_d
            else:
                four_Num = num_a, num_b, num_d, num_c
            return four_Num
        elif num_c > num_b and num_c > num_d:
            if num_b > num_d:
                four_Num = num_a, num_c, num_b, num_d
            else: 
                four_Num = num_a, num_c, num_d, num_b
            return four_Num
        else:
            if num_c > num_b:
                four_Num = num_a, num_d, num_c, num_b
            else:
                four_Num = num_a, num_d, num_b, num_c
            return four_Num

# second number is the largest
    if num_b > num_a and num_b > num_c and num_b > num_d:
        if num_a > num_c and num_a > num_d:
            if num_c > num_d:
                four_Num = num_b, num_a, num_c, num_d
            else:
                four_Num = num_b, num_a, num_d, num_c
            return four_Num
        elif num_c > num_a and num_c > num_d:
            if num_a > num_d:
                four_Num = num_b, num_c, num_a, num_d
            else: 
                four_Num = num_b, num_c, num_d, num_a
            return four_Num
        else:
            if num_c > num_a:
                four_Num = num_b, num_d, num_c, num_a
            else:
                four_Num = num_b, num_d, num_a, num_c
            return four_Num

# third number is the largest
    if num_c > num_a and num_c > num_b and num_c > num_d:
        if num_a > num_b and num_a > num_d:
            if num_b > num_d:
                four_Num = num_c, num_a, num_b, num_d
            else:
                four_Num = num_c, num_a, num_d, num_b
            return four_Num
        elif num_b > num_a and num_b > num_d:
            if num_a > num_d:
                four_Num = num_c, num_b, num_a, num_d
            else: 
                four_Num = num_c, num_b, num_d, num_a
            return four_Num
        else:
            if num_a > num_b:
                four_Num = num_c, num_d, num_a, num_b
            else:
                four_Num = num_c, num_d, num_a, num_b
            return four_Num

# fourth number is the largest
    if num_d > num_a and num_d > num_b and num_d > num_c:
        if num_a > num_b and num_a > num_c:
            if num_b > num_c:
                four_Num = num_d, num_a, num_b, num_c
            else:
                four_Num = num_d, num_a, num_c, num_b
            return four_Num
        elif num_b > num_a and num_b > num_c:
            if num_a > num_c:
                four_Num = num_d, num_b, num_a, num_c
            else: 
                four_Num = num_d, num_b, num_c, num_a
            return four_Num
        else:
            if num_a > num_b:
                four_Num = num_d, num_c, num_a, num_b
            else:
                four_Num = num_d, num_c, num_b, num_a
            return four_Num