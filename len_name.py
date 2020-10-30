from transformer import Table, Reader, Dictionary
import re

SRC = 'imdb'
OUT = 'out'
NULL = '\\N'
SEP2 = ''

lmax = 0
names = Reader(SRC + '/title.principals.tsv')
for row in names:
    l = len(row['job'])
    if l > lmax:
        lmax = l

print(lmax)

