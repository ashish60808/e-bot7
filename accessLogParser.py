access_logs = [
    '2019-01-01T00:00:01, 12.21.1.101, GET, /assets/js/loader2.js, 102, 0',
    '2019-01-01T00:00:02, 12.21.1.109, GET, /assets/js/loader3.js, 102, 0',
    '2019-01-01T00:00:01, 12.21.1.101, GET, /assets/js/loader.js, 102, 0',
    '2019-01-01T00:00:02, 12.21.2.102, GET, /assets/img/hero_100.jpg, 157121, 0',
    '2019-01-01T01:00:01, 12.21.1.102, GET, /assets/js/loader.js, 102, 1',
    '2019-01-01T01:00:03, 12.21.1.108, GET, /assets/js/loader.js, 102, 1',
    '2019-01-01T00:00:04, 12.21.1.107, GET, /assets/js/loader.js, 102, 0',
    '2019-01-01T00:00:05, 12.21.2.108, GET, /assets/img/hero_100.jpg, 157121, 0',
    '2019-01-01T01:00:06, 12.21.1.102, GET, /assets/js/loader.js, 102, 1',
    '2019-01-01T01:00:07, 12.21.1.104, GET, /assets/js/loader.js, 102, 1',
    '2019-01-01T00:00:08, 12.21.2.105, GET, /assets/img/hero_100.jpg, 157121, 0',
    '2019-01-01T01:00:09, 12.21.1.103, GET, /assets/js/loader.js, 102, 1',
    '2019-01-01T00:00:10, 12.21.2.102, GET, /assets/img/hero_100.jpg, 157121, 0',
    '2019-01-01T01:00:11, 12.21.1.101, GET, /assets/js/loader.js, 102, 1',
]

'''
Part 1
Generate a report showing the number of accesses to each asset. Display the report in sorted order by showing the most popular assets first.

Expected Output
Asset, Count
/assets/js/loader.js, 2
/assets/img/hero_100.jpg, 1

'''


def display_access_report(access_logs):
    # Implementation starts here
    list_assets=[]
    for row_log in access_logs:
        row_log_list=row_log.split(',')
        list_assets.append(row_log_list[3])      # Extracting the URI Path
    dict_assets={uri: list_assets.count(uri) for uri in list_assets}          #Dictionary comprehension
    sorted_d = sorted(dict_assets.items(), key=lambda x: x[1],reverse=True)
    print(sorted_d)
    print("Problem # 1: Assets count for each URI ")
    print("Asset, Count")
    for k,v in sorted_d:
        print('{} {}'.format(k,v))


display_access_report(access_logs)

'''
Part 2
Generate a report showing the number of cache hits   to each timestamps.

(a)Cache Hits
Timestamp, Count
2019-01-01T01:00:01, 2
2019-01-01T01:00:03.jpg, 1

(b)Cache Misses
Timestamp, Count
2019-01-01T01:00:02, 2
2019-01-01T01:00:04.jpg, 1

'''
def display_access_report2(access_logs):
    # Implementation starts here
    time_stamp=[]
    cache=[]
    for row_log in access_logs:
        row_log_list=row_log.split(',')
        time_stamp.append(row_log_list[0])
        cache.append(int(row_log_list[5]))
    cache_hit=list(filter(lambda pair: pair[1] == 1,zip(time_stamp,cache)))
    cache_miss=list(filter(lambda pair: pair[1] == 0,zip(time_stamp,cache)))
    dict_cache_hit={bool[0]: cache_hit.count(bool) for bool in cache_hit}
    print("Problem # 2(a): Cache Hits")
    print("Timestamp, Count")
    for k,v in dict_cache_hit.items():
        print('{} {}'.format(k,v))
    dict_cache_miss={bool[0]: cache_miss.count(bool) for bool in cache_miss}
    print("Problem # 2(b): Cache Misses")
    print("Timestamp, Count")
    for k,v in dict_cache_miss.items():
        print('{} {}'.format(k,v))

#Call a functions
display_access_report2(access_logs)




'''
Part 3
Generate a report showing the bytes transferred  to each destination.

Bytes Transferred to destination
IPs, Bytes Transferred
'12.21.1.107': 102,
'12.21.1.104': 157121

'''
def display_access_report3(access_logs):
    # Implementation starts here
    ips=[]
    bytes=[]
    for row_log in access_logs:
        row_log_list=row_log.split(',')
        ips.append(str(row_log_list[1]))
        bytes.append(int(row_log_list[4]))
    zip_data=list(zip(ips,bytes))
    dict_bytes_transfer={}
    for dest_ip in set(ips):
        dest_ip_list=filter(lambda pair:pair[0]==dest_ip,zip_data)
        dest_ip_list_arr=[dest_ip_list[l][1] for l  in range(len(dest_ip_list))]
        dict_bytes_transfer[dest_ip]= sum(dest_ip_list_arr)
    print("Problem # 3: Bytes Transferred to destination")
    print("IPs, Bytes Transferred")
    for k,v in dict_bytes_transfer.items():
      print('{} {}'.format(k,v))u_liu_listst    

display_access_report3(access_logs)