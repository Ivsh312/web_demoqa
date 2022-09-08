class tmp:

    def __getitem__(self, item):
        menu_items_by_index = dict(zip([i for i in range(len(menu_items))], menu_items.values()))
        if isinstance(item, str):
            menu_item = menu_items.get(item)
        elif isinstance(item, int):
            menu_item = menu_items_by_index.get(item)
        else:
            raise TypeError(f'Unsaported type of menu_item {type(item)}')
        menu_item.click()

user = tmp()
print(user[1])