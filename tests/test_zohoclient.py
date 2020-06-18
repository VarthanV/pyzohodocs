import pytest
from pyzohodocs.zohoauth import ZohoAuth
from pyzohodocs.pyzohodoc import ZohoDocsClient
def test_auth_fails():
    with pytest.raises(Exception) as e :
        token = ZohoAuth(email ='vichu@gmail.con',password='dd',display_name = 'dkdkdkd')

def test_upload_docs_client_fails():
    with pytest.raises(Exception) as e:
        client = ZohoDocsClient('attjtj')
        client.upload_file(file_name='examplee.docx',file_path = 'The path to your file')

def test_download_docs_fails():
    with pytest.raises(Exception) as e:
        client = ZohoDocsClient('attjtj')
        client.download_file('dkdjd',file_name='v.docx')





    
