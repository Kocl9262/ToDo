from google.appengine.ext import ndb


class TaskManager(ndb.Model):
    created = ndb.DateTimeProperty(auto_now_add=True)
    task = ndb.StringProperty()
    description = ndb.TextProperty()
    completed = ndb.BooleanProperty(default=False)
    deleted = ndb.BooleanProperty(default=False)
    complete_till = ndb.StringProperty()
