from locust import task, between
from locust.contrib.fasthttp import FastHttpUser


# (Only first time) Install @locust, open a terminal & run: pip3 install locust
# Open terminal & run: locust -f us_pg.py
# Open address: http://localhost:8089/
# Insert the Number of total users to simulate
# Insert the Spawn rate (users spawned/second)
# Finally the HOST of the page that probably loads it, otherwise it is:  https://us.pg.com

class WebsiteUser(FastHttpUser):
    # Config the host
    host = "https://us.pg.com"
    wait_time = between(2, 50)

    # some things you can configure on FastHttpUser
    connection_timeout = 60.0
    insecure = True
    max_redirects = 5
    max_retries = 1
    network_timeout = 60.0

    @task()  # Index
    def index(self):
        self.client.get("/")
        pass

    @task()  # Brands
    def brands(self):
        self.client.get("/brands")
        pass

    @task()  # Baby
    def baby_care(self):
        self.client.get("/brands/#Baby-Care")
        pass

    @task()  # Fabric
    def fabric_care(self):
        self.client.get("/brands/#Fabric-Care")
        pass

    @task()  # Family
    def family_care(self):
        self.client.get("/brands/#Family-Care")
        pass

    @task()  # Feminine
    def femenine_care(self):
        self.client.get("/brands/#Feminine-Care")
        pass

    @task()  # Grooming
    def grooming(self):
        self.client.get("/brands/#Grooming")
        pass

    @task()  # Hair
    def hair_care(self):
        self.client.get("/brands/#Hair-Care")
        pass

    @task()  # Home
    def home_care(self):
        self.client.get("/brands/#Home-Care")
        pass

    @task()  # Oral
    def oral_care(self):
        self.client.get("/brands/#Oral-Care")
        pass

    @task()  # Personal health
    def personal_health_care(self):
        self.client.get("/#Personal-Health-Care")
        pass

    @task()  # Sking & Personal
    def personal_health_care(self):
        self.client.get("/brands/#Skin-and-Personal-Care")
        pass
