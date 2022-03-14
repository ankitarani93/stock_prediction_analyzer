import pymysql

try:
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="password",
        db="stock_analysis"
    )
    cursor = connection.cursor()
    sql ="INSERT INTO `stock_details_static` (`symbol`, `shortName`, `sector`, `Country`) VALUES (%s,%s,%s,%s)"
    cursor.execute(sql, ('AAPLe','Apple','Tech','United States'))
    connection.commit()
   # Execute query
   #  sql = "SELECT * FROM `stock_details_static`"
   #  cursor.execute(sql)
   #  # Fetch all the records
   #  result = cursor.fetchall()
   #  for i in result:
   #      print(i)

except Error as e:
    print(e)

finally:
    # close the database connection using close() method.
    connection.close()