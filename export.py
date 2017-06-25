import reports as r


def export_text(file_name):
    export_list = [r.count_games("game_stat.txt"), r.decide("game_stat.txt", 1999),
                   r.get_latest("game_stat.txt"), r.count_by_genre("game_stat.txt", "RPG"),
                   r.get_line_number_by_title("game_stat.txt", "Terraria"),
                   r.sort_abc("game_stat.txt"), r.get_genres("game_stat.txt"),
                   r.when_was_top_sold_fps("game_stat.txt")]
    path = "/home/akos/codeLUL/si3/pbwp-3rd-si-game-statistics-AkosPutnoki/%s" % file_name
    with open(path, "w") as text:
        for item in export_list:
            text.write(str(item)+"\n")


export_text("export.txt")
