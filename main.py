import matplotlib.pyplot as plt


def result_visualization(group_number: dict):
    """функция визуализации результата"""
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.ylabel('Количество клиентов')
    plt.xlabel('Номер группы')
    plt.title(f'количество покупателей в группах при нумерации от {n_first_id} до {n_customers} включительно')
    for key, value in group_number.items():
        print(f'В группе номер {key} количество покупателей = {value}')
        ax.bar(key, value, color='blue')
    plt.show()


def sort_dict(group_number: dict):
    """функция сортировки словаря по возрастанию ключа(номера группы)"""
    group_number = dict(sorted(group_number.items(), key=lambda x: x[0]))
    return group_number


def group_customer_number(id_customer: int):
    """функция вычисляет номер группы клиента"""
    list_id_customer = list(map(int, list(str(id_customer))))
    return sum(list_id_customer)


def test_end_to_end_numbering(n_customers: int):
    """количество покупателей в группах при сквозной нумерации от 0 до n_customers включительно"""
    group_number = {}
    for customer in range(n_customers + 1):
        number = group_customer_number(customer)
        if number not in group_number:
            group_number[number] = 0
        group_number[number] += 1
    group_number = sort_dict(group_number)
    result_visualization(group_number)


def test_arbitrary_numbering(n_customers: int, n_first_id: int):
    """количество покупателей в группах при произвольной нумерации от n_first_id до n_customers включительно"""
    group_number = {}
    for customer in range(n_first_id, n_customers + 1):
        number = group_customer_number(customer)
        if number not in group_number:
            group_number[number] = 0
        group_number[number] += 1
    group_number = sort_dict(group_number)
    result_visualization(group_number)


if __name__ == '__main__':
    n_first_id = 0
    n_customers = int(input('Количество клиентов при сквозной нумерации : '))
    print()
    print('*' * 100)
    print()
    test_end_to_end_numbering(n_customers)
    print()
    print('*' * 100)
    print()
    n_customers = int(input('Количество клиентов при произвольно нумерации : '))
    n_first_id = int(input('Первый ID в последовательности : '))
    n_customers += n_first_id
    print()
    print('*' * 100)
    print()
    test_arbitrary_numbering(n_customers, n_first_id)
