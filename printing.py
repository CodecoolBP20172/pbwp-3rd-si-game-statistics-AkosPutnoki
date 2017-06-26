from reports import *


def printint_text(file_name):
    print_list = [count_games(file_name),
                  decide(file_name, 1999),
                  get_latest(file_name),
                  count_by_genre(file_name, "RPG"),
                  get_line_number_by_title(file_name, "Terraria"),
                  sort_abc(file_name),
                  get_genres(file_name),
                  when_was_top_sold_fps(file_name)]

    for item in print_list:
        print(item)


printint_text("game_stat.txt")
