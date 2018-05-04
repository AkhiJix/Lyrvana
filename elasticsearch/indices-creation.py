from elasticsearch import Elasticsearch
client = Elasticsearch(['https://elastic:CcrIUTedTbLYCZyEqHVKfYmQ@7e4e69552436e5c164c62ed7afb082a8.us-west-2.aws.found.io:9243']) #Expires on May 11th, 2018
mappings = {
    'mappings' : {
        'event' : {
            'properties' : {
                'artist' : {'type': 'text', 'analyzer': 'english'},
                'songname' : {'type': 'text', 'analyzer': 'english'},
                'lyrics': {'type': 'text', 'analyzer': 'english'}
            }
        }
    }
}
client.indices.create(index='lyrvanaindex',  body=mappings)
