from transformer import Reader

src_i18n = Reader('imdb_shot/title.akas.tsv')

for r in src_i18n:
    print(r['isOriginalTitle'])


