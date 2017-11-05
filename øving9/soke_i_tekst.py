import re
#a
def read_from_file(filename):
    try:
        with open(filename, "r") as f:
            print("Start of file:\n",f.read())
    except:
        print("File not found!")

#b
def remove_symbols(text):
    return re.sub(r'([^\s\w]|_)+', '', text).lower()


#c
def count_words(filename):
    try:
        words = []
        full = {}
        with open(filename, "r") as f:
            for line in f:
                new_line = re.split("[; ,\*\n]", remove_symbols(line))
                for i in new_line:
                    if(i != ""):
                        words.append(i)

        for word in words:
            if(word not in full):
                full[word] = 1
            else:
                full[word] += 1
        for word, val in full.items():
            print(word,val)
    except:
        print("File not found!")
#a
#read_from_file("meme.txt")
#
#b
#remove_symbols("heihei@ hade")
#
#c
count_words("BIBLE.txt")
