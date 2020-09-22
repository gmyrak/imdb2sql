from transformer import Writer, Reader

SRC = 'imdb_shot'
OUT = 'out'

src_title_basics = Reader(SRC + '/title.basics.tsv')

table_title = Writer(OUT + '/title.tsv',
                     ['id',
                'type',
                'primary_title',
                'original_title',
                'runtime_minutes',
                'start_year',
                'end_year',
                'is_adult'], 'title'
                     )

table_types = Writer(OUT + '/types.tsv', ['id', 'type'], 'types')
types_index = {}
types_id = 0

table_genres = Writer(OUT + '/genres.tsv', ['id', 'genre'], 'genres')
genres_index = {}
genres_id = 0

table_title_genres = Writer(OUT + '/title_genres.tsv',
                            ['title_id', 'genre_id'], 'title_genres')


for row in src_title_basics:
    item = {
        'id': row['tconst'],
        'primary_title': row['primaryTitle'],
        'original_title': row['originalTitle'],
        'is_adult': row['isAdult'],
        'start_year': row['startYear'],
        'end_year': row['endYear'],
        'runtime_minutes': row['runtimeMinutes']
    }

    ttype = row['titleType']
    if not ttype in types_index:
        types_id += 1
        types_index[ttype] = types_id
        table_types.insert({'id': types_id, 'type': ttype})

    item['type'] = types_index[ttype]

    if row['genres'] == '\\N':
        genres = []
    else:
        genres = row['genres'].split(',')
    for g in genres:
        if not g in genres_index:
            genres_id += 1
            genres_index[g] = genres_id
            table_genres.insert({'id': genres_id, 'genre': g})
        table_title_genres.insert({
            'title_id': row['tconst'],
            'genre_id': genres_index[g]
        })

    table_title.insert(item)


table_title.close()
table_types.close()