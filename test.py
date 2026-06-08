import oracledb

try:
    connection = oracledb.connect(
        user="system",
        password="1234",
        dsn="localhost/XE"
    )
    print("Connected successfully 🎉")

except Exception as e:
    print("Error:", e)