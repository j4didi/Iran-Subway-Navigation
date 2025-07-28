from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Station(db.Model):
    __tablename__ = 'stations'
    id = db.Column(db.Integer, primary_key=True)
    fa = db.Column(db.String, nullable=False)
    en = db.Column(db.String, nullable=False)

class Line(db.Model):
    __tablename__ = 'lines'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

class LineStation(db.Model):
    __tablename__ = 'line_stations'
    line_id = db.Column(db.Integer, db.ForeignKey('lines.id'), primary_key=True)
    station_id = db.Column(db.Integer, db.ForeignKey('stations.id'), primary_key=True)
    station_order = db.Column(db.Integer, nullable=False)

    line = db.relationship('Line', backref='line_stations')
    station = db.relationship('Station', backref='line_stations')

class Connection(db.Model):
    __tablename__ = 'connections'
    id = db.Column(db.Integer, primary_key=True)
    from_id = db.Column(db.Integer, db.ForeignKey('stations.id'))
    to_id = db.Column(db.Integer, db.ForeignKey('stations.id'))
    line = db.Column(db.String(50))
