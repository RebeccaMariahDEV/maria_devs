import psycopg2
from psycopg2.extras import RealDictCursor


conn = psycopg2.connect("dbname=curso_mvcad user=c80967a password=postgres "
                        "host=localhost")

conn.autocommit = True

cursor = conn.cursor(cursor_factory=RealDictCursor)

