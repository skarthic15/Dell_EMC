# Dell_EMC

Note : Please select any 5 questions from this list.
 
1) Let’s assume a linux machine has a product installed which includes 3 services namely db_service, app_service and web_service
a. Lets say there is a dependency in the order of service starting. For a proper working of the product, db_service should be started first and then app_service followed by a web_service (db_service > app_service > web_service). So if the app_service requires a restart then app_service is restarted first and then web_service be restarted, but not db_service.
b. Using ansible handlers write a program to check the status of each service and if some service is found stopped, restart only the required services in a proper order.
 
 
2)You have been provided with the list of users below.
Use /home/automation/plays/vars/user_list.yml file to save this content.
---
users:
  - username: alice
    uid: 1201
  - username: vincent
    uid: 1202
  - username: sandy
    uid: 2201
  - username: patrick
    uid: 2202
Create a playbook /home/automation/plays/users.yml that uses the vault file /home/automation/plays/secret.yml to achieve the following:
    Users whose user ID starts with 1 should be created on servers in the webservers host group. User password should be used from the user_password variable.
    Users whose user ID starts with 2 should be created on servers in the database host group. User password should be used from the user_password variable.
              All users should be members of a supplementary group wheel.
              Shell should be set to /bin/bash for all users.
              Account passwords should use the SHA512 hash format.
              Each user should have an SSH key uploaded (use the SSH key that you created previously, see task #2).
 
After running the playbook, users should be able to SSH into their respective servers without passwords.
 
 
3) Create a role called sample-apache and store it in /home/automation/plays/roles. The role should satisfy the following requirements:
The httpd, mod_ssl and php packages are installed. Apache service is running and enabled on boot.
              Firewall is configured to allow all incoming traffic on HTTP port TCP 80 and HTTPS port TCP 443.
              Apache service should be restarted every time the file /var/www/html/index.html is modified.
              A Jinja2 template file index.html.j2 is used to create the file /var/www/html/index.html with the following content:
 
The address of the server is: IPV4ADDRESS
IPV4ADDRESS is the IP address of the managed node.
Create a playbook /home/automation/plays/apache.yml that uses the role and runs on hosts in the webservers host group.
 
 
4) Install a ubuntu VM on a given vsphere server, then install Postgres SQL and create a database with the below inputs.  (terraform)
 
Vsphere details:
vsphere user = admin
vsphere password = Iwiiap@13ns
vsphere server = 10.241.110.12
VM path = dc1/testvm/myguestvm1
 
Number of CPU = 4
Memory = 8 GB
HDD = 120 GB
 
Datacenter = dc1
datastore = dc1_datastore
 
PostgresSQL Details:
port: 23456
database: test_db
username: user1
password: Slkcpal@35
 
5) Create Python REST client program which queries http://api.open-notify.org/astros.json and list the user name in sorted order. Convert the REST JSON object to list<String> with JSON names in sorted order. (python)
 
6) Suppose I have "n" chocolates. and "m" children, if i want to distribute each chocolates to all m children in a sequential order by repeating same list of children if excess. how do you distribute? (python)
    example1: if n=3 (chocolates here is 3) , m=3 (children are 3 you can name it as 1,2,3 ) answer: 1:1,2:1,3:=1 
    example 2: if n=5 and m=7 then child 1:2, 2:2, 3:1, 4:1, 5:1
can you write a simple python function to resolve this? where n and m are parameters.