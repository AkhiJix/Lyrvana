# Lyrvana
A Music Searching Engine implemented using Elasticsearch

## Introduction

### What is Elasticsearch?
Elasticsearch is a RESTful powerful indexing and search tool, which is a part of the Elastic Stack.<br />
Elasticsearch is horizontally scalable, which is ideal for music data, whose size may go up to a few GBs.<br />
Elasticsearch is also highly available, has flexible data model, and boasts rapid query execution.<br />
Since the goal is to develop a Music Search Engine, Elasticsearch qualfies as a fast and reliable searching tool.<br />

### Data
The data used for this project is from Song Lyrics Dataset on [Kaggle](https://www.kaggle.com/mousehead/songlyrics "55000+ Song Lyrics").
It contains 57650 songs in CSV format. The attributes are Artist Name, Song Name and the Lyrics of the song.<br />

### Setting up Elasticsearch
An Elasticsearch cluster can be installed on all major platforms. In order to ensure availability, this project would be hosted on 
[Elastic cloud](https://cloud.elastic.co "Elastic Cloud").
> Create a new account on [Elastic cloud](https://cloud.elastic.co "Elastic Cloud"). <br />
> Create a New Cluster and keep the default settings intact on the following page. Let the cluster name be _Cluster1ES_.<br />
> Now view the cluster just created. Save the CloudID, username and password for the newly created cluster. You'll need this later.<br />
> Wait for the 'Node Status' to change to 'Running'. Now click on the Endpoints -> Elasticsearch to see .<br />
> The cluster is up and running now.<br />

The next step involves creating indices on this Elasticsearch cluster.
