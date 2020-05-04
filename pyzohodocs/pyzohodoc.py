from pyzohodocs.conf import URL_DEFAULTS
from pyzohodocs.zohoauth import ZohoAuth
import requests
from pyzohodocs.exceptions import ZohoDocsException


class ZohoDocsClient(ZohoAuth):
    def __init__(self, auth_token):
        super().__init__(auth_token)

    def upload_file(self, file_name, file_path, **kwargs):
        self.url = URL_DEFAULTS.get("upload")
        """
        Method to upload your file to the ZohoDocs 
        :param file_name : The name of the file you wish to give it in the cloud.
        :param file_path : The path of the file in your local machine that you need to upload ,
        can be a file name if it is in the same directory.

        :param fid : optional : The folder id you wish to upload.
        :param wsid  : optional : The ID of the Workspace

        """
        self._params = {
            "filename": file_name,

        }
        _files = {"content": open(
            file_path, 'rb')}
        self._params.update(kwargs)
        self._params.update(self.default_params)
        self._make_request(self.url, self._params, _files)

    def _save_doc(self, link, file_name, params):
        try:
            file_obj = requests.get(link, params=params, stream=True)
            with open(file_name, 'wb') as f:
                # 2 MB chunks
                for chunk in file_obj.iter_content(1024 * 1024 * 2):
                   
                    f.write(chunk) 
        except Exception as e:
            raise ZohoDocsException(e)

    def download_file(self, doc_id, file_name):
        """
        Downloads your file  from the ZohoDocs
        :param doc_id  ID of the document 
        : param file_name The File Name you want to Save

         """
        self._url = URL_DEFAULTS.get("download")
        self._formatted_url = self._url+doc_id
        self._save_doc(self._formatted_url, file_name, self.default_params)


    