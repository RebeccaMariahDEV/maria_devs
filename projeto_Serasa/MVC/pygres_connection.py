import psycopg2

conn = psycopg2.connect(host="localhost", user="USERNAME", passwd="PASSWORD", dbname="maria_devs")

cursor = conn.cursor()

cursor.execute()

conn.comit()
cursor.close()
conn.close()

