-- 여기서 작성하는 SQL문을 mydb.sqlite3에서 사용하겠다고 선언해줘야함!
-- 마우스 우클릭 -> Use Databass -> mydb.sqlite3 선택

CREATE TABLE contacts (
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    email TEXT NOT NULL UNIQUE
);

ALTER TABLE contacts RENAME TO new_contacts;

ALTER TABLE new_contacts RENAME COLUMN name TO last_name;

ALTER TABLE new_contacts ADD COLUMN address TEXT NOT NULL DEFAULT 'no address';

ALTER TABLE new_contacts DROP COLUMN address;

DROP TABLE new_contacts;
