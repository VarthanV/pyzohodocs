import pytest
from pyzohodocs.zohoauth import ZohoAuth
from pyzohodocs.pyzohodoc import ZohoDocsClient

def test_auth_fails():
    with pytest.raises(Exception) as e :
        z =ZohoAuth.get_auth_token('v','dd','cc')

def test_upload_docs_client_fails_when_key_invalid():
    with pytest.raises(Exception) as e:
        client = ZohoDocsClient('attjtj')
        client.upload_file(file_name='examplee.docx',file_path = 'The path to your file')

def test_download_docs_fails_when_key_invalid():
    with pytest.raises(Exception) as e:
        client = ZohoDocsClient('attjtj')
        client.download_file('dkdjd',file_name='v.docx')


