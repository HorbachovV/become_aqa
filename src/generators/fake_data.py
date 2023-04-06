from faker import Faker

fake = Faker('en_US')

class FakeData:

    def random_repo_name(self):
        repo_name = fake.text()
        return repo_name