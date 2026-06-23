from requests import Session
from requests.cookies import cookiejar_from_dict


class APIProfile:
    def __init__(self, name, url, token, username):
        self.name = name
        self.url = url
        self.token = token
        self.username = username
        self.session = Session()
        self.session.cookies = cookiejar_from_dict({"GZCTF_TOKEN": self.token})

    def make_endpoint(self, rel_path: str):
        return self.url + rel_path

    @classmethod
    def from_dict(cls, obj: dict[str, str]):
        name = obj["name"].strip("/")
        url = obj["url"].strip("/")
        token = obj["token"]
        username = obj["username"]
        return cls(name, url, token, username)


def make_get(profile: APIProfile, rel_path: str, **kwargs):
    r = profile.session.get(url=profile.make_endpoint(rel_path), **kwargs)
    r.raise_for_status()
    return r


def make_post(profile: APIProfile, rel_path: str, **kwargs):
    r = profile.session.post(url=profile.make_endpoint(rel_path), **kwargs)
    r.raise_for_status()
    return r


def make_put(profile: APIProfile, rel_path: str, **kwargs):
    r = profile.session.put(url=profile.make_endpoint(rel_path), **kwargs)
    r.raise_for_status()
    return r


def make_delete(profile: APIProfile, rel_path: str, **kwargs):
    r = profile.session.delete(url=profile.make_endpoint(rel_path), **kwargs)
    r.raise_for_status()
    return r
