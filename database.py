from sqlalchemy import create_engine, text


db_connection_string = "mysql+pymysql://dfo8j20atq70zfbrdlz4:pscale_pw_xoFW4mmND7ByEGNM30NF6Y5Vsh3hhuCCzjjToFyRVjO@aws.connect.psdb.cloud/sklcareers?charset=utf8mb4"

engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })

def joblist_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    jobs = []
    for row in result.all():
      jobs.append(dict(row._mapping))
    return jobs
  
