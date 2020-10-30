from transformer import Reader, Table, Dictionary

SRC = 'imdb_shot'
OUT = 'out'
NULL = '\\N'

#TT = open('tconsts', 'rb')
#tconsts = pickle.load(TT)
#TT.close()
#print('Load Set')
# -------------------------------------------------------
src_names = Reader(SRC + '/name.basics.tsv')
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

    if row['primaryProfession']:
        for p in row['primaryProfession'].split(','):
            lnk_person_profession.insert({
                'person_id': item['id'],
                'profession_id': ref_profession.add(p)
            })

    if row['knownForTitles'] != NULL:
        for t in row['knownForTitles'].split(','):
            lnk_person_know.insert({'person_id': item['id'], 'title_id': t})

# -------------------------------------------------------
Table.close_all()
