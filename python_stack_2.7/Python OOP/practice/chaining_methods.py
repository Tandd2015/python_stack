user1.login()
user1.show()
user1.logout()

user1.login().show().logout()

class User(object):
    def login(self):
        # your code goes here...
        return self