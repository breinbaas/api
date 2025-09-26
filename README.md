## run locally

python -m uvicorn main:app --reload

## install mongodb on chromebook (2025-10)

* curl -fsSL https://www.mongodb.org/static/pgp/server-7.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg --dearmor
* echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list
* sudo apt-get update
* sudo apt-get install -y mongodb-org
* sudo systemctl start mongod
* sudo systemctl enable mongod

## create the database

* sudo nano -w /etc/mongod.conf

```
security:
  authorization: enabled
```

* ```mongosh```
    * db.createUser({ user: "admin" , pwd: "password", roles: ["userAdminAnyDatabase", "dbAdminAnyDatabase", "readWriteAnyDatabase"]})
    * use leveelogic
    * db.user.insert({name: "Ada Lovelace", age: 205})
    


