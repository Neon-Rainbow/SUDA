def perceptron(T: list, eta: float, dimension: int) -> list:
    w: list = [0] * dimension
    b: float = 0
    label = 1
    while label == 1:
        for i in T:
            if float(i[-1]) * (matrix_mult(i[0:2], w, dimension) + b) <= 0:
                temp_list: list = update(w, b, eta, i[0:2], i[-1], dimension)
                w = temp_list[0]
                b = temp_list[1]
                label += 1
        if label != 1:
            label = 1
        else:
            label = 0
    return [w, b]


def matrix_mult(lst1: list, lst2: list, dimension: int) -> int:
    ans: int = 0
    for i in range(dimension):
        ans += float(lst1[i]) * float(lst2[i])
    return ans


def sign(x) -> int:
    if x >= 0:
        return 1
    else:
        return -1


def update(w: list, b: float, eta: float, point: list, y: int, dimension: int) -> list:
    for i in range(dimension):
        w[i] = float(w[i]) + float(eta) * float(point[i]) * float(y)
    b = float(b) + float(eta) * float(y)
    return [w, b]


def read_file(filename: str) -> list:
    lst: list = []
    dimension: int = 0
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            lst.append(line.strip("\n").split(','))
            dimension = len(line.split(','))
    return [lst, dimension]


def signed_number(num) -> str:
    if num > 0:
        return "+{}".format(num)
    else:
        return "{}".format(num)


if __name__ == '__main__':
    lst, dimension = read_file("Iris.txt")
    total_length = len(lst)
    training_length = int(total_length * 0.75)
    dimension -= 1
    w, b = perceptron(lst[0:training_length], 0.01, dimension)
    test_lst = lst[training_length + 1:]
    wrong_data = 0
    for i in test_lst:
        if float(i[-1]) * (matrix_mult(i[0:2], w, dimension) + b) <= 0:
            wrong_data += 1

    print(f"w为{w}T,b为{round(b, 4)}")
    print(f"超平面为: {w[0]}x(1){signed_number(w[1])}x(2){signed_number(b)}")
    print(f"正确率为: {((total_length - training_length - wrong_data) / (total_length - training_length)) * 100}%")
