import csv
csv_file = open('songdata.csv','r')
json_file = open('LyrJson.json','w')
json_file.write("[\n")
for line in csv.reader(csv_file):
    json_file.write(",\n\t{\n")
    json_file.write( "\t\t\"artist\": \""+line[0].replace(",","").replace("\'","").replace("\"","")+"\",\n")
    json_file.write( "\t\t\"songname\": \""+line[1].replace(",","").replace("\'","").replace("\"","")+"\",\n")
    json_file.write( "\t\t\"lyrics\": \""+line[2].replace("\n","").replace(",","").replace("\'","").replace("\"","")+"\"\n")
    json_file.write("\t}")
json_file.write("]")
json_file.close()
csv_file.close()
