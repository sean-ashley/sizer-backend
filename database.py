from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy

conn_str = "cockroachdb://sean:sizristhebest@dopey-bison-8cc.gcp-northamerica-northeast1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&sslrootcert=dopey-bison-ca.crt"

#create sqlalchemy engine
engine = create_engine(conn_str)

try:
    #connect to engine
    connection = engine.connect()
    print("Connected")
except:
    print("Connection failed")