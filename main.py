from stats import count_number_of_words
from stats import num_of_characters
from stats import sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    book_contents = get_book_text("books/frankenstein.txt")
    total_words = count_number_of_words(book_contents)
    total_characters = num_of_characters(book_contents)

    def sort_on(items):
        return items["sum"]

    sorted_total_characters = sorted_list(total_characters)
    sorted_total_characters.sort(reverse=True, key=sort_on)

    def report():
        
        count = 0
        for item in sorted_total_characters:
            for key in item:
                if item['char'].isalpha():
                    print(f"{item['char']}: {item['sum']}")
                    count += 1

    
    print("========= BOOKBOT =========\n"
    "Analyzing book found at books/frankenstein.txt...\n" \
        "----- Word Count -----")
    print(f"Found {total_words} total words")
    print("----- Character Count -----")
    print(report())
    print("========== END ==========")

main()