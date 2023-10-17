def qiu_yin_zi_he(a):
    sum = 0
    for i in range(1,a):
        if a%i == 0:
            sum += i
    return  sum
print(qiu_yin_zi_he(8))