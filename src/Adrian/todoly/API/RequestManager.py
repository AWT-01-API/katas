"""manage rest api requests"""
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class RequestManager(object):
    """manager of rest api requests"""
    def __init__(self, main_url, username, password):
        self.main_url = main_url
        self.username = username
        self.password = password
        self.token = None

    def set_token(self, token):
        """set token value for non basic authentication requests"""
        self.token = token

    def get_request_basic_auth(self, endpoint):
        """used to get user token using"""
        session = requests.Session()
        session.auth = (self.username, self.password)
        response = self.requests_retry_session(session=session).get(self.main_url + endpoint)
        return response

    def get_request(self, endpoint):
        """used to get request from api"""
        # endpoint: api request endpoint as string
        session = requests.Session()
        if self.token:
            session.headers.update({"X-TrackerToken": self.token})
        else:
            # log message "set token before make get_request"
            return None
        response = self.requests_retry_session(session=session).get(self.main_url + endpoint)
        return response

    def post_request(self, endpoint, body):
        """used to get request from api"""
        # endpoint: api request endpoint as string
        # body: body for post as dictionary of strings {"example":"data",}
        session = requests.Session()
        if self.token:
            session.headers.update({"X-TrackerToken": self.token})
        else:
            # log message "set token before make post_request"
            return None
        response = self.requests_retry_session(session=session).post(self.main_url + endpoint, body)
        return response

    def put_request(self, endpoint, body):
        """used to get request from api"""
        # endpoint: api request endpoint as string
        # body: body for post as dictionary of strings {"example":"data",}
        session = requests.Session()
        if self.token:
            session.headers.update({"X-TrackerToken": self.token})
        else:
            # log message "set token before make put_request"
            return None
        response = self.requests_retry_session(session=session).put(self.main_url + endpoint, body)
        return response

    def delete_request(self, endpoint):
        """used to get request from api"""
        # endpoint: api request endpoint as string
        session = requests.Session()
        if self.token:
            session.headers.update({"X-TrackerToken": self.token})
        else:
            # log message "set token before make post_request"
            return None
        response = self.requests_retry_session(session=session).delete(self.main_url + endpoint)
        return response

    @staticmethod
    def requests_retry_session(
            retries=3,
            backoff_factor=0.3,
            status_forcelist=(500, 502, 504),
            session=None):
        """used to process a request retry if their response is 500, 502, or 504 """
        session = session or requests.Session()
        retry = Retry(
            total=retries,
            read=retries,
            connect=retries,
            backoff_factor=backoff_factor,
            status_forcelist=status_forcelist,
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        return session
