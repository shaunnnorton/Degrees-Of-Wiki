import unittest

from src import app, db

#################################################
# Tests                                         #
#################################################


class UtilsTests(unittest.TestCase):
    "Tests for funcitons contained in Utils"
    def setUp(self):
        """Executed prior to each test."""
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        app.config["DEBUG"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

    def test_stored_query(self):
        """TESTS a query that is stored in database"""
        pass

    def test_adjacent_query(self):
        """TESTS a query that should return 1"""
        pass

    def test_long_query(self):
        """TESTS a deep query"""
        pass

    def test_dead_end(self):
        """TESTS a query with no links to follow"""
        pass
