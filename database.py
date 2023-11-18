from sqlalchemy import create_engine

db_connection_string = "mysql+pymysql://dfo8j20atq70zfbrdlz4:pscale_pw_xoFW4mmND7ByEGNM30NF6Y5Vsh3hhuCCzjjToFyRVjO@aws.connect.psdb.cloud/sklcareers?charset=utf8mb4"

engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })
