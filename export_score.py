import hero_creator
import hero_inventory

def export_statistics(filename, hero_stats, inventory, time):
    name = hero_stats[0]
    total_coins = hero_inventory.total_coins(inventory)
    hero_statistics = [name, total_coins]
    with open (filename, 'a') as hall_of_fame:
        hall_of_fame.write("Hero name: %s, " % name)
        hall_of_fame.write("Time played: %.2f,  " % time)
        hall_of_fame.write("Gold gathered: %s \n" % total_coins)

def main():
    hero_stats = ["Achilles"]
    export_statistics('hallOfFame.txt', hero_stats)

if __name__ == '__main__':
    main()
