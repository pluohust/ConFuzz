create table t(l);PRAGMA writable_schema=ON;
UPDATE sqlite_master SET sql='0 0000000000000000000000000000000000000000000000000000000000000000000000000000000[%S';PRAGMA t;SAVEPOINT x;ROLLBACK;VACUUM;
