def inputData():# считывание входных данных из файла
    branch = []
    with open('input.txt', 'r', encoding = 'utf8') as file:
        count = int(file.readline())
        for i in range(count):
            data = list(map(int, file.readline().split()))
            branch.append(data)
    return branch, count

def search(branch, count):  # проверка на сбалансированность дерева
    result = []
    lengthAnd = {}
    length = list(reversed(range(len(branch))))
    for i in length:    # перебор по элементам из массива (их номера)
        if branch[i][1] == 0 and branch[i][2] == 0: #если элемент лист
            lenBranch = 1 # высота
            agreement = 0 # балансировка
            lengthAnd[i+1] = (lenBranch, agreement)# запись в словарь для использования
            result.append(0)    # запись балансировки как конечный результат дял этого элемента
        else:   # проверка следующих элементов
            if branch[i][1] == 0:
                hight1 = 0
            else:
                element1 = lengthAnd[branch[i][1]]
                hight1 = element1[0]    # высота
            if branch[i][2] == 0:
                hight2 = 0
            else:
                element2 = lengthAnd[branch[i][2]]
                hight2 = element2[0]

            agreement = hight2 - hight1 # вычисление балансировки
            lenBranch = max(hight1, hight2) + 1 # высота текущего узла
            result.append(agreement) # запись результата текущего элемента
            lengthAnd[i+1] = (lenBranch, agreement) # запись в словарь для использования
    return reversed(result), lengthAnd

def balans(branch, length): # балансировка дерева
    check = length[branch[0][2]][1] # проверка балансировки правого ребёнка
    result = []
    if check == -1: # выполнить большой левый поворот
        rightIndex = branch[0][2]-1
        leftOfRight = branch[rightIndex][1]-1 # елемент, который необходимо постивить в корень дерева
        # находим детей самого левого ребёнка в первом узле правого ребёнка
        left = branch[leftOfRight][1]
        right = branch[leftOfRight][2]

        #производим балансировку
        branch.insert(0, branch[leftOfRight])
        del branch[leftOfRight+1]
        # обновляем сылки для сбалансированного дерева
        branch[0][1], branch[0][2] = 2, branch[1][2]+1
        branch[branch[0][1]-1][2], branch[branch[0][2]-1][1] = left, right

        # отпрвляем данные для обновления сылок с учетом сдвига в массиве
        branch = checkData(branch, leftOfRight)

        #print(branch)
    else:
        # производим малый левый поворот, аналогично с большим левым поворотом
        rightIndex = branch[0][2] - 1 # с право
        leftOfRight = branch[rightIndex][1] - 1

        branch.insert(0, branch[rightIndex])
        del branch[rightIndex+1]

        branch[0][1], branch[1][2] = 2, leftOfRight+1

        branch = checkData(branch, rightIndex)

    return branch

def checkData(branch, data):    # функция обнавления сылок на дочерние элементы в дареве АВЛ
    for num, i in enumerate(branch[1:data]):
        for num1, j in enumerate(i[1::]):
            if j < data + 1 and j != 0 :
                branch[num + 1][num1 + 1] = j + 1
    return branch

def printResult(result,count): # вывод в файл конечного результата
    with open('output.txt', 'w', encoding = 'utf8') as file:
        file.write(str(count)+'\n')
        for i in result:
            file.write(' '.join(list(map(str, i))))
            file.write('\n')

def main():
    branch, count = inputData()
    result, length = search(branch, count)
    result = balans(branch, length)

    printResult(result, count)


if __name__ == '__main__':
    main()