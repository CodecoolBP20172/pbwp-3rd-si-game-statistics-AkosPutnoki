from reports import *


def export_text(input_file, export_file):
    export_list = [count_games(input_file),
                   decide(input_file, 1999),
                   get_latest(input_file),
                   count_by_genre(input_file, "RPG"),
                   get_line_number_by_title(input_file, "Terraria"),
                   sort_abc(input_file),
                   get_genres(input_file),
                   when_was_top_sold_fps(input_file)]
    path = "/home/akos/codeLUL/si3/pbwp-3rd-si-game-statistics-AkosPutnoki/%s" % export_file
    with open(path, "w") as text:
        for item in export_list:
            text.write(str(item)+"\n")


export_text("game_stat.txt", "export.txt")
