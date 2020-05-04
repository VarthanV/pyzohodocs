from pyzohodocs.conf import URL_DEFAULTS
from pyzohodocs.zohoauth import ZohoAuth
import requests
from pyzohodocs.exceptions import ZohoDocsException


class ZohoDocsClient(ZohoAuth):
    def __init__(self, auth_token):
        super().__init__(auth_token)
        self.response = {}
        self.params = {}
        self.params.update(self.default_params)

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

        self._make_post_request(self.url, self._params, _files)

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
        return self.response

    def create_file(self, filename, service, type, **kwargs):
        """
        Creates an empty file 

        :param filename :The name of the file 
        :param service : acceptable inputs document,spreadsheet ,presentation
        :param type : acceptable inputs doc,template 
        :param parentfolderid  : Pass as kwargs, optional
        """
        self.url = URL_DEFAULTS.get('create')
        self.params.update({
            "filename": filename,
            "service": service,
            "type": type
        })
        self.params.update(kwargs)
        self._make_post_request(self.url, self.params)
        return self.response

    def my_files(self, category):
        """
        List your files from ZohoDoc

        :param category : The Category of files you want to list 
        Possible Values string - (documents | spreadsheets | presentations | pictures | music | videos | sharedbyme | sharedtome | thrashed)
        """
        self.params .update({
            "category": category
        })
        self.url = URL_DEFAULTS.get("files")
        self._make_get_request(self.url, self.params)

    def copy_file(self, doc_id, folder_id):
        """
        Copies a file to the required Destination 
        :param:doc_id:  The id of the document that you need to copy
        :param : folder_id : The id of the folder that you wish to copy
        """
        self.params.update({
            "docid": doc_id,
            "folderid": folder_id
        })
        self.url = URL_DEFAULTS.get("copy")
        self._make_post_request(self.url, self.params)

    def move_file(self, doc_id, folder_id):
        """
        Moves a file to the required Destination 
        :param:doc_id:  The id of the document that you need to copy
        :param : folder_id : The id of the folder that you wish to copy
        """
        self.params.update({
            "docid": doc_id,
            "folderid": folder_id
        })
        self.url = URL_DEFAULTS.get("move")
        self._make_post_request(self.url, self.params)

    def move_to_trash(self, doc_id):
        """
        Moves a file to trash 
        :param doc_id : The id of the document you wish to move to trash
        """
        self.url = URL_DEFAULTS.get("trash")
        self.params.update({
            "docid": doc_id
        })
        self._make_post_request(self.url, self.params)

    def restore_from_trash(self, doc_id):
        """
        Restores a file to trash 
        :param doc_id : The id of the document you wish to move to trash
        """
        self.url = URL_DEFAULTS.get("restore")
        self.params.update({
            "docid": doc_id
        })
        self._make_post_request(self.url, self.params)

    def delete_doc(self, doc_id):
        """
        Deletes  a Document
        :param doc_id : The id of the document to delete
        """
        self.url = URL_DEFAULTS.get('delete')
        self.params.update({
            "docid": doc_id
        })
        self._make_post_request(self.url, self.params)

    def rename_doc(self, doc_id, doc_name):
        """
        Used to Rename  a file
        :param doc_id : The id of the Document that you wish to Rename
        :param doc_name  : The new name you wish to give to the document
        """
        self.url = URL_DEFAULTS.get("rename")
        self.params.update({
            "docid": doc_id,
            "docname": doc_name
        })
        self._make_post_request(self.url, self.params)

    def share_folder(self, folder_id, email_id, permission, notify, message="A folder has been shared"):
        """"
        Shares the given Folder 
        :param: folder_id  The id of the folder.
        :param : email_id  The List of Email ID's that you wish 
        to share the folder.

        :param : permission possible values, readonly|readwrite | coowner 
        the permissions you wish to give to the folder. 
        :param : notify Whether to notify the user or not if he has an user id
        :param :message If you wish to provide a message you can

        """
        self.params.update({

            "folderids": folder_id,
            "emailids": email_id,
            "permission": permission,
            "notify": notify,
            "message": message
        })
        self.url = URL_DEFAULTS.get("share")
        self._make_post_request(self.url, self.params)
        
    def share_as_link(self, folderid, visibility, permission, **kwargs):
        """
        Shares a folder as a link ,Returns the Shared link 
        """
        self.url = URL_DEFAULTS.get('link_share')
        self.params.update({
            "folderid": folderid,
            "visibility": visibility,
            "permission": permission
        })
        self.params.update(kwargs)
        self._make_post_request(self.url, self.params)
        return self.response['response'][2]['result'][0]['permaLink']
