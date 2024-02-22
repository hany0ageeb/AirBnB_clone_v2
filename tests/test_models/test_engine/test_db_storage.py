#!/usr/bin/python3
"""
This Module defines class TestDBStorage
"""
from unittest import TestCase
from models.engine.db_storage import DBStorage
from datetime import datetime
import MySQLdb
import os



class TestDBStorage(TestCase):
    """TestDBStorage class defines serveral tests for DBStorage"""
    def test_all(self):
        from models.state import State
        # Setup
        storage = DBStorage()
        storage.reload()
        conn = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            database=os.getenv('HBNB_MYSQL_DB'),
            username=os.getenv('HBNB_MYSQL_USER'),
            password=os.getenv('HBNB_MYSQL_PWD'))
        cur = conn.cursor()
        cur.execute('INSERT INTO states(id, name. created_at, updated_at) VALUES (%s,%s,%s,%s)', ('123-123', 'Fake State', datetime.utcnow(), datetime.utcnow()))
        states = storage.all(State)
        self.assertEqual(len(states), 1, 'all not working')
        self.assertTrue('State.123-123' in states)
        cur.close()
        conn.close()