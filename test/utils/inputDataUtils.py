class InputDataFromFaker:

    def __init__(self, fakerObject):
        self.fakerObj = fakerObject

    def getFirstName(self):
        return self.fake.first_name()

    def getLastName(self):
        return self.fake.last_name()

    def getEmailID(self):
        return (self.fake.email())

    def getAddress(self):
        return self.fake.address()

    def getPassWord(self):
        self.fake.internet.password()
