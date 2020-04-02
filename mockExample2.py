import requests
class Gold(object):
    def __init__(self):
        self.headers= {"about":"information","contact":"phone"}
        self.url="https://www.tutorialspoint.com/index.htm"
    def get(self):
        r= requests.get(url=self.url, headers=self.headers)
        if r.ok:
            return r.status_code
        else:
            return "bad response"

obj= Gold()
print(obj.get())
