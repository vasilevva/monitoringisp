import fdb

con = fdb.connect(host='192.168.31.188',
                  port=3050,
                  database='C:/database/AMIRS_3-test.FDB',
                  user='SYSDBA',
                  password='masterkey',
                  sql_dialect=3,
                  charset='WIN1251')
cur = con.cursor()
cur.execute('''SELECT COUNT(DISTINCT "ExternalQuery") FROM "ExternalSystemLogRecord" WHERE "LogMessage" LIKE 'Создана квитанция о подтверждении%';''')
for result in cur:
    print(result)
con.close()


#con = fdb.connect(host='172.16.0.123', port=3050, database='E:/database/AMIRS_3-test.FDB', user='SYSDBA', password='masterkey', sql_dialect=3, charset='WIN1251')
