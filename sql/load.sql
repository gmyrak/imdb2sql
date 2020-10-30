
load data infile 'D:/Projects/Python/imdb2sql/out/ref_types.tsv' into table ref_types ignore 1 lines;
load data infile 'D:/Projects/Python/imdb2sql/out/ref_genres.tsv' into table ref_genres ignore 1 lines;
load data infile 'D:/Projects/Python/imdb2sql/out/ref_attributes.tsv' into table ref_attributes ignore 1 lines;
load data infile 'D:/Projects/Python/imdb2sql/out/title.tsv' into table title ignore 1 lines;
load data infile 'D:/Projects/Python/imdb2sql/out/lnk_title_genres.tsv' into table lnk_title_genres ignore 1 lines;
load data infile 'D:/Projects/Python/imdb2sql/out/episode.tsv' into table episode ignore 1 lines;
load data infile 'D:/Projects/Python/imdb2sql/out/ref_lang.tsv' into table ref_lang ignore 1 lines;
load data infile 'D:/Projects/Python/imdb2sql/out/i18n.tsv' into table i18n ignore 1 lines;
load data infile 'D:/Projects/Python/imdb2sql/out/lnk_i18n_attributes.tsv' into table lnk_i18n_attributes ignore 1 lines;
load data infile 'D:/Projects/Python/imdb2sql/out/lnk_i18n_types.tsv' into table lnk_i18n_types ignore 1 lines;

load data infile 'D:/Projects/Python/imdb2sql/out/person.tsv' into table person ignore 1 lines;
load data infile 'D:/Projects/Python/imdb2sql/out/ref_profession.tsv' into table ref_professions ignore 1 lines;
load data infile 'D:/Projects/Python/imdb2sql/out/lnk_person_profession.tsv' into table lnk_person_profession ignore 1 lines;
load data infile 'D:/Projects/Python/imdb2sql/out/lnk_person_know.tsv' into table lnk_person_know ignore 1 lines;

load data infile 'D:/Projects/Python/imdb2sql/out/title_crew.tsv' into table title_crew ignore 1 lines;