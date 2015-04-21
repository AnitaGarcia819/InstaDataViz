from instagram.client import InstagramAPI
api = InstagramAPI(client_id='7f674565db0d42ed9b4dd4f366db65be', client_secret='9a5f5c38eec74eff9f479e3659d4824f')
popular_media = api.media_popular(count=20)
for media in popular_media:
    print media.images['standard_resolution'].url