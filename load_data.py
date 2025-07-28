from flask import Flask
from models import db, Station, Line, LineStation
from stations import line1, line1_2, line2, line3, line4, line4_2, line5, line6, line7
print("Line1 count:", len(line1))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///metro.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

lines_data = [
    ("line1", line1),
    ("line1(2)", line1_2),
    ("line2", line2),
    ("line3", line3),
    ("line4", line4),
    ("line4(2)", line4_2),
    ("line5", line5),
    ("line6", line6),
    ("line7", line7),
]

with app.app_context():
    db.drop_all()
    db.create_all()

    station_map = {}

    for line_name, stations in lines_data:
        line = Line(name=line_name)
        db.session.add(line)
        db.session.commit()

        for order, station in enumerate(stations):
            key = (station.fa, station.en)
            if key not in station_map:
                db_station = Station(fa=station.fa, en=station.en)
                db.session.add(db_station)
                db.session.commit()
                station_map[key] = db_station.id
            station_id = station_map[key]
            db.session.add(LineStation(line_id=line.id, station_id=station_id, station_order=order))

    db.session.commit()
    print("✅ اطلاعات با موفقیت وارد دیتابیس شد.")
