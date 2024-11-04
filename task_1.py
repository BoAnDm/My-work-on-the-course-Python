# TODO Напишите функцию для поиска индекса товара
def find_index_item (list_, item):
    index = 0
    for i in list_:  # нахождение индекса
        if item == i:
            return index
        index += 1

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_index_item(items_list, find_item) # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
