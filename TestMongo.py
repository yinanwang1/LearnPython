import pymongo
import dbapi


gconn = pymongo.MongoClient('mongodb://192.168.30.172:3717')
gconn.bike_qa.authenticate('bike_qa', '2XDNNh6Tp82GneCywHcRJXFQJuYDQRyH', mechanism='SCRAM-SHA-1')
bike_location = location = gconn.bike_qa.d_bike_location
bike_move_record = gconn.bike_qa.d_bike_move_record


r = dict()
r["distance"] = 0
session = None
try:
    number = "3301000030"
    connection = "mysql+mysqldb://bike:QEj5edLxZDFlFZOh@192.168.30.173:3306/bike_qa?charset=utf8"
    session = dbapi.get_scoped_session(connection)
    bikes = list(bike_location.find({"_id": number}))
    if bikes:
        coordinate = bikes[0]["coordinate"]
        r.update(coordinate)
    else:
        r.setdefault("latitude", 30.288775)
        r.setdefault("longitude", 120.01496)
    sql = """select t1.id,t1.battery_id,t2.number as battery_number from d_bike t1 
    left join d_battery t2 on t1.battery_id = t2.id and t2.link_type=0 and t2.link_id=t1.id
    where t1.number = :number"""
    row = session.execute(sql, {"number": number}).fetchone()
    if row:
        r["id"] = row["id"]
        r["battery_id"] = row["battery_id"]
        r["battery_number"] = row["battery_number"]
        open('/tmp/d.log','a+').write(str(r['id'])+ '\n')
        records = list(bike_move_record.find({"bikeId": row["id"]}).sort([("addTime", -1)]).limit(1))
        open('/tmp/d.log','a+').write(str(records) +'\n')
        print("records")
        print(records)
        if records:
            record = records[0]
            r["distance"] = record["currentMileage"]
            r.update(record["coordinate"])
        sql = """select * from d_battery where id=:battery_id"""
        drow = session.execute(sql, {"battery_id": row["battery_id"]}).fetchone()
        if drow:
            r["power"] = drow["power"]
except:
    print("出现错误了")

if session:
    session.commit()

print("wyn text id is %s" % r['id'])
