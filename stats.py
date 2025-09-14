def get_num_words(text):
    return len(text.split())


def get_stats(text):
    text_lower = text.lower()
    counts = {}

    for char in text_lower:
        if "a" <= char <= "z":
            counts[char] = counts.get(char, 0) + 1
    return counts


def sort_on(dict):
    return dict["num"]


def sort_dict(dict):
    dict_list = []
    for key, value in dict.items():
        dict_list.append({"char": key, "num": value})

    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
