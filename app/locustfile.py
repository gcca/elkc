from random import sample, randint
from string import digits, ascii_letters

from locust import HttpUser, task


class PostsUser(HttpUser):
    mset = digits + ascii_letters

    @task
    def push(self):
        slug = "".join(sample(self.mset, randint(20, 30)))
        data = {
            f"k_{i}": "".join(sample(self.mset, randint(30, 50)))
            for i in range(randint(15, 20))
        }
        self.client.post(f"/post/{slug}", json=data)

    @task
    def describe(self):
        self.client.get("/posts/describe")
