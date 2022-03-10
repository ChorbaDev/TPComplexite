from experimentateur import test
import os

if __name__ == '__main__':
    res_list = []
    m = 10
    for i in range(1, 11):
        filePath="res-" + str(m) + ".dat"
        if os.path.exists(filePath):
            os.remove(filePath)
        with open(filePath, "a") as file:
            for p in range(1, m + 1):
                res = ' '.join(str(e) for e in test(p, m))
                file.write(res+"\n")
        res_list.clear()
        m += 10
