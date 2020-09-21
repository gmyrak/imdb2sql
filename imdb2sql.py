from transformer import Writer, Reader

title_basics = Reader('imdb_shot/title.basics.tsv')

title = Writer('out/title.tsv',
               ['id', 'type', 'primary_title', 'original_title', 'is_adult', 'start_year', 'end_year', 'runtime_minutes'],
                'title'
               )

for row in title_basics:
    item = {
        'id': row['tconst'],
        'type': row['titleType'],
        'primary_title': row['primaryTitle'],
        'original_title': row['originalTitle'],
        'is_adult': row['isAdult'],
        'start_year': row['startYear'],
        'end_year': row['endYear'],
        'runtime_minutes': row['runtimeMinutes']
    }
    title.insert(item)


title.close()