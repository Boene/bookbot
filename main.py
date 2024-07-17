def main():

    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    sorted_list_holder = sort_list(text)
    #print(f"{num_words} were found in the document")
    #print(count_chars(text))
    #print(sort_list(text))

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{get_num_words(text)} words found in the document")
    print("")
    for entry in sorted_list_holder:
        if entry.isalpha() == True:
            print(f"The '{entry}' character was found {sorted_list_holder[entry]} times")
    print("--- End Report ---")


def get_book_text(book_path):
    with open(book_path, 'r') as book_text:
        return book_text.read()

def get_num_words(text):
    return(len(text.split()))

def count_chars(text):
    #chars_dict = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0}
    chars_dict = {}
    for word in text:
        lower_word = word.lower()
        if lower_word in chars_dict:
            chars_dict[lower_word] += 1
        else:
            chars_dict[lower_word] = 1
    return chars_dict

def sorter(dict):
    return dict["#"]
    
def sort_list(text):
    sorted_list = []
    sorted_dic = {}
    unsorted_dic = count_chars(text)
    for entry in unsorted_dic:
        sorted_list.append({"char" : entry , "#" : unsorted_dic[entry]})
    sorted_list.sort(reverse=True, key=sorter)
    for dic_entry in sorted_list:
        sorted_dic[dic_entry["char"]] = dic_entry["#"]
    return sorted_dic

if __name__ == "__main__":
    main()
