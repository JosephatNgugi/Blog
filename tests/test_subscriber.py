# import unittest
# from app.models import Subscriber
# from app import db

# class SubscriberModelTest(unittest.TestCase):
#     """
#     Test Class to test the behaviour of the subscriber class
#     """

#     def setUp(self):
#         """
#         Set up method that will run before every Test
#         """
#         self.subscriber = Subscriber(email='Test.subscriber@mail.com')

#     def tearDown(self):
#         Subscriber.query.delete()

#     def test_instance(self):
#         self.assertTrue(isinstance(self.subscriber, Subscriber))

#     def test_check_instance_variables(self):
#         self.assertEquals(self.subscriber.email, 'Test.subscriber@mail.com')
