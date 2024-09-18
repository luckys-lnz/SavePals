import unittest
from models import storage
from models.user import User
from sqlalchemy.exc import IntegrityError
from sqlalchemy import MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.exc import OperationalError
"""
Module defines a test for database storage
"""


class TestDBStorage(unittest.TestCase):
    """ Test DBStorage """

    def setUp(self):
        """ Set up test environment """
        # clear database
        self.clear_db()

    def tearDown(self):
        """ Tear down test environment """
        # closes the database session
        storage.close()

    def test_reload(self):
        """Test reloading the session"""
        new_user = User(first_name='test', last_name='data',
                        user_name='reloadtest', email='reload@example.com',
                        password="testpwd")
        storage. new(new_user)
        storage.save()

        # Reload the session
        storage.reload()

        # Verify that the user still exists after reload
        reloaded_user = storage.get(User, new_user.id)
        self.assertIsNotNone(reloaded_user)
        self.assertEqual(reloaded_user.user_name, 'reloadtest')

    def test_new(self):
        """ Test add a new object to the database """
        new_user = User(first_name='test', last_name='data',
                        user_name='testuser', email='test@example.com',
                        password="testpwd")
        storage.new(new_user)
        storage.save()

        # Verify that the user was added by retrieving it from the database
        retrieved_user = storage.get(User, new_user.id)
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.user_name, 'testuser')

    def test_get(self):
        """ Test get an object by ID """
        new_user = User(first_name='test', last_name='data',
                        user_name='getuser', email='get@example.com',
                        password="testpwd")
        storage.new(new_user)
        storage.save()

        # Retrieve the user and check its attributes
        retrieved_user = storage.get(User, new_user.id)
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.user_name, 'getuser')

    def test_filter(self):
        """ Test: filter results from database storage """
        user1 = User(first_name='test', last_name='data',
                     user_name='user1', email='user1@example.com',
                     password="testpwd1")
        user2 = User(first_name='test', last_name='data',
                     user_name='user2', email='user2@example.com',
                     password="testpwd2")
        user3 = User(first_name='test', last_name='data1',
                     user_name='user3', email='user3@example.com',
                     password="testpwd1")
        user4 = User(first_name='test', last_name='data2',
                     user_name='user4', email='user4@example.com',
                     password="testpwd2")

        # save to storage
        user1.save()
        user2.save()
        user3.save()
        user4.save()

        # reload from storage
        storage.reload()

        users = storage.filter(User, last_name='data')
        self.assertEqual(len(users), 2)

        user_ids = [user.id for user in users]

        self.assertIn(user1.id, user_ids)
        self.assertIn(user2.id, user_ids)

    def test_all(self):
        """ Test: retrieve all objects of a specific class """
        user1 = User(first_name='test', last_name='data',
                     user_name='user1', email='user1@example.com',
                     password="testpwd1")
        user2 = User(first_name='test', last_name='data',
                     user_name='user2', email='user2@example.com',
                     password="testpwd2")
        storage.new(user1)
        storage.new(user2)

        all_users = storage.all(User)
        self.assertEqual(len(all_users), 2)
        usernames = [user.user_name for user in all_users.values()]
        self.assertIn('user1', usernames)
        self.assertIn('user2', usernames)

    def test_count(self):
        """ Test: count the number of objects in the database """
        initial_count = storage.count(User)
        new_user = User(first_name='test', last_name='data',
                        user_name='countuser', email='count@example.com',
                        password="testpwd")
        storage.new(new_user)

        updated_count = storage.count(User)
        self.assertEqual(updated_count, initial_count + 1)

    def test_delete(self):
        """ Test: delete an object from the database """
        new_user = User(first_name='test', last_name='data',
                        user_name='deleteuser', email='delete@example.com',
                        password="testpwd")
        storage.new(new_user)
        storage.save()

        # Verify the user is added
        storage.reload()

        retrieved_user = storage.get(User, new_user.id)
        self.assertIsNotNone(retrieved_user)

        storage.delete(retrieved_user)
        storage.save()

        # Verify the user is added
        storage.reload()

        with self.assertRaises(ValueError):
            storage.get(User, new_user.id)

    def test_update(self):
        """ Test: update an object's attributes """
        new_user = User(first_name='test', last_name='data',
                        user_name='updateuser', email='update@example.com',
                        password="testpwd")
        storage.new(new_user)
        storage.save()

        attr_dict = {'user_name': 'updateduser'}
        storage.update(User, new_user.id, attr_dict)

        # Verify that the user's username was updated
        updated_user = storage.get(User, new_user.id)
        self.assertEqual(updated_user.user_name, 'updateduser')

    def test_save(self):
        """ Test: save changes to the database """
        new_user = User(first_name='test', last_name='data',
                        user_name='saveuser', email='save@example.com',
                        password="testpwd")
        storage.new(new_user)
        storage.save()

        # Directly check that the user exists in the database
        retrieved_user = storage.get(User, new_user.id)
        self.assertIsNotNone(retrieved_user)

    def clear_db(self):
        """Clear all data from the database"""
        engine = storage._DBStorage__engine
        metadata = MetaData(bind=engine)
        metadata.reflect()  # Reflect the existing database schema
        Session = sessionmaker(bind=engine)
        session = scoped_session(Session)
        # Iterate through all tables in the database and delete all entries
        for table in reversed(metadata.sorted_tables):
            session.execute(table.delete())
        session.commit()
        session.remove()  # Remove the scoped session after use

    def test_close(self):
        """ Test: closes the current session."""
        new_user = User(first_name='test', last_name='data',
                        user_name='updateuser', email='update@example.com',
                        password="testpwd")
        storage.new(new_user)

        # close session
        storage.close()

        with self.assertRaises(ValueError):
            storage.get(User, new_user.id)
