#gold coin = [name, count, weight, type]
def add_to_inventory(item, inventory):
    if item in inventory:
        item[1] += 1
    else:
        inventory.append(item)

    return inventory


def display_inventory_items(inventory):
    for item in inventory:
        print (item)


def print_table(inventory):
    print("INVENTORY")
    #name, type, weight
    print("{:>1}".format("Item name |"), "{:>5}".format("Count |"), "{:>5}".format("Weight |"), "{:>5}".format("Type |"))
    print("_______________________________")
    display_inventory_items(str(inventory))
    print("_______________________________")

def main():
    inventory = []
    gold_coin = ['Gold Coin', 1, 0.1, 'Collectable']
    axe = ['Axe', 1, 10, 'Weapon']
    add_to_inventory(gold_coin, inventory)
    add_to_inventory(axe, inventory)
    #add_to_inventory('armor', inventory)
    print_table(inventory)

if __name__ == '__main__':
    main()
