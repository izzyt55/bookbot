def count_number_of_words(book_contents):
    num_of_words = 0
    book_contents_each_word = book_contents.split()
    for word in book_contents_each_word:
        num_of_words += 1
    return num_of_words

def num_of_characters(book_contents):
    character_dict = {}
    book_contents_lowercase = book_contents.lower()
    for char in book_contents_lowercase:
        if char in character_dict:
            character_dict[char] += 1
        else:
            total_characters = 0
            character_dict[char] = total_characters + 1
    # add code to create a new dictionary containing character_dict, but adding 
    # the keys "char" and "num"...this should give the sort function the ability
    # to sort based on "num" once working

    return character_dict

def sorted_list(character_dict):
    return character_dict['']