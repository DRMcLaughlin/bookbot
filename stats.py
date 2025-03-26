def main(x):
    book_path = x
    book_text = get_book_text(x)
    print(book_text)

def get_book_text(path):
    with open(path) as b:
        book_text = b.read()
    return book_text

def get_word_count(path):
    words = get_book_text(path).split()
    num_words = len(words)
    return num_words
    #print(f"{num_words} words found in the document")

def repeating_characters(path):
    char_dict = {str(): int()}
    uni_chars = (get_book_text(path).lower())
    for char in uni_chars:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sorted_dict(path):
    char_dict = repeating_characters(path)
    dict_list = [{"character": char, "count": count} for char, count in char_dict.items()]
    dict_list.sort(reverse=True, key=lambda x: x["count"])
    return dict_list

def formatted_output(path):
    sorted_dict_list = sorted_dict(path)
    formatted_output = ""
    for item in sorted_dict_list:
        formatted_output += f"{item['character']}: {item['count']}\n"
    return formatted_output
    
    
def main(x):
    book_path = x
    book_text = get_book_text(x)
    print(book_text)

#print(formatted_output("books/frankenstein.txt"))
#print(sorted_dict("books/frankenstein.txt"))
        




