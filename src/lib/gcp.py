import os
from googleapiclient.discovery import build, MediaFileUpload
from httplib2 import Http
from oauth2client import file, client, tools


class GCP(object):
    def __init__(self, cred_file, store_file=os.getenv('gcp_ident_file')):
        self.store_file = store_file
        # self.photo_scopes = 'https://www.googleapis.com/auth/photoslibrary.readonly'
        self.photo_scopes = 'https://www.googleapis.com/auth/photoslibrary.sharing'

        store = file.Storage(self.store_file)
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets(cred_file, self.photo_scopes)
            creds = tools.run_flow(flow, store)

        self.lib = build('photoslibrary', 'v1', http=creds.authorize(Http()))

    def format_date(self, my_date):
        # my_date = "27/12/2019"

        my_date_arr = my_date.split('/')
        return [{"day": my_date_arr[0], "month": my_date_arr[1], "year": my_date_arr[2]}]

    def listMedia(self, date_filter=None, media_type=["PHOTO", "VIDEO"]):
        # date_filter = "27/12/2019" or "0/12/2019" for all days of december

        nextpagetoken = 'Dummy'
        filters = { "mediaTypeFilter": {"mediaTypes": media_type} }
        if date_filter is not None:
            filters = {
                    "dateFilter": {"dates": self.format_date(date_filter)},
                    "mediaTypeFilter": {"mediaTypes": media_type}
            }

        res = []
        while nextpagetoken != '':
            nextpagetoken = '' if nextpagetoken == 'Dummy' else nextpagetoken
            results = self.lib.mediaItems().search(
                body={
                    "filters":  filters, 
                    "pageSize": 100, 
                    "pageToken": nextpagetoken,
                }
            ).execute()
                          
            # The default number of media items to return at a time is 25. The maximum pageSize is 100.
            items = results.get('mediaItems', [])
            nextpagetoken = results.get('nextPageToken', '')
            for item in items:
                res.append(item)
                
        return res
    
    def uploadMedia(self, media, name='', mimetype='image/png'):
        media = MediaFileUpload(media, mimetype=mimetype, resumable=True)
        request = self.lib.create(media_body=media, body={'name': name})
        response = None
        while response is None:
            status, response = request.next_chunk()

        return response

    def listAlbums(self):
        r = self.lib.albums().list(pageSize=10).execute()
        items = r.get('albums', [])
        return items
    
    def createAlbum(self, title):
        r = self.lib.albums().create(body={'album':{'title':title}}).execute()
        return r.id

