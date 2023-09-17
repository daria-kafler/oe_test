import unittest
from django.core.management import call_command
from django.test import TestCase
from octopchallange.models import Reading
from django.core.management.base import CommandError


BASE = 'octopchallange/sample_data/'

class ReadingTestCase(TestCase):
    def test_happy_path(self):
      '''Given a valid flow file, the data is parsed and added to the database'''
      filepath = f'{BASE}data_for_testing_valid.txt'
      args = []
      call_command('importflow', *args, filepath)

      assert(Reading.objects.all().count() == 13)

    def test_missing_register_readings_line(self):
      '''Given a flow file with a type line missing,
      no data is added to the database and an exception is raised'''

      filepath = f'{BASE}data_for_testing_no_030.txt'
      args = []
      call_command('importflow', *args, filepath)

      assert(Reading.objects.all().count() == 0)
      self.assertRaises(CommandError)

