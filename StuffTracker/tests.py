from django.test import TestCase, Client
from .models import Stuff, MyUser
# Create your tests here.
"""
Write a system test using Client that makes sure that on a successful login the correct user's item list is displayed. Load the test database with records to support your test.
Write a system test using Client that makes sure on an unsuccessful login, the home page is redisplayed with a message. Load the test database with records to support your test.
Write a system test that shows that an item added to the list immediately shows up in the rendered response. Load the test database with records to support your test.
"""
class LoginList(TestCase):
    monkey=None
    thingList=None

    def setUp(self):
        self.monkey = Client()
        self.thingList ={"one":["cat","dog"],"two":["cake"]}

        for i in self.thingList.keys():
            temp = MyUser(name=i,password=i)
            temp.save()
            for j in self.thingList[i]:
                Stuff(name=j,owner=temp).save()

    def test_correctName(self):
        for i in self.thingList.keys():
            resp = self.monkey.post("/",{"name":i,"password":i},follow=True)
            self.assertEqual(resp.context["name"],i,"name not passed from login to list")

    def test_complete(self):
        for i in self.thingList.keys():
            resp = self.monkey.post("/",{"name":i,"password":i},follow=True)
            for j in self.thingList[i]:
                self.assertIn(j,resp.context["things"],"list missing an item, user: " + i)

    def test_precise(self):
        for i in self.thingList.keys():
            resp = self.monkey.post("/",{"name":i,"password":i},follow=True)
            for j in resp.context["things"]:
                self.assertIn(j,self.thingList[i],"list contains an extra item, user: " + i)

class LoginFail(TestCase):

    monkey = None
    thingList = None

    def setUp(self):
        self.monkey = Client()
        self.thingList = {"one": ["cat", "dog"], "two": ["cake"]}

        for i in self.thingList.keys():
            temp = MyUser(name=i, password=i)
            temp.save()
            for j in self.thingList[i]:
                Stuff(name=j, owner=temp).save()

    def test_noPassword(self):
        resp = self.monkey.post("/", {"name": "one", "password": "three"}, follow=True)
        self.assertEqual(resp.context["message"],"bad password","no failed login password, user:one, pass:three")

    def test_OtherUserPassword(self):
        resp = self.monkey.post("/", {"name": "one", "password": "two"}, follow=True)
        self.assertEqual(resp.context["message"],"bad password","no failed login password, user:one, pass:two, two is valid for another user")

class AddItem(TestCase):

    monkey = None
    thingList = None

    def setUp(self):
        self.monkey = Client()
        self.thingList = {"one": ["cat", "dog"], "two": ["cake"]}

        for i in self.thingList.keys():
            temp = MyUser(name=i, password=i)
            temp.save()
            for j in self.thingList[i]:
                Stuff(name=j, owner=temp).save()

    def test_addItem(self):
        c = self.monkey.session
        c["name"] = "one"
        c.save()
        resp = self.monkey.post("/things/", {"stuff": "fish"}, follow=True)
        print(resp.context)
        self.assertListEqual(["cat","dog","fish"],resp.context["things"])