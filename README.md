Course Code & Name:	CMPT 756-Distributed & Cloud Systems \
Semester:			Spring 2023 \
Project Group:		5 \
Group Members:		Shung Ho Jonathan Au, Hossain Mahbub, Min Fei, Zipeng Liang,
Chifeng Wen
## Project Title: 
# Comparing Serverless and Serverful Performance for An Application Using Microservices Architecture

Our project aim is to examine the performance difference between the serverless and serverful implementation of a map application. This map application allows users to modify and navigate across a randomly generated directed graph. The application serves two functions: navigation query (read operation) and map information update (write operation), with the assumption that the read frequency is 10 times greater than write. We will develop on Amazon AWS to leverage its cloud services including Elastic Beanstalks, SQS, Lambda, and RDS. The map navigator service can directly access the database. The map update service pushes an update into a queue where it will be materialized by the batch update module. To compare the serverless and serverful implementation of map application, the performance metrics that we will monitor are Response Time (amount of time to respond to a request) and Throughput (number of queries it can perform in a given time interval).



