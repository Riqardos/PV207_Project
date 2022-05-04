# PV207_jBPM

## Prerequisites
- installed and running [Docker](https://www.docker.com/)

# This showcase image contains default users and roles:
```
USER        PASSWORD    ROLE
*************************************************
wbadmin     wbadmin     admin,analyst,user,process-admin,kie-server
krisv       krisv       admin,analyst,user,process-admin,kie-server
john        john        analyst,Accounting,PM,kie-server
sales-rep   sales-rep   analyst,sales,kie-server
katy        katy        analyst,HR,kie-server
jack        jack        analyst,IT,kie-server
```

## Some useful commands
```
# pull and run docker web app should be running on http://localhost:8080/business-central/ 
# first run can take a while
docker run -p 8080:8080 -p 8001:8001 -d --name jbpm-server-full jboss/jbpm-server-full:latest

# to show logs run 
docker logs -f --tail 100 jbpm-server-full

# to add jBPM remote
git remote add business-central ssh://wbadmin@localhost:8001/TestSpace/TestProject

# to pull project from jBPM
git pull business-central master 

# to push project to jBPM
git push business-central master 

# to push to our repo
git push origin master 
```


