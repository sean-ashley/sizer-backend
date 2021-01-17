from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy

conn_str = "cockroachdb://sean:sizristhebest@free-tier.gcp-us-central1.cockroachlabs.cloud:26257/snappy-bear-200.defaultdb?sslmode=verify-full&sslrootcert=cc-ca.crt"

#create sqlalchemy engine
engine = create_engine(conn_str)

try:
    #connect to engine
    connection = engine.connect()
    print("Connected")
except:
    print("Connection failed")