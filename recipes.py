def get_ingredients_list():
    # собираем словарь ингредиентов для каждого блюда
    i1 = ingredients[0]
    i2 = ingredients[1].replace(' ', '')
    i3 = ingredients[2].replace(' ', '')
    ingredient_dict = {'ingredient_name': i1, 'quantity': i2, 'measure': i3}
    dish_list.append(ingredient_dict)
    return dish_list


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:  # цикл по блюдам из списка
        for dish_name in cook_book.keys():
            if dish == dish_name:
                ingredient_list = cook_book.get(dish)
                for ingredient in ingredient_list:
                    quantity_in_list = int(ingredient['quantity']) * person_count
                    #  проверка наличия ингредиента в shop_list{}
                    if ingredient['ingredient_name'] not in shop_list.keys():
                        shop_dict = {'measure': ingredient['measure'], 'quantity': quantity_in_list}
                    else:
                        iin = ingredient['ingredient_name']
                        # iin - вспомогательная переменная, чтобы следующая формула выглядела полегче,
                        # суть название ингредиента
                        sum_quantity = quantity_in_list + shop_list.get(iin)['quantity']
                        shop_dict = {'measure': ingredient['measure'], 'quantity': sum_quantity}
                    shop_list[ingredient['ingredient_name']] = shop_dict
    print(shop_list)
    return


cook_book = {}
with open('recipes.txt', encoding="utf-8") as f:
    while True:
        # название блюда
        recipe_name = f.readline().strip()
        if not recipe_name:
            break
        # количество ингредиентов - счетчик для цикла разбора строк
        ingredients_number = int(f.readline().strip())
        # разбор строк с ингредиентами в словарь
        index = 0
        dish_list = []
        while index < ingredients_number:
            ingredients = f.readline().strip().split('|')
            # отдельная функция
            get_ingredients_list()
            index += 1
        # собираем словарь с рецептами
        cook_book[recipe_name] = dish_list
        f.readline()
# print(cook_book)

# get_shop_list_by_dishes()
get_shop_list_by_dishes(['Омлет', 'Омлет'], 2)
