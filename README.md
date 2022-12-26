
# DORIS SRO Locality Data API 
## Overview:
This project involves scraping data from Delhi Online Registration Information System and cleaning it to create a uniform database stored on Postgres server running on docker.
The postgres server was then integrated with a flask based REST API in order to query the data from the database.
This project includes data scraped from a delhi government website of different localities and SRO's the data scraped here contains 11000 plus entries of the registration numbers, area in square feet of the property, type of property.



## Run Locally

Clone the project

```bash
git clone git@github.com:Kathanbhavsar/propreturns-task-with-api.git
```

Go to the project directory

```bash
cd doris-sro-locality-with-api
```

Install dependencies


```bash
pip install -r requiremets.txt
```
Setting up the postgres docker container,
Pull the docker image
```bash
docker pull postgres
```
Run the docker command as follows in terminal to setup the postgres 
```bash
docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres
```

Then start the docker container
```bash
docker start postgresqldb
```
Access the shell of the postgres
```bash
docker exec -it [container ID] bash
```
Enter the psql command line
```bash
psql -h [localhost] -U [postgres]
```
Then create a database by giving the appropriate database name
```bash
create database [database_name];
```
## Deployment

Navigate to the postgres_write file and edit the conn_string with your database and password
```bash
conn_string = 'postgresql://[user]:[password]@:[host]/[dbname]'
```
You can also change the database table name as the file scraped will be stored in the table under that name in the postgres_write file
```bash
df.to_sql('[table name]', con=conn, if_exists='replace', index=False)
```
After installing all the dependencies run the main.py file. 
```bash
python main.py
```
After running the data scraped will be stored in the csv and if you have configured the database porperly it will save the scraped data into the postgresql

Lastly Navigate to the app.py script under the rest_api folder and type the following command in the terminal to run the flask app
```bash
flask run
```
The flask app will allow you to query the data that is stored in the postgres server



## API Reference


#### Get item

```http
GET http://127.0.0.1:5000/doris?id={id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. reg_no of item to fetch |

### Get Item/Items through custom Query

```http
GET http://127.0.0.1:5000/doris/execute
```



## Screenshots
API call with the reg_no
![GET method reg_id Screenshot](https://raw.githubusercontent.com/Kathanbhavsar/doris-sro-locality-with-api/main/Screenshot%202022-12-26%20at%203.03.06%20PM.png)
Custom-Query 
![GET method custom query Screenshot](https://raw.githubusercontent.com/Kathanbhavsar/doris-sro-locality-with-api/main/custom-query.png)


## 🔗 Links
[![Linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kathan-bhavsar-852b72192/)



## Authors

- [@Kathanbhavsar](https://github.com/Kathanbhavsar)

