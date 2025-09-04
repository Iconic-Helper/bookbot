from stats import num_of_words
from stats import num_of_char
from stats import convert
import sys
if len(sys.argv) == 2:
   path = sys.argv[1]
else:
    print ("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
def get_book_text(filepath):
    with open (filepath) as f:
        books = f.read()
    return books



def main():
    book_contents = get_book_text(path)
    print(f"============ BOOKBOT ===========")
    print(f"Analyzing book found at {path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_of_words(book_contents)} total words")
    print(f"--------- Character Count -------")
    char_dict = num_of_char(book_contents)
    sorted_chars = convert(char_dict)
    for char_info in sorted_chars:
        character = char_info["char"]
        if character.isalpha():  
            count = char_info["num"]
            print(f"{character}: {count}")
    print ("============= END ===============")
        

main()