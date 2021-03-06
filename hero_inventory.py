def collectable_item(item_name, count, weight, item_type):
    """Creates and returns dictionary with item_name as a key and list with item parameters as a value"""

    item_parameters = [count, weight, item_type]
    item_dict = {item_name: item_parameters}
    return item_dict


def add_to_inventory(inventory, item_name, count, weight, item_type, gathered_items=[]):
    """Add new item to players inventory or increases item count if item already gathered, returns updated inventory"""

    item_dict = collectable_item(item_name, count, weight, item_type)
    if inventory:
        for index in range(len(inventory)):
            for key in inventory[index]:
                if item_name == key:
                    inventory[index].get(item_name)[0] += 1
                    inventory[index].get(key)[1] = inventory[index].get(key)[0] * weight
                elif item_name not in gathered_items:
                    inventory.append(item_dict)
                    gathered_items.append(item_name)
    else:
        inventory.append(item_dict)
        gathered_items.append(item_name)

    return inventory


def total_weight(inventory):
    """Counts and returns total_weight of items in inventory"""

    total_weight = 0
    for index in range(len(inventory)):
        for key in inventory[index]:
            total_weight += inventory[index].get(key)[1]
    return(total_weight)


def total_coins(inventory):
    """Count and returns number of coins placed in inventory"""

    total_coins = 0
    for index in range(len(inventory)):
        for key in inventory[index]:
            if key == "Gold coin":
                return inventory[index].get(key)[0]


def display_inventory_items(inventory):
    """ Prints items contained in inventory"""

    for index in range(len(inventory)):
        for key in inventory[index]:
            count = inventory[index].get(key)[0]
            weight = inventory[index].get(key)[1]
            item_type = inventory[index].get(key)[2]
            print('{:9} {:8} {:8} {:1}'.format(key, count, weight, item_type))


def print_table(inventory):
    """Prints inventory in formatted way"""

    print("INVENTORY")
    print('{:13} {:8} {:8} {:1}'.format("Name", "Count", "Weight", "Type"))
    print("___________________________________________")
    display_inventory_items(inventory)
    print("___________________________________________")
    print("Total weight: %s / 100" % total_weight(inventory))


def main():

    inventory = []
    add_to_inventory(inventory, 'Gold coin', 1, 1, 'Collectable')
    add_to_inventory(inventory, 'Gold coin', 1, 1, 'Collectable')
    add_to_inventory(inventory, 'Gold coin', 1, 1, 'Collectable')
    add_to_inventory(inventory, 'Axe', 1, 1, 'Weapon')
    print(total_coins(inventory))

if __name__ == '__main__':
    main()
