create table public.biobank_record
(
    id            char not null
        constraint biobank_record_pk
            primary key,
    record        json not null,
    creation_time timestamp,
    modified_time timestamp
);
