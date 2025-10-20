def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

################################

def get_num_words(text):
    return len(text.split())

################################

def get_character_count(text):
    characters = {}
    lower_case = text.lower()
    for letter in lower_case:
        if letter in characters:
            characters[letter] += 1
        else:
            characters[letter] = 1
    return characters

   
###########################################
#### With help from boots #################
###########################################

def build_char_list(char_counts):
    items = []
    for ch, n in char_counts.items():
        if ch.isalpha():
            items.append({"char": ch, "num": n})
    return items

def sort_on(item):
    return item["num"]