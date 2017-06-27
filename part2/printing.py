from reports import *


def printint_text(file_name):
    print_list = [get_most_played(file_name),
                  sum_sold(file_name),
                  get_selling_avg(file_name),
                  count_longest_title(file_name),
                  get_date_avg(file_name),
                  get_game(file_name, "Terraria"),
                  count_grouped_by_genre(file_name),
                  get_date_ordered(file_name)]

    for item in print_list:
        print(item)


printint_text("game_stat.txt")
