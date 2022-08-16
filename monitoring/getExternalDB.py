import fdb

con = fdb.connect(host='172.21.80.1',
                  port=3050,
                  database='C:/Database/AMIRS_3-test.FDB',
                  user='SYSDBA',
                  password='masterkey',
                  sql_dialect=3,
                  charset='WIN1251')
cur = con.cursor()
cur.execute('''SELECT COUNT("OID") FROM "ExternalSystemLogRecord" WHERE "LogMessage" LIKE 'Создана квитанция о подтверждении%';''')
for result in cur:
    print(result)

con.close()