from transformer import Reader
import pickle

SRC = 'imdb'
OUT = 'out'

src_title_basics = Reader(SRC + '/title.basics.tsv')
tconsts = set()

for row in src_title_basics:
    tconsts.add(row['tconst'])

F = open('tconsts', 'wb')
pickle.dump(tconsts, F)
F.close()

