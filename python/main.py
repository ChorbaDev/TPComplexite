from experimentateur import test

if __name__ == '__main__':
    res_list = []
    m = 10
    for i in range(1, 11):
        for p in range(1, m + 1):
            res_list.append(test(p, m))
        with open("res-" + str(m) + ".dat", "a") as file:
            file.write(str(res_list))
        res_list.clear()
        m += 10
