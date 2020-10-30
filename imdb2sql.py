from transformer import Table, Reader, Dictionary
import re

SRC = 'imdb'
OUT = 'out'
NULL = '\\N'
SEP2 = ''

LIMIT = 100000

tconsts = set()
nconsts = set()

src_title_basics = Reader(SRC + '/title.basics.tsv', LIMIT)


tab_title = Table('title',
                  [
                      'id',
                      'type',
                      'primary_title',
                      'original_title',
                      'runtime_minutes',
                      'start_year',
                      'end_year',
                      'is_adult'
                  ]
                  )

ref_types = Dictionary('ref_types', ['id', 'type'])
ref_genres = Dictionary('ref_genres', ['id', 'genre'])
lnk_title_genres = Table('lnk_title_genres', ['title_id', 'genre_id'])

for row in src_title_basics:

    item = {
        'id': row['tconst'],
        'primary_title': row['primaryTitle'],
        'original_title': row['originalTitle'],
        'is_adult': row['isAdult'],
        'start_year': row['startYear'],
        'end_year': row['endYear'],
        'runtime_minutes': row['runtimeMinutes'],
        'type': ref_types.add(row['titleType'])
    }

    #if row['titleType'] == 'tvEpisode' and re.match(r'Episode #', row['primaryTitle']):
    #    continue


    if row['genres'] != NULL:
        for g in row['genres'].split(','):
            lnk_title_genres.insert({
                'title_id': row['tconst'],
                'genre_id': ref_genres.add(g)
            })

    if item['id'] not in tconsts:
        tconsts.add(item['id'])
        tab_title.insert(item)


src_episode = Reader(SRC + '/title.episode.tsv', LIMIT)

episode_fields = [
    'episode_id',
    'parent_id',
    'episode_number',
    'season_number'
]

table_episode = Table('episode', episode_fields)
table_episode_error = Table('episode_error', episode_fields, 'err')

for row in src_episode:
    item = {
        'episode_id': row['tconst'],
        'parent_id': row['parentTconst'],
        'episode_number': row['episodeNumber'],
        'season_number': row['seasonNumber']
    }
    if item['episode_id'] in tconsts and item['parent_id'] in tconsts:
        table_episode.insert(item)
    else:
        if item['episode_id'] not in tconsts and item['parent_id'] not in tconsts:
            tag = 'B'
        elif item['episode_id'] not in tconsts:
            tag = 'E'
        else:
            tag = 'S'
        item['tag'] = tag
        table_episode_error.insert(item)

src_i18n = Reader(SRC + '/title.akas.tsv', LIMIT)

tab_i18n = Table('i18n',
                 ['id',
                  'title_id',
                  'ordering',
                  'title',
                  'region',
                  'language',
                  'is_original'
                  ]
                 )

tab_i18n.auto_increment = {'id': 0}

i18n_errors = Table('i18n_error', ['title_id'], 'err')
ref_lang = Dictionary('ref_lang', ['id', 'code'])

lnk_i18n_types = Table('lnk_i18n_types', ['i18n_id', 'type_id'])

ref_attributes = Dictionary('ref_attributes', ['id', 'attribute'])
lnk_i18n_attributes = Table('lnk_i18n_attributes', ['i18n_id', 'attribute_id'])

for row in src_i18n:
    if row['titleId'] in tconsts:
        item = {
            'title_id': row['titleId'],
            'ordering': row['ordering'],
            'title': row['title'],
            'region': ref_lang.add(row['region']),
            'language': ref_lang.add(row['language']),
            'is_original': row['isOriginalTitle']
        }

        item = tab_i18n.insert(item)

        if row['types'] != NULL:
            for t in row['types'].split(SEP2):
                lnk_i18n_types.insert({
                    'i18n_id': item['id'],
                    'type_id': ref_types.add(t)
                })

        if row['attributes'] != NULL:
            for a in row['attributes'].split(SEP2):
                lnk_i18n_attributes.insert({
                    'i18n_id': item['id'],
                    'attribute_id': ref_attributes.add(a)
                })

    else:
        i18n_errors.insert({'title_id': row['titleId']})


# --- Actors ---

src_names = Reader(SRC + '/name.basics.tsv', LIMIT)
tab_person = Table('person', ['id', 'name', 'birth_year', 'death_year'])
ref_profession = Dictionary('ref_profession', ['id', 'profession'])
lnk_person_profession = Table('lnk_person_profession', ['person_id', 'profession_id'])
lnk_person_know = Table('lnk_person_know', ['person_id', 'title_id'])

for row in src_names:
    item = {
        'id': row['nconst'],
        'name': row['primaryName'],
        'birth_year': row['birthYear'],
        'death_year': row['deathYear']
    }
    tab_person.insert(item)
    nconsts.add(item['id'])

    if row['primaryProfession']:
        for p in row['primaryProfession'].split(','):
            lnk_person_profession.insert({
                'person_id': item['id'],
                'profession_id': ref_profession.add(p)
            })

    if row['knownForTitles'] != NULL:
        for t in row['knownForTitles'].split(','):
            if t in tconsts:
                lnk_person_know.insert({'person_id': item['id'], 'title_id': t})


src_crew = Reader(SRC + '/title.crew.tsv', LIMIT)
tab_title_crew = Table('title_crew', ['title_id', 'person_id', 'role'])

for row in src_crew:
    if not row['tconst'] in tconsts:
        continue
    if row['directors'] != NULL:
        for d in row['directors'].split(','):
            if not d in nconsts:
                continue
            tab_title_crew.insert({
                'title_id': row['tconst'],
                'person_id': d,
                'role': 'Director'
            })

    if row['writers'] != NULL:
        for w in row['writers'].split(','):
            if not w in nconsts:
                continue
            tab_title_crew.insert({
                'title_id': row['tconst'],
                'person_id': w,
                'role': 'Writer'
            })


Table.close_all()