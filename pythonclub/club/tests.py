from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event
from django.urls import reverse

# Create your tests here.
class MeetingTest(TestCase):
    def test_stringOutput(self):
        meeting = Meeting(meetingtitle = 'Test Meeting Title')
        self.assertEqual(str(meeting), meeting.meetingtitle)
    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class ResourceTest(TestCase):
    def test_stringOutput(self):
        resource = Resource(resourcename = 'Tutorial Website')
        self.assertEqual(str(resource), resource.resourcename)
    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
    def test_stringOutput(self):
        event = Event(eventtitle = 'Test Event Title')
        self.assertEqual(str(event), event.eventtitle)
    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'event')

class MinutesTest(TestCase):
    #def test_stringOutput(self):
        #minutes = MeetingMinutes(minutestime = 10)
        #self.assertEqual(str(minutes), minutes.minutestime)
    def test_tablename(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'minutes')
