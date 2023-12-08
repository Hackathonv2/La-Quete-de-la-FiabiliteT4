
def main():
    result : str = ""
    res_val : int = 1000
    tmp : int = 0
    file : list[list[str]] | None = ["", ""]
    for i in range(2):
        file[i] = input().split(" ")
    
    for i in range(2):
        tmp = int(file[i][1]) * (int(file[i][2]) + int(file[i][3]))
        if (tmp < res_val):
            result = file[i][0]
            res_val = tmp
    print(result)
    return 0

if __name__ == '__main__':
    exit(main())