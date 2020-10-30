create table person
(
    id         varchar(10) not null
        primary key,
    name       varchar(50) not null,
    birth_year int         null,
    death_year int         null
);

create table ref_attributes
(
    id        int         not null
        primary key,
    attribute varchar(60) not null
);

create table ref_genres
(
    id    int         not null
        primary key,
    genre varchar(20) not null,
    constraint genres_genre_uindex
        unique (genre)
);

create table ref_lang
(
    id   int        not null
        primary key,
    code varchar(5) not null
);

create table ref_professions
(
    id         int         not null
        primary key,
    profession varchar(50) not null
);

create table lnk_person_profession
(
    person_id     varchar(10) null,
    profession_id int         null,
    constraint lnk_person_profession_person_id_fk
        foreign key (person_id) references person (id),
    constraint lnk_person_profession_ref_professions_id_fk
        foreign key (profession_id) references ref_professions (id)
);

create table ref_types
(
    id   int         not null
        primary key,
    type varchar(20) not null,
    constraint types_type_uindex
        unique (type)
);

create table title
(
    id              varchar(10)  not null comment 'alphanumeric unique identifier of the title'
        primary key,
    type            int          not null comment 'the type/format of the title (e.g. movie, short, tvseries, tvepisode, video, etc)',
    primary_title   varchar(500) not null comment 'the more popular title / the title used by the filmmakers on promotional materials at the point of release',
    original_title  varchar(500) not null comment 'original title, in the original language',
    runtime_minutes int          null comment 'primary runtime of the title, in minutes',
    start_year      int          null comment 'represents the release year of a title. In the case of TV Series, it is the series start year',
    end_year        int          null comment 'TV Series end year. null for all other title types',
    is_adult        tinyint(1)   null comment '0: non-adult title; 1: adult title',
    constraint title_type_id_fk
        foreign key (type) references ref_types (id)
);

create table episode
(
    episode_id     varchar(10) not null comment 'alphanumeric identifier of episode'
        primary key,
    parent_id      varchar(10) not null comment 'alphanumeric identifier of the parent TV Series',
    episode_number int         null comment 'episode number of the episide_id in the TV series',
    season_number  int         null comment 'season number the episode belongs to',
    constraint episode_title_id_fk
        foreign key (episode_id) references title (id),
    constraint episode_title_id_fk_2
        foreign key (parent_id) references title (id)
);

create table i18n
(
    id          int           not null
        primary key,
    title_id    varchar(10)   not null comment 'an alphanumeric unique identifier of the title',
    ordering    int           null comment 'a number to uniquely identify rows for a given titleId',
    title       varchar(1000) not null comment 'the localized title',
    region      int           null,
    language    int           null,
    is_original tinyint       null comment '0: not original title; 1: original title',
    constraint i18n_i18n_lang_id_fk
        foreign key (region) references ref_lang (id),
    constraint i18n_i18n_lang_id_fk_2
        foreign key (language) references ref_lang (id),
    constraint i18n_title_id_fk
        foreign key (title_id) references title (id)
);

create table lnk_i18n_attributes
(
    i18n_id      int not null,
    attribute_id int not null,
    primary key (i18n_id, attribute_id),
    constraint lnk_i18n_attributes_i18n_id_fk
        foreign key (i18n_id) references i18n (id),
    constraint lnk_i18n_attributes_ref_attributes_id_fk
        foreign key (attribute_id) references ref_attributes (id)
);

create table lnk_i18n_types
(
    i18n_id int not null,
    type_id int not null,
    primary key (i18n_id, type_id),
    constraint lnk_i18n_types_i18n_id_fk
        foreign key (i18n_id) references i18n (id),
    constraint lnk_i18n_types_ref_types_id_fk
        foreign key (type_id) references ref_types (id)
);

create table lnk_person_know
(
    person_id varchar(10) null,
    title_id  varchar(10) null,
    constraint lnk_person_titles_person_id_fk
        foreign key (person_id) references person (id),
    constraint lnk_person_titles_title_id_fk
        foreign key (title_id) references title (id)
);

create table lnk_title_genres
(
    title_id varchar(10) not null,
    genre_id int         not null,
    primary key (title_id, genre_id),
    constraint title_genres_genres_id_fk
        foreign key (genre_id) references ref_genres (id),
    constraint title_genres_title_id_fk
        foreign key (title_id) references title (id)
);

create table title_crew
(
    title_id  varchar(10)                 not null,
    person_id varchar(10)                 not null,
    role      enum ('Director', 'Writer') not null,
    primary key (title_id, person_id, role),
    constraint title_crew_person_id_fk
        foreign key (person_id) references person (id),
    constraint title_crew_title_id_fk
        foreign key (title_id) references title (id)
);

