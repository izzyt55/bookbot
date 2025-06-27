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

    print(f"{total_words} words found in the document")

    total_characters = num_of_characters(book_contents)
    print(total_characters)

    sorted_total_characters = total_characters.sort(reverse=True, key=sorted_list(total_characters))
    print(sorted_total_characters)

main()