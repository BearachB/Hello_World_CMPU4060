import string

def get_words():
    data_file = open("hare_and_tortoise.txt", "r")
    word_dict = {}  # start with an empty word dictionary
    for line in data_file:
        line = line.lower()
        line = line.split()
        for word in line:
            add_word(word,word_dict)
    data_file.close()
    return word_dict

def add_word(w,dict):
    for key in dict.keys():
        if key == w:
            dict[key] = dict[key] + 1
            return dict
        else:
            dict[w] = 1
            return dict

def create_html(word_dict):
    html = '<!DOCTYPE html>\ <html> <head lang="en"> <meta charset="UTF-8"> <title>Tag Cloud Generator</title> </head> <body> <div style="text-align: center; width: 15%; vertical-align: middle; font-family: arial; color: white; background-color:black; border:1px solid black">'
    for key in word_dict.keys():
        html += '<span style="font-size: '
        html += str(word_dict[key] * 10)
        html += 'px"> '
        html += key
        html += '</span>'

    html += '</div> </body> </html>'
    fo = open("output.html", "w")
    fo.write(html)

dict = get_words()
create_html(dict)
