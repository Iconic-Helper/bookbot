
def num_of_words(book_contents):
    words = book_contents.split()
    number_of_words = len(words)
    return number_of_words

def num_of_char(book_contents):
    l_char = book_contents.lower()
    num_char ={}
    for char in l_char:
        if char not in num_char:
            num_char[char]= 1
        else:
            num_char[char] += 1
    return num_char
def convert(num_char):
    list_convert=[]
    for char in num_char:
        sorted ={
            "char" : char ,"num": num_char[char]
        }
        list_convert.append(sorted)
    list_convert.sort(reverse=True, key=sort_char)
    return list_convert
def sort_char(dict):
    return dict["num"]
    

    