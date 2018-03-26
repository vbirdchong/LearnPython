
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
from collections import OrderedDict

def clean_input(input):
    input = re.sub('\n+', " ", input)
    input = re.sub(r'\[[0-9]*\]', "", input)
    input = re.sub(' +', " ", input)
    input = input.upper()
    input = bytes(input, "UTF-8")
    input = input.decode("ascii", "ignore")
    
    cleaned_input = []
    input = input.split(' ')

    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a') or (item.lower() == 'i'):
            cleaned_input.append(item)

    return cleaned_input


def ngrams(input, n):
    input = clean_input(input)
    output = {}
    for i in range(len(input) - n + 1):
        t = " ".join(input[i : i+n])
        if t not in output:
            output[t] = 0
        output[t] += 1
    return output

def save_to_file(data):
    with open('data.txt', 'w+') as f:
        for d in data:
            f.write(d + ', ' + str(data[d]) + '\n')

def main():
    URL = "http://en.wikipedia.org/wiki/Python_(programming_language)"
    html = urlopen(URL)
    bsObj = BeautifulSoup(html, "lxml")

    content = bsObj.find("div", {"id": "mw-content-text"}).get_text()
    ngram = ngrams(content, 2)
    ngram = OrderedDict(sorted(ngram.items(), key=lambda t: t[1], reverse=True))
    print(ngram)
    print(type(ngram))
    print('2-gram count is: ' + str(len(ngram)))
    save_to_file(ngram)

if __name__ == '__main__':
    main()