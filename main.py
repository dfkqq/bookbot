def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        counter = count_words(file_contents)
        dict_number_of_letters = dict_letters(file_contents)
        checked = checking(dict_number_of_letters)
        new_list = convert(checked)
        new_list.sort(reverse=True, key=sort_on)
        print("--- Begin report ---")
        print(f"{counter} words found in the document")
        for item in new_list:
            print(f"The '{item['character']}' character was found {item['number']} times")
        print("--- End report ---")


def count_words(f:str):
    words = f.split()
    counter = 0
    for w in words:
        counter+=1
    return counter

def dict_letters(f:str):
    dict_letters = {}
    lower = f.lower()
    for l in lower:
        if l not in dict_letters:
            dict_letters[l] = 1
        elif l in dict_letters:
            dict_letters[l] +=1
    return dict_letters
def sort_on(d):
    return d["number"]

def convert(dict_:dict):
    new_list = []
    for d in dict_:
        dict_to_append = {"character":d,"number":dict_[d]}
        new_list.append(dict_to_append)
    return new_list

def checking(dict_):
    checked_dict = {item:dict_[item] for item in dict_ if item.isalnum()}
    return checked_dict







main()