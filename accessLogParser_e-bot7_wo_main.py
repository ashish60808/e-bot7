import json,pymongo,re
f = open("log/host.access.log", "r")
i=0
document={'user agent':'','timestamp':'','status code':''}
for line in f:
    # print(f'{i}.{line}')
    match=re.search(r'(^\d+.\d+.\d+.\d+)\s-\s(\w+)\s\[(.+)\]\s"\w+\s(.+)\sHTTP/\d+.\d+"\s(\d+)\s(\d+)\s"(\D)"\s"(.+)"\s"',line)
    if match:
        # print("IP IS:",match.group(1))
        # print("USER IS:",match.group(2))
        # print("Timestamp IS:",match.group(3))
        # print("Requested File:",match.group(4))
        # print("Status Code :",match.group(5))
        # print("BAndwidth :",match.group(6))
        # print("Refrer :",match.group(7))
        # print("UA :",match.group(8))
        document['user agent']=match.group(8)
        document['timestamp']=match.group(3)
        document['status code']=match.group(5)

    print(document)     
    i+=1



#    172.17.0.1 - admin [13/Jun/2021:01:51:39 +0000] "GET / HTTP/1.1" 304 0 "-" 
# "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0" "-"
# UA,Timestamp,Response code