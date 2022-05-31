# PV207_jBPM

## Prerequisites
- installed and running [Docker](https://www.docker.com/)
- installed `docker-compose`

# Steps to prepare project
1. `git clone https://github.com/Riqardos/PV207_Project.git`
2. `docker-compose build`
3. `docker-compose up -d`
4. go to http://localhost:8080/business-central/, sign in, and create RichardSpace and CarRental project
5. `cd PV207_jBPM`
6. `git remote add business-central ssh://wbadmin@localhost:8001/RichardSpace/CarRental`
7. `git push business-central master` 

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

# to show logs run 
docker logs -f --tail 100 jbpm-server-full

## Some useful commands
```
# to add jBPM remote
git remote add business-central ssh://wbadmin@localhost:8001/TestSpace/TestProject

# to pull project from jBPM
git pull business-central master 

# to push project to jBPM
git push business-central master 

# to push to our repo
git push origin master 
```


