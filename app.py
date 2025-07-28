from flask import Flask, render_template, request
from collections import defaultdict, deque

from models import db, Station, Line, LineStation, Connection
from stations import line1, line1_2, line2, line3, line4, line4_2, line5, line6, line7

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///metro.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# داده‌ها
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

# ساخت گراف مترو (دیکشنری از ایستگاه‌ها به لیست (همسایه، خط))
metro_graph = defaultdict(list)
station_lines = defaultdict(set)

def build_graph():
    global metro_graph, station_lines
    metro_graph.clear()
    station_lines.clear()

    stations = {s.id: s for s in Station.query.all()}
    for conn in Connection.query.all():
        metro_graph[conn.from_id].append((conn.to_id, conn.line))
        metro_graph[conn.to_id].append((conn.from_id, conn.line))
        station_lines[conn.from_id].add(conn.line)
        station_lines[conn.to_id].add(conn.line)

def find_paths(start_station, end_station):
    start_id = start_station.id
    end_id = end_station.id
    queue = deque()
    visited = dict()
    for line in station_lines[start_id]:
        queue.append((start_id, [(start_id, line)], line, 0))
    results = []
    while queue:
        current, path, current_line, changes = queue.popleft()
        if current == end_id:
            results.append((path, changes))
            continue
        state = (current, current_line)
        length = len(path)
        if state in visited:
            prev_changes, prev_len = visited[state]
            if changes > prev_changes or (changes == prev_changes and length >= prev_len):
                continue
        visited[state] = (changes, length)
        for neighbor, neighbor_line in metro_graph[current]:
            new_changes = changes + (neighbor_line != current_line)
            queue.append((neighbor, path + [(neighbor, neighbor_line)], neighbor_line, new_changes))
    if not results:
        return None
    min_changes = min(r[1] for r in results)
    candidates = [r for r in results if r[1] == min_changes]
    best_path, best_changes = min(candidates, key=lambda x: len(x[0]))
    for path, changes in results:
        if changes > best_changes and len(path) + 5 <= len(best_path):
            best_path, best_changes = path, changes
    return best_path

@app.route('/', methods=['GET', 'POST'])
def home():
    stations = Station.query.order_by(Station.fa).all()
    route_info = None

    if request.method == 'POST':
        start_fa = request.form['start']
        end_fa = request.form['end']
        start_station = Station.query.filter_by(fa=start_fa).first()
        end_station = Station.query.filter_by(fa=end_fa).first()
        if not start_station or not end_station:
            route_info = ["❌ ایستگاه‌ها نامعتبرند."]
        else:
            route = find_paths(start_station, end_station)
            if not route:
                route_info = ["❌ مسیر پیدا نشد."]
            else:
                stations_map = {s.id: s for s in Station.query.all()}
                route_info = []
                for i in range(len(route) - 1):
                    current_id, current_line = route[i]
                    next_id, next_line = route[i + 1]
                    current_station = stations_map[current_id]
                    next_station = stations_map[next_id]
                    if current_line != next_line:
                        route_info.append(f"🛑 تعویض خط در ایستگاه {current_station.fa} (از {current_line} به {next_line})")
                    route_info.append(f"از {current_station.fa} ({current_line}) به {next_station.fa} ({next_line})")
                route_info.append(f"✅ رسیدی به {stations_map[route[-1][0]].fa}")

    return render_template('home.html', stations=stations, route_info=route_info)


def initialize_db():
    with app.app_context():
        db.drop_all()
        db.create_all()

        station_map = {}

        # وارد کردن خطوط و ایستگاه‌ها
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

        # ساخت جدول connections از روی line_stations (ایستگاه‌های پشت سر هم)
        for line in Line.query.all():
            line_stations = LineStation.query.filter_by(line_id=line.id).order_by(LineStation.station_order).all()
            for i in range(len(line_stations) - 1):
                from_station_id = line_stations[i].station_id
                to_station_id = line_stations[i + 1].station_id
                # اتصال دو طرفه (فقط یکبار ذخیره می‌کنیم چون گراف غیر جهتیه)
                exists = Connection.query.filter(
                    ((Connection.from_id == from_station_id) & (Connection.to_id == to_station_id)) |
                    ((Connection.from_id == to_station_id) & (Connection.to_id == from_station_id))
                ).first()
                if not exists:
                    conn = Connection(from_id=from_station_id, to_id=to_station_id, line=line.name)
                    db.session.add(conn)
        db.session.commit()

        # ساخت گراف
        build_graph()
        print("✅ دیتابیس آماده و گراف ساخته شد.")


if __name__ == '__main__':
    initialize_db()
    app.run(debug=True)
