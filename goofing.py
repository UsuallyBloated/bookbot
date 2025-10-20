
def sorted_characters(characters):
    #return characters["num"]
    sorted_list = []
    for char, num in characters.items():
        sorted_list = [
            {"char": char, "num": num},
        ]
    return sorted_list
  