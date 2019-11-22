from pymysql import connect
import os

#connect python to SQL
connection = connect (
    host = os.getenv('MYSQL_HOST'),
    user = os.getenv('MYSQL_USER'),
    password = os.getenv('MYSQL_PASSWORD'),
    db = os.getenv('MYSQL_DATABASE'),
    charset = 'utf8mb4'
)

'''name = input ("enter name: ")

try:
    with connection.cursor() as cursor:
        query = f"INSERT INTO accounts (person_name, person_username, password) VALUES ('{name}', 'emailaddress@yahoo.com', 'password');"
        cursor.execute(query)
    connection.commit()

    with connection.cursor() as cursor:
        query = ("INSERT INTO account_details (person_name, customer_ID, account_ID, sort_code, balance) VALUES ('Shaz', '', '', 10-10-10, 10, 'password', 100)")
        cursor.execute(query)
    connection.commit()


    with connection.cursor() as cursor:
        query = 'SELECT * FROM db.account;'
        cursor.execute
        result = cursor.fetchall()
        print(result)'''

try:
    with connection.cursor() as cursor:
        query = f"INSERT INTO accounts (person_name, person_username, password) VALUES ('{name}', 'emailaddress@yahoo.com', 'password');"
        cursor.execute(query)
    connection.commit()


finally:
    connection.close()

