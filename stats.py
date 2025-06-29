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

    return character_dict

def sorted_list(character_dict):
    sorted_dictionary_list = []
    for char in character_dict:
        dict1 = {}
        dict1["char"] = char
        dict1["sum"] = character_dict[char]
        sorted_dictionary_list.append(dict1)
    
    return sorted_dictionary_list