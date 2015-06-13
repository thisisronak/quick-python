import sqlite3

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def main():
  #init db
  tableCreate()

def tableCreate():
  c.execute("CREATE TABLE stuffToPlot (ID INT , unix REAL, datestamp TEXT, keyword TEXT, value REAL)")

def dataEntry():
  c.execute( "INSERT INTO stuffToPlot VALUES (1, 641294, 'jbfkbjkbfbsdfjb', 'ugerge', 48036) ")


if __name__ == "__main__" : main()