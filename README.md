# Lyrvana
A Music Searching Engine implemented using Elasticsearch. 
This project is developed as a part of the coursework *CS185C-Advanced Topics in CS (Big Data)* under the supervision of Prof. James Casaletto at San Jose State University.  
The team members are [Akhilesh Jichkar]("https://github.com/AkhiJix/") and [Siddharth Kulkarni]("https://github.com/siddharthkul").  

## Introduction

### What is Elasticsearch?
Elasticsearch is a RESTful powerful indexing and search tool, which is a part of the Elastic Stack.<br />
Elasticsearch is horizontally scalable, which is ideal for music data, whose size may go up to a few GBs.<br />
Elasticsearch is also highly available, has flexible data model, and boasts rapid query execution.<br />
Since the goal is to develop a Music Search Engine, Elasticsearch qualfies as a fast and reliable searching tool.<br />

### Setting up Elasticsearch
An Elasticsearch cluster can be installed on all major platforms. In order to ensure availability, this project would be hosted on 
[Elastic cloud](https://cloud.elastic.co "Elastic Cloud").
- Create a new account on [Elastic cloud](https://cloud.elastic.co "Elastic Cloud"). <br />
- Create a New Cluster and keep the default settings intact on the following page. Let the cluster name be _Cluster1ES_.<br />
- Now view the cluster just created. Save the CloudID, username and password for the newly created cluster. You'll need this later.<br />
- Wait for the 'Node Status' to change to 'Running'. Now click on the Endpoints -> Elasticsearch to see .<br />
- The cluster is up and running now.<br />

The next step involves creating indices on this Elasticsearch cluster. But before that, we need to take a look into the data we would be using for the project. This is because the Elasticsearch indices depend on the data type of the incoming data.

## Data
The data used for this project is from Song Lyrics Dataset on [Kaggle](https://www.kaggle.com/mousehead/songlyrics "55000+ Song Lyrics").
It contains 57650 songs in CSV format. The attributes are Artist Name, Song Name and the Lyrics of the song.<br />

To be ingested by Elasticsearch, the data needs to be converted from CSV to JSON.
Since the data is around 70MBs, the online converters won't be able to do the conversion.
Therfore, a python script [*csvtojson.py*]("../data/csvtojson.py") is written to perform the conversion. The output is [LyrJson.json](..data/LyrJson.zip)
> PS: Unzip [zip file](../data/songdata.zip) first to get the csv file.
> PS: There is an extra comma in Line 2 of the generated JSON file, and it needs to be removed manually.

Optionally, you may want to include images of artist in your search results, [artistimages.py](../data/artistimages.py) shows a rudimentary way to obtain artist images from Wikipedia pages using BeautifulSoup, a Python Web Scraping tool.

The data preprocessing is now complete.

## Creating Indices on Elastic Cloud
