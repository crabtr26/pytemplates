from locust import HttpUser, task

class PyTemplatesUser(HttpUser):
    @task
    def test(self):
        self.client.get("test")