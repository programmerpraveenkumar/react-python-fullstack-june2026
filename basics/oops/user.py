class User:
    # variable
    userlist = []
    # to access or same class prop we should class `self`
    def add_user(self,name):
        self.userlist

    def print_user(self):
        for user in self.userlist:
            print(user)