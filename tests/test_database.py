import unittest

from testcontainers.postgres import PostgresContainer

from database.database import Database


class DatabaseTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls._postgresContainer = PostgresContainer("postgres:14", dbname="biobank")
        cls._postgresContainer.start()
        url = cls._postgresContainer.get_connection_url().split("+")[1].replace("psycopg2", "postgresql")
        Database.connectionUrl = url
        cls._db = Database()

    def test_ConnectionIsAlive(self):
        self.assertTrue(self._db.isAlive())

    def test_PostgresVersion(self):
        version = self._db.query("select version()")
        self.assertIn("14", version[0][0])

    def test_DBWasInitialized(self):
        result = self._db.query("SELECT to_regclass('biobank_record')")
        self.assertEquals(result[0][0], "biobank_record")

    def test_executeCreateTable(self):
        self.assertTrue(self._db.execute(create_table))
        self._db.execute(drop_table)

    def test_CreateAndInsertIntoTestTable(self):
        self._db.execute(create_table)
        self.assertTrue(self._db.execute(insert_test))
        self._db.execute(drop_table)

    @classmethod
    def tearDownClass(cls) -> None:
        cls._db.close()
        cls._postgresContainer.stop()


create_table = 'CREATE TABLE test (id integer);'
drop_table = 'DROP TABLE test;'
insert_test = 'INSERT INTO test VALUES (1);'
