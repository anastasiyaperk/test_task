#Тестовое задание Napoleon IT School . Вариант 2
def get_array(array_size):
    array = []
    for i in range(array_size):
        x = int(input())
        array.append(x)
    return array

def even_array(array):
    even_arr=[x for x in array if x%2==0]
    for i in range(len(even_arr)-1 , 0 , -1):
        for j in range(i):
            if even_arr[j]>even_arr[j+1]:
                temp = even_arr[j]
                even_arr[j]=even_arr[j+1]
                even_arr[j+1]=temp
    return even_arr

def odd_array(array):
    odd_arr=[x for x in array if x%2==1]
    for i in range(len(odd_arr)-1 , 0 , -1):
        for j in range(i):
            if odd_arr[j]<odd_arr[j+1]:
                temp = odd_arr[j]
                odd_arr[j]=odd_arr[j+1]
                odd_arr[j+1]=temp
    return odd_arr

if __name__ =='__main__':
    while True:
        array_size = int(input('Введите N - размер массива(2 ≤ N ≤ 10000):'))
        if array_size > 10000 or array_size < 2:
            print('Ошибка, недопустимый размер массива. Повторите ввод...')
        else:
            break
    print('Введите элементы массива:')
    array = get_array(array_size)

    odd_arr = odd_array(array)
    even_arr = even_array(array)
    print('Результат сортировки:  ', even_arr+odd_arr)
