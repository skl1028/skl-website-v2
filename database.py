from sqlalchemy import create_engine, text
import os

db_connection = os.environ['DB_CONNECTION']

engine = create_engine(
  db_connection,
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

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text("SELECT * FROM jobs WHERE id = :val"), 
      {"val": id}
    )
    row = result.first()
    if row is None:
      return None
    else:
      return dict(row._mapping)


def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, working_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :working_experience, :resume_url)")
    
    conn.execute(query, 
                   {"job_id": job_id,
                   "full_name": data['full_name'],
                   "email": data['email'],
                   "linkedin_url":data['linkedin_url'],
                   "education":data['education'],
                   "working_experience":data['working_experience'],
                   "resume_url":data['resume_url']})
      
    
