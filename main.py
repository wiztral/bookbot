import sys
from stats import get_character_counts, get_sorted_character_counts, get_word_count

def get_book_text(file_path: str):
    file_content = None
    with open(file_path) as f:
        file_content = f.read()

    return file_content

def main():
    args = sys.argv

    if(len(args) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    content = get_book_text(args[1])
    word_count = get_word_count(content)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    character_counts = get_character_counts(content)
    sorted_character_counts = get_sorted_character_counts(character_counts)

    for item in sorted_character_counts:
        if(item["character"].isalpha()):
            print(f"{item["character"]}: {item["count"]}")


    print("============= END ===============")

main()
