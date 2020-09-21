f = open('imdb_shot/title.basics.tsv', 'r', encoding='utf-8')

while True:
    line = f.readline()
    if line:
        print(line, end='')
    else:
        #line1 = f.readline()
        break