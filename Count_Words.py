# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    handle = open(filename, 'r')
    msg = handle.readlines()
    return msg

def count_words():
    text = read_file_content("./story.txt")
    words_count = dict()
    for word in str(text).strip('[]').split():
        words_count[word] = words_count.get(word, 0) + 1
    return words_count

print(count_words())
