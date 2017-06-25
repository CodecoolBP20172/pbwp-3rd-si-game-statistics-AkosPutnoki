import reports as r


def printint_text():
    print_list = [r.count_games("game_stat.txt"), r.decide("game_stat.txt", 1999),
                  r.get_latest("game_stat.txt"), r.count_by_genre("game_stat.txt", "RPG"),
                  r.get_line_number_by_title("game_stat.txt", "Terraria"),
                  r.sort_abc("game_stat.txt"), r.get_genres("game_stat.txt"),
                  r.when_was_top_sold_fps("game_stat.txt")]
    for item in print_list:
        print(item)

printint_text()
