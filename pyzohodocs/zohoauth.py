from pyzohodocs.conf import URL_DEFAULTS
import requests
from requests.exceptions import HTTPError
from pyzohodocs.exceptions import ZohoDocsException
import re


class ZohoAuth(object):
    def __init__(self, auth_token=None):
        self.response = {}
        self.auth_token = auth_token
        self.default_params = {
            "SCOPE": "docsapi",
            "authtoken": self.auth_token
        }

    def _make_request(self, url, params, files=None):
        try:
            self.response = requests.post(url,params,files=files).json()
            return self.response
            
        except Exception as e:
            raise ZohoDocsException("An exception occured make sure you have passed the valid params",e)   

    def get_auth_token(self, email, password, display_name):
        """
        :param email : The Email ID association with your Zoho Docs Account
        :param password : The App Specific password of your account
        :param display_name: The  display name of your account
        """
        url = URL_DEFAULTS.get("auth")
        params = {
            "SCOPE": "ZohoPC/docsapi",
            "EMAIL_ID": email,
            "PASSWORD": password,
            "DISPLAY_NAME": display_name
        }
        res = requests.post(url, params=params).text
        token = re.search('(?<=AUTHTOKEN=)(.*)', res)
        return token
