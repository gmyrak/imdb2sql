CREATE DATABASE `imdb` DEFAULT COLLATE utf8mb4_unicode_ci;

USE `imdb`;

create table genres
(
    id    int         not null
        primary key,
    genre varchar(20) not null,
    constraint genres_genre_uindex
        unique (genre)
);

create table types
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
    is_adult        tinyint(1)   not null comment '0: non-adult title; 1: adult title',
    constraint title_types_id_fk
        foreign key (type) references types (id)
);

