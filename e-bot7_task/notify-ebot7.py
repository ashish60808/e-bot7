import json,pymongo,re,smtplib

report={'user':'','status code':''}
list_report=[]
  
def access_report(log_file):
  user=[]
  status=[] 
  dict_status={} 
  for line in log_file:
    match=re.search(r'(^\d+.\d+.\d+.\d+)\s-\s(\w+)\s\[(.+)\]\s"\w+\s(.+)\sHTTP/\d+.\d+"\s(401)\s(\d+)\s"(\D)"\s"(.+)"\s"',line)
    if match:
        user.append(match.group(2))
        status.append(match.group(5))
    zip_data=list(zip(user,status))
  for u in set(user):
    u_list=list(filter(lambda pair:pair[0]==u,zip_data))
    dict_status[u_list[0][0]]=len(u_list)
  print(dict_status)
  for k,v in dict_status.items():
    if v>=1:
      msg=f'{k} attempted wrong athetication {v} times.' 
      print(msg)
      # send_mail(msg)


def send_mail(message):
  sender = 'server@fromdomain.com'
  receivers = ['admin@todomain.com']

  message = """From: From Person <server@fromdomain.com>
  To: To Person <admin@todomain.com>
  Subject: SMTP e-mail test

  you have attempted more than 10 wrong passwords.
  """

  try:
     smtpObj = smtplib.SMTP('localhost')
     smtpObj.sendmail(sender, receivers, message)         
     print("Successfully sent email")
  except SMTPException:
     print("Error: unable to send email")

if __name__ == '__main__':
  log_file = open("/home/nginx/log/host.access.log", "r")
  access_report(log_file)