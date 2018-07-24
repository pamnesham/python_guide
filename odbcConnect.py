import pyodbc
import pandas as pd


#This function makes the connection to a database. DSN is the name of the database.
def querytoDF(sql,dsn,username,password):
    connectString = 'DSN={0};Uid={1};Pwd={2};'.format(dsn,username,password)
    connection = pyodbc.connect(connectString)
    data = pd.read_sql(sql,connection)
    df = data.applymap(lambda x : x.lower() if type(x) == str else x)
    connection.close()
    return df


def main():
# write your SQL here
    sql = """
        SELECT *
        FROM table
        WHERE ROWNUM <=2

        """
   # enter database name, lanID, password
    df = querytoDF(sql,'database','ID','password')



if __name__ == '__main__':
    main()


#Type TNSPing in the command line to get more info on your database.
