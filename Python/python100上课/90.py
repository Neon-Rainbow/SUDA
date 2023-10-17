def pan_duan_zhi_shu(a):
    for i in range(2, a):
        if a % i == 0:
            break
    else:
        return True


def pan_duan_fan_zhi_shu(b):
    b = str(b)
    if b == b[::-1]:
        return False
    else:
        if pan_duan_zhi_shu(int(b)) == pan_duan_zhi_shu(int(b[::-1])) == True:
            return True


def zhao_chu_qian_30_ge_fan_zhi_shu():
    print_count1 = 0
    print_count2 = 0
    lst = [0 for i in range(30)]
    count = 0
    for i in range(1000):
        if pan_duan_fan_zhi_shu(int(i)) == True:
            lst[count] = int(i)
            count += 1
        if count == 30:
            break
    for i in lst:
        print(f'{i:>5}',end='')
        print_count1 += 1
        if print_count1 == 8:
            print()
            print_count1 = 0
        if print_count2 == 30:
            break


zhao_chu_qian_30_ge_fan_zhi_shu()