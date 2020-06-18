# pyzohodocs

pyzohodocs is an unofficial client for the Zohodocs REST API.

[https://www.zoho.com/docs/zoho-docs-api.html](http://https://www.zoho.com/docs/zoho-docs-api.html "https://www.zoho.com/docs/zoho-docs-api.html")


[![pyzohodocs](https://pypip.in/download/pyzohodocs/badge.svg)](https://pypi.org/project/pyzohodocs/)
 

It blends seamlessy with your web applications,scripts ,automation etc . Incase you are using Zoho Docs in your application, you can use this client.

## Obtaining an Authtoken

```python
from pyzohodocs.auth import  ZohoAuth
token = ZohoAuth.get_auth_token(email = '<YOUR EMAIL ID>',
password = '<YOUR APP SPECIFIC PASSWORD>',
display_name = '<YOUR DISPLAYNAME>')
```

## Uploading a File
```python
    from pyzohodocs.pyzohodoc import ZohoDocsClient
    client = ZohoDocsClient('<YOUR AUTH TOKEN>')
    client.upload_file(file_name.='example.docx',file_path = 'The path to your file')
```
You can pass extra arguments to this method as dict . See Documentation for the list of arguments you can pass

## Downloading a File

```python
# Pass the id of the document
# The File name you wish to name it
from pyzohodocs.pyzohodoc import ZohoDocsClient
client = ZohoDocsClient('<YOUR AUTH TOKEN>'
client.download_file(doc_id ='676554www',file_name = ' v.docx' )
```

## Create a Empty File

```python
from pyzohodocs.pyzohodoc import ZohoDocsClient
client = ZohoDocsClient('<YOUR AUTH TOKEN>')
client.create_file(filename = 'test.docx', service='document',type='doc')
```

## List your Files

```python
from pyzohodocs.pyzohodoc import ZohoDocsClient
client = ZohoDocsClient('<YOUR AUTH TOKEN>'
client.my_files(category = "documents")
```

There are methods for every operation that is available in the API . A documentation will be created soon.

In case of Issues please create a new Ticket here .
[https://github.com/VarthanV/pyzohodocs/issues](htthttps://github.com/VarthanV/pyzohodocs/issuesp:// "https://github.com/VarthanV/pyzohodocs/issues")

For addition of new features
[https://github.com/VarthanV/pyzohodocs/pulls](https://github.com/VarthanV/pyzohodocs/pullshttp:// "https://github.com/VarthanV/pyzohodocs/pulls")
