# TODO Напишите функцию для поиска индекса товара
def search_item(searched_list, item_to_search):
    return next((index for index, item in enumerate(searched_list) if item == item_to_search), None)


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = search_item(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
