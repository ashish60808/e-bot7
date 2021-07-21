import json,pymongo,re

document={'user agent':'','timestamp':'','status code':''}
list_documents=[]

def log_parser(log_file): 
#   i=3  
  for line in log_file:
    match=re.search(r'(^\d+.\d+.\d+.\d+)\s-\s(\w+)\s\[(.+)\]\s"\w+\s(.+)\sHTTP/\d+.\d+"\s(\d+)\s(\d+)\s"(\D)"\s"(.+)"\s"',line)
    if match:
        # document['_id']=i
        document['user agent']=match.group(8)
        document['timestamp']=match.group(3)
        document['status code']=match.group(5)
        list_documents.append(document.copy())
    # i+=1        
    insert_document(document) 

def insert_document(document):
  client = pymongo.MongoClient("mongodb://localhost:27017/")
  db = client["ebot7"]
  col = db["access"]
  result = col.insert_one(document)
  print(result.inserted_id)   

if __name__ == '__main__':
  log_file = open("log/host.access.log", "r")
  log_parser(log_file)