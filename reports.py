import operator


def text_conversion(file_name):
    path = "/home/akos/codeLUL/si3/pbwp-3rd-si-game-statistics-AkosPutnoki/%s" % file_name
    textlist = []
    with open(path) as text:
        for line in text:
            element = line.split("\t")
            textlist.append(element)

    return textlist


def count_games(file_name):
    game_count = 0
    for game in text_conversion(file_name):
        game_count += 1

    return game_count


def decide(file_name, year):
    decision = False
    for lists in text_conversion(file_name):
        for item in lists:
            if str(year) in item:
                decision = True

    return decision


def get_latest(file_name):
    game_year = {}
    for lists in text_conversion(file_name):
        game_year[lists[0]] = int(lists[2])
    sorted_dict = sorted(game_year.items(), key=operator.itemgetter(1))

    return sorted_dict[-1][0]


def count_by_genre(file_name, genre):
    game_count = 0
    for lists in text_conversion(file_name):
        if genre in lists:
            game_count += 1

    return game_count


def get_line_number_by_title(file_name, title):
    game_number = {}
    i = 1
    for lists in text_conversion(file_name):
        game_number[lists[0]] = i
        i += 1
    if title not in game_number.keys():
        raise ValueError("No such title in the file.")

    return game_number[title]


def sort_abc(file_name):
    abc_list = []
    for lists in text_conversion(file_name):
        abc_list.append(lists[0])

    return sorted(abc_list)


def get_genres(file_name):
    genre_set = set()
    for lists in text_conversion(file_name):
        genre_set.add(lists[3])

    return sorted(genre_set, key=str.lower)


def when_was_top_sold_fps(file_name):
    fps_year = {}
    for lists in text_conversion(file_name):
        if lists[3] == "First-person shooter":
            fps_year[int(lists[2])] = float(lists[1])
    if fps_year == {}:
        raise ValueError("No such genre in the input file.")
    sorted_dict = sorted(fps_year.items(), key=operator.itemgetter(1))

    return sorted_dict[-1][0]
