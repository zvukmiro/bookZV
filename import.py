import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

f = open("books.csv")
reader = csv.reader(f)

for isbn, title, author, year in reader:
    db.execute("INSERT INTO books(isbn, title, author, year) VALUES (:isbn, :title, :author, :year)", {"isbn":isbn, "title":title, "author":author, "year":year})
db.commit()

f.close()
db.close()

""" file used to create a database on Heroku web site, by populating the table books, with the info from the file books.csv"""
