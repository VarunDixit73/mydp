if __name__ == '__main__':
    list = []
    list_2 = []
    for _ in range(0,int(input())):
        name = input()
        score = float(input())
        list.append([name,score])
        
    list.sort(key = lambda x: x[1])
    for x in range(1, len(list)):
        if(list[x][1] != list[x-1][1]):
            score = list[x][1]
            break
    list = sorted(list);
    for x in range(len(list)):
        if(list[x][1] == score):
            print(list[x][0])