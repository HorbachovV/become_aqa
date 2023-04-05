from faker import Faker

fake = Faker()

class FakeData:

    def random_repo_name(self):
        repo_name = fake.url()
        return repo_name