
def add_to_inventory(item, inventory):
    if item in inventory:
        inventory[item] += 1
    else:
        inventory[item] = 1

    return inventory


def display_inventory_items(inventory):
    for key, value in inventory.items():
        print ((" {} : {} ").format(key, value))

def print_table(inventory):
    print("INVENTORY")
    print("_____________________")
    display_inventory_items(inventory)
    print("_____________________")

def main():
    inventory = {'gold coin' : 2}
    add_to_inventory('gold coin', inventory)
    add_to_inventory('axe', inventory)
    add_to_inventory('armor', inventory)
    print_table(inventory)

if __name__ == '__main__':
    main()
