from reports import *


def export_text(input_file, export_file):
    export_list = [get_most_played(input_file),
                   sum_sold(input_file),
                   get_selling_avg(input_file),
                   count_longest_title(input_file),
                   get_date_avg(input_file),
                   get_game(input_file, "Terraria"),
                   count_grouped_by_genre(input_file),
                   get_date_ordered(input_file)]
    path = "/home/akos/codeLUL/si3/pbwp-3rd-si-game-statistics-AkosPutnoki/part2/%s" % export_file
    with open(path, "w") as text:
        for item in export_list:
            text.write(str(item)+"\n")


export_text("game_stat.txt", "export.txt")
