import hero_inventory


def export_statistics(filename, hero_stats, inventory, played_time):
    """Exports game statistics to file"""

    player_name = hero_stats[0]
    total_coins = hero_inventory.total_coins(inventory)
    hero_statistics = [player_name, total_coins]

    with open(filename, 'a') as hall_of_fame:
        hall_of_fame.write("Hero name: %s, " % player_name)
        hall_of_fame.write("Time played: %.2f,  " % played_time)
        hall_of_fame.write("Gold gathered: %s \n" % total_coins)
