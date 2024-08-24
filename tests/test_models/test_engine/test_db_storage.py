import unittest
from models import storage
from models.user import User
from sqlalchemy.exc import IntegrityError
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
        new_user = User(username='reloadtest', email='reload@example.com',
                        password="testpwd")
        storage.add(new_user)
        storage.save()

        # Reload the session
        storage.reload()

        # Verify that the user still exists after reload
        reloaded_user = storage.get(User, new_user.id)
        self.assertIsNotNone(reloaded_user)
        self.assertEqual(reloaded_user.username, 'reloadtest')

    def test_add(self):
        """ Test add a new object to the database """
        new_user = User(username='testuser', email='test@example.com',
                        password="testpwd")
        storage.add(new_user)

        # Verify that the user was added by retrieving it from the database
        retrieved_user = storage.get(User, new_user.id)
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.username, 'testuser')

    def test_get(self):
        """ Test get an object by ID """
        new_user = User(username='getuser', email='get@example.com',
                        password="testpwd")
        storage.add(new_user)

        # Retrieve the user and check its attributes
        retrieved_user = storage.get(User, new_user.id)
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.username, 'getuser')

    def test_all(self):
        """ Test: retrieve all objects of a specific class """
        user1 = User(username='user1', email='user1@example.com',
                     password="testpwd1")
        user2 = User(username='user2', email='user2@example.com',
                     password="testpwd2")
        storage.add(user1)
        storage.add(user2)

        all_users = storage.all(User)
        self.assertEqual(len(all_users), 2)
        usernames = [user.username for user in all_users]
        self.assertIn('user1', usernames)
        self.assertIn('user2', usernames)

    def test_count(self):
        """ Test: count the number of objects in the database """
        initial_count = storage.count(User)
        new_user = User(username='countuser', email='count@example.com',
                        password="testpwd")
        storage.add(new_user)

        updated_count = storage.count(User)
        self.assertEqual(updated_count, initial_count + 1)

    def test_delete(self):
        """ Test: delete an object from the database """
        new_user = User(username='deleteuser', email='delete@example.com',
                        password="testpwd")
        storage.add(new_user)
        storage.save()

        # Verify the user is added
        storage.reload()

        retrieved_user = storage.get(User, new_user.id)
        self.assertIsNotNone(retrieved_user)

        storage.delete(new_user)
        storage.save()

        # Verify the user is added
        storage.reload()

        deleted_user = storage.get(User, new_user.id)
        self.assertIsNone(deleted_user)

    def test_update(self):
        """ Test: update an object's attributes """
        new_user = User(username='updateuser', email='update@example.com',
                        password="testpwd")
        storage.add(new_user)

        storage.update(User, new_user.id, username='updateduser')

        # Verify that the user's username was updated
        updated_user = storage.get(User, new_user.id)
        self.assertEqual(updated_user.username, 'updateduser')

    def test_save(self):
        """ Test: save changes to the database """
        new_user = User(username='saveuser', email='save@example.com',
                        password="testpwd")
        storage.add(new_user)

        # Directly check that the user exists in the database
        retrieved_user = storage.get(User, new_user.id)
        self.assertIsNotNone(retrieved_user)

    def clear_db(self):
        """Clear all data from the database"""
        session = storage._DBStorage__session
        # Iterate through all tables in the database and delete all entries
        for table in reversed(session.metadata.sorted_tables):
            session.execute(table.delete())
        session.commit()

    def close(self):
        """Closes the current session."""
        self.session.close()
