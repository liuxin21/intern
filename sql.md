```sql
create table cat
(
    name varchar(20),
    sex char(1),
    birth date
);

describe pet;

load data infile
"...txt"
into table pet;

insert into pet values
("...", ".", "..."),
("...", ".", "...");

update pet
sex = "m"
where name = "liu";



```