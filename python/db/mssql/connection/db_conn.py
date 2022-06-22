# The standard sys module has a platform object
from sys import platform

print("This systems platform is: " + platform)

print("If this fails we need to pip install pyodbc...")
import pyodbc as po
print("...Nope! Looks like it's found it!")


# Variables
server = 'db address'
database = 'database name'
username = 'admin'
password = 'password in plain text lol'
sql_driver = "ODBC Driver 17 for SQL Server"

# Prepare the stored procedure execution script and parameter values
storedProc = "Exec [Foo].[Bar] @SearchText = ?, @MaximumRowsToReturn = ?"
params = ("And", 10)


def mssql_execute():
    try:
        # Build the Auth string looks like:
        # DRIVER={'BLAH BLAH'};SERVER=localhost;DATABASE=blah;UID=user;PWD=pass
        con_string = 'DRIVER={' + sql_driver
        con_string += '};SERVER=' + server
        con_string += ';DATABASE=' + database
        con_string += ';UID=' + username
        con_string += ';PWD=' + password

        # Connection string
        cnxn = po.connect(con_string)
        cursor = cnxn.cursor()

        # Execute Stored Procedure With Parameters
        cursor.execute(storedProc, params)

        # Iterate the cursor
        row = cursor.fetchone()
        while row:
            # Print the row
            print(str(row[0]) + " : " + str(row[1] or ''))
            row = cursor.fetchone()

        # Close the cursor and delete it
        cursor.close()
        del cursor

        # Close the database connection
        cnxn.close()

    except Exception as e:
        print("Error: %s" % e)


if __name__ == "__main__":
    if platform == "linux" or platform == "linux2":
        # linux
        print("Running on Linux")
    elif platform == "darwin":
        # OS X
        print("Running on Mac")
    elif platform == "win32":
        # Windows...
        print("Running on Win")
    mssql_execute()
