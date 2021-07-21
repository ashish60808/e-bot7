The Challenge:
Basic docker application

 

Note: For docker images you may use anything that is available on docker hub. You may use the original images or build new images based on the originals as you see fit.

 

1.1 Simple web page

 

Create a docker image based on nginx which will serve a very simple web page. The contents of the page should be “Hello from e-bot7!”.

Secure the web app with HTTP basic auth. Add a user named admin with password e-bot7.

 ## Solution:
 > 1. nginx folder contains the conf/.htpasswd.secret file for Basic auth.
 
 > 2. Access logs are store in log/host.access.log
 
 > 3. Cutomize Nginx configuration is stored in conf/conf.d/e-bot7.conf
 
 > 4. Docker can run via docker-compose command.

1.2 Access logs to MongoDB

Each access to the page should result in the creation of a new document in the MongoDB collection named access. We want to save the user agent string, the date of the access and the response code.

 ## Solution:
> python code 'pushLogToMongo.py' has been developed which will get the logs from log/host.access.log and create the document and push them to mogoDB.

>> DataBase Name: ```ebot7```

>> Collection Name: ```access```

1.3 Notifications

Let's assume we want to be notified when the access was denied more than 10 times total, e.g. because the user entered the wrong password. Create a script that counts the number of access denials and sends an email to some address (you can send it to yourself for testing) if that number is above 10.

## Solution:
> python code 'notify-ebot7.py' has been developed which will which will get the logs from log/host.access.log and check for HTTP 401 status code and if that value exceed 10 Times it will trigger the Mail.

> >To run the code just execute ```python notify-e-bot7.py```

 

Note: the email might be rejected or marked as spam on the receiving end. Why would that happen and how could you mitigate it? (It's not necessary to fix this now since it might take up too much time, so just tell us what you would do.)
>Solutions:
>>We are not able to send the Mail from server becasue we donot have registered domain and SMTP server Setup.

>>To resolve that issue we can setup the SMTP server in our domain using which we can send the Mail.

 
The access-denied counter script should be run periodically. Create an image that runs the script once every 20 minutes.
 
 > we can run the notification python script using following commands.

 >> ```sudo docker build -t notify .```

 > To run the notification scripy every 20 minutes we can use the cron job .

 >> ```*/20 * * * *  docker run --rm -v `pwd`:/home -it   notify /home/notify-ebot7.py```

 

1.4 docker-compose file

Create a docker-compose file that manages the entire application described above. Running docker-compose up should start everything.

 ### Solution:
>>Folder caontains the file ```docker-compose.yml```
 

Submitting your work

 

When you are finished, you can submit your solution. Answer all questions mentioned above and optionally describe what you did and if there is anything else we should know before evaluating your solution. Package all relevant configuration files into a .tar.gz or .zip archive and upload it by using the provided link. Feel free to reach out to me if you are facing issues with the upload.

 

You should be able to do this in a couple of hours. Let me know how long it took for you.
