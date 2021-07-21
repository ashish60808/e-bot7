import json,pymongo,re

document={'user agent':'','timestamp':'','status code':''}


def log_parser(log_file): 
#   i=3  
  list_documents=[]
  for line in log_file:
    match=re.search(r'(^\d+.\d+.\d+.\d+)\s-\s(\w+)\s\[(.+)\]\s"\w+\s(.+)\sHTTP/\d+.\d+"\s(\d+)\s(\d+)\s"(\D)"\s"(.+)"\s"',line)
    if match:
        document['user agent']=match.group(8)
        document['timestamp']=match.group(3)
        document['status code']=match.group(5)
        list_documents.append(document.copy()) 
    print(document) 
  print(list_documents)         
  insert_document(list_documents) 

def insert_document(document):
  client = pymongo.MongoClient("mongodb://localhost:27017/")
  db = client["ebot7"]
  col = db["access"]
  result = col.insert_many(document)
  print(result)   
  db = client["ebot7"]
if __name__ == '__main__':
  log_file = open("nginx/log/host.access.log", "r")
  log_parser(log_file)