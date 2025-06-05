import sys 

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

file_name = sys.argv[1]

from stats import count_words, count_characters, structure

def get_book_text(file_path):
    file_contents = None
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

text = get_book_text(file_name)
num_words = count_words(text)
char_counts=count_characters(text)
sorted= structure(char_counts)

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for ch, count in sorted [:20]:
        print(f"{ch}: {count}")

main()
