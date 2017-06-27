import operator
import imp
reports = imp.load_source("reports", "/home/akos/codeLUL/si3/pbwp-3rd-si-game-statistics-AkosPutnoki/reports.py")


def text_conversion(file_name):
    path = "/home/akos/codeLUL/si3/pbwp-3rd-si-game-statistics-AkosPutnoki/%s" % file_name
    textlist = []
    with open(path) as text:
        for line in text:
            element = line.rstrip().split("\t")
            textlist.append(element)

    return textlist


def get_most_played(file_name):
    amounts_sold = {}
    for lists in text_conversion(file_name):
        amounts_sold[lists[0]] = float(lists[1])
    sorted_amounts = sorted(amounts_sold.items(), key=operator.itemgetter(1))

    return sorted_amounts[-1][0]


def sum_sold(file_name):
    sold_total = 0
    for lists in text_conversion(file_name):
        sold_total += float(lists[1])

    return sold_total


def get_selling_avg(file_name):
    average = sum_sold(file_name) / count_games(file_name)

    return average


def count_longest_title(file_name):
    title_length = {}
    for lists in text_conversion(file_name):
        title_length[lists[0]] = len(lists[0])
    sorted_length = sorted(title_length.items(), key=operator.itemgetter(1))

    return sorted_length[-1][1]


def get_date_avg(file_name):
    date_sum = 0
    for lists in text_conversion(file_name):
        date_sum += int(lists[2])
    date_average = round(date_sum / count_games(file_name))

    return date_average


def get_game(file_name, title):
    for lists in text_conversion(file_name):
        if lists[0] == title:
            lists[1], lists[2] = float(lists[1]), int(lists[2])
            return lists


def count_grouped_by_genre(file_name):
    genre_count = {}
    for lists in text_conversion(file_name):
        if lists[3] in genre_count:
            genre_count[lists[3]] += 1
        else:
            genre_count[lists[3]] = 1

    return genre_count


def get_date_ordered(file_name):
    title_year = {}
    for lists in text_conversion(file_name):
        title_year[lists[0]] = int(lists[2])
    date_ordered_list = [item[0] for item in sorted(title_year.items(), key=lambda kv: (-kv[1], kv[0]))]

    return(date_ordered_list)
