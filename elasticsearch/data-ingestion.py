from elasticsearch import Elasticsearch
import json
import random as r
client = Elasticsearch(['https://elastic:CcrIUTedTbLYCZyEqHVKfYmQ@7e4e69552436e5c164c62ed7afb082a8.us-west-2.aws.found.io:9243']) #Expires on May 11th, 2018

docs = json.load(open('LyrJson.json'))
for doc in docs:
    client.create(index='lyrvanaindex',doc_type='event', body=doc, id=['artist'] + ['songname'] + r.randint(0,100))
