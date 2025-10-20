from stats import get_book_text, get_num_words, get_character_count, build_char_list, sort_on
import sys

print(sys.argv)
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else: 

    def main():
        print(f"============ BOOKBOT ============")
        


        path_to_file = sys.argv[1] #"books/frankenstein.txt"
        print(sys.argv)
        text = get_book_text(path_to_file)
        num_words = get_num_words(text)
        
        print(f"Analyzing book found at {path_to_file}")

        print(f"----------- Word Count ----------")

        print(f"Found {num_words} total words")

        print(f"--------- Character Count -------")

        characters = get_character_count(text)
        #for char, num in characters.items():
        #    print(f"'{char}': {num}")

        items = build_char_list(characters)
        items.sort(key=sort_on, reverse=True)
        for it in items:
            print(f"{it['char']}: {it['num']}")
        
        print(f"============= END ===============")

        
        
        
    if __name__ == "__main__":
        main()