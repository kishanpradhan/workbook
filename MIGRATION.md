# Migration Plan

# Goal
- Have one database and unify data
- Migrate Scala code to Python
- Single authentication system
- Decide on infra in AWS

## Have one database and unify data

**Time** : 1 month (While developing APIs, we might need to change the migration script/ schema)

So there are two databases which have differnet data and relations. In order to unify them, we need to find the relations between two datbaase tables.

After that we are going to create new schema where we can have our own roles/permissions in which way we want. 

Later we need to create migration scripts to get data from both databases and save to unified one.

Below are the tasks that we might follow

- Each developer will learn about the database schema.
- Have a meeting setup to discuss the relations between two dbs and creating new database schema
- After finalizing schema, we can divide works for migrations.

## Migrate Scala code to Python Django

**Time**: 1-2 months(This will be overrapling with DB migration script)

Since we have 2 systems with multiple APIs, first we need to list out all the APIs and merge any API that we can. Create postman for this.

After deciding on the schema, we need to start on creating models in Django and add the APIs.

## Single authentication system 

**Time**: 2 weeks (After deciding on schema, it will not take that much time)

Since we are creating one system, we don't need to have a seprate service for authentication. We have all data like company/teams/roles/permission in one system, 
so we can have this auth system in one of Django module too.

## Decide on infra in AWS

**Time**: 1 month (terraform setup one time and deployment script will take most of times)

To make it simple to create and deploy our service, we can just use EC2 instances and manage themm by devop tools.

To manage server, we can use `terraform`. This will be one time setup and next time we add more servers, we just have to run terraform and it will have all the services needed in that server.

To deploy or handle any services in all of servers, we can use `ansible`. This will let us deploy/restart/install any services in all of our servers.

We can have a load balancer server which will connect to all other servers as backend. We can use `nginx` as load balancer and also to run Django on all servers.
So when we add new server, terraform will create the server, install services and update nginx config in load balancer.

For database, it is good to use RDS as we won't have to manage the scalability and reliability which is important. 

For files, we can use AWS S3 storage.

We are going to dockorize the service. 

Since we are going to create our own authentication service, we won't be needing Cognito.

