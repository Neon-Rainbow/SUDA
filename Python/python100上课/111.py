import re


def is_result(n):
    if n in range(-9, 10):
        return False
    lst = list(map(int, str(abs(n))))
    for i in range(len(lst)):
        if (i + 1) % 2 == 0:
            if lst[i] % 2 == 0:
                return False
    return True


def find_numbers(text):
    # find
    pattern = re.compile('-?\d+')
    all_int = list(map(int, pattern.findall(text)))
    res = []
    for number in all_int:
        if is_result(number):
            res.append(number)
    # save
    ans = []
    reformat = '{0:8d}'.format
    for i in range(len(res) // 3 + 1):
        temp = ''.join(map(reformat, res[3 * i:3 * (i + 1)])) + '\n'
        ans.append(temp)
    return ans


def write_file(file_name, new_file_name):
    with open(file_name, encoding="UTF-8") as file_raw:
        text = file_raw.read()
    ans = find_numbers(text)
    with open(new_file_name, "w") as file_result:
        for s in ans:
            file_result.write(s)


if __name__ == "__main__":
    write_file(r"StrInts.txt", r"ResultInts.txt")