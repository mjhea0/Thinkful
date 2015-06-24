create table snippets (
keyword text primary key,
message text not null default ''
);

insert into snippets values ('insert', 'Add new rows to a table');
insert into snippets values ('inserted again', 'added another row')
insert into snippets values ('third insert', 'third row')
