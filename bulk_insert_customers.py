
from cms.models import Customer
from faker import Faker

fake = Faker()

for i in range(1,500):
    Customer.objects.create(first_name=fake.first_name(), last_name=fake.last_name())

