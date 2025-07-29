from flask import Flask, render_template, request
from collections import defaultdict, deque

from models import db, Station, Line, LineStation, Connection
from stations import line1, line1_2, line2, line3, line4, line4_2, line5, line6, line7

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///metro.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

line_names_translations = {
    "خط 1": "Line 1",
    "خط1 بخش 2": "Line 1 - Part 2",
    "خط 2": "Line 2",
    "خط 3": "Line 3",
    "خط 4": "Line 4",
    "خط 4 بخش دوم": "Line 4 - Part 2",
    "خط 5": "Line 5",
    "خط 6": "Line 6",
    "خط 7": "Line 7",
}

def translate_line_name(line_name, lang):
    if lang == 'en':
        return line_names_translations.get(line_name, line_name)
    return line_name

# داده‌ها
lines_data = [
    ("خط 1", line1),
    ("خط1 بخش 2", line1_2),
    ("خط 2", line2),
    ("خط 3", line3),
    ("خط 4", line4),
    ("خط 4 بخش دوم", line4_2),
    ("خط 5", line5),
    ("خط 6", line6),
    ("خط 7", line7),
]

# ساخت گراف مترو و نگهداری اطلاعات جهت حرکت قطار در هر خط
metro_graph = defaultdict(list)  # key=station_id, value=list of (neighbor_id, line_name)
station_lines = defaultdict(set)  # station_id -> set of line_names
line_station_orders = {}  # (line_name, station_id) -> order index in line

def build_graph():
    global metro_graph, station_lines, line_station_orders
    metro_graph.clear()
    station_lines.clear()
    line_station_orders.clear()

    stations = {s.id: s for s in Station.query.all()}
    # ذخیره ترتیب ایستگاه‌ها در هر خط
    for line in Line.query.all():
        line_stations = LineStation.query.filter_by(line_id=line.id).order_by(LineStation.station_order).all()
        for ls in line_stations:
            line_station_orders[(line.name, ls.station_id)] = ls.station_order

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

def get_train_direction(line_name, current_station_id, next_station_id):
    # بررسی ترتیب ایستگاه‌ها در خط و تعیین جهت حرکت قطار
    order_current = line_station_orders.get((line_name, current_station_id))
    order_next = line_station_orders.get((line_name, next_station_id))
    if order_current is None or order_next is None:
        return None
    if order_next > order_current:
        return "به سمت انتهای خط"  # فارسی
    else:
        return "به سمت ابتدای خط"

def get_train_direction_en(line_name, current_station_id, next_station_id):
    order_current = line_station_orders.get((line_name, current_station_id))
    order_next = line_station_orders.get((line_name, next_station_id))
    if order_current is None or order_next is None:
        return None
    if order_next > order_current:
        return "towards end of line"
    else:
        return "towards start of line"

@app.route('/', methods=['GET', 'POST'])
def home():
    lang = request.args.get('lang', 'fa')
    stations = Station.query.order_by(Station.fa).all()
    route_info = None
    start_fa = None
    end_fa = None

    # برای ذخیره order ایستگاه‌ها در خطوط (جهت پیدا کردن ابتدا و انتهای خط)
    global line_station_orders
    if 'line_station_orders' not in globals():
        line_station_orders = {}
        for ls in LineStation.query.all():
            line_station_orders[(ls.line.name, ls.station_id)] = ls.station_order

    def get_line_end_stations(line_name):
        # گرفتن ایستگاه اول و آخر خط با توجه به order
        stations_in_line = [(station_id, order) for (ln, station_id), order in line_station_orders.items() if ln == line_name]
        if not stations_in_line:
            return None, None
        stations_sorted = sorted(stations_in_line, key=lambda x: x[1])
        return stations_sorted[0][0], stations_sorted[-1][0]

    if request.method == 'POST':
        start_fa = request.form['start']
        end_fa = request.form['end']
        start_station = Station.query.filter_by(fa=start_fa).first()
        end_station = Station.query.filter_by(fa=end_fa).first()
        if not start_station or not end_station:
            route_info = ["❌ ایستگاه‌ها نامعتبرند."] if lang == 'fa' else ["❌ Invalid stations."]
        else:
            route = find_paths(start_station, end_station)
            if not route:
                route_info = ["❌ مسیر پیدا نشد."] if lang == 'fa' else ["❌ No route found."]
            else:
                stations_map = {s.id: s for s in Station.query.all()}
                route_info = []

                # --- شروع مسیر: تعیین جهت حرکت قطار ---
                start_line = route[0][1]
                start_station_id = route[0][0]
                first_station_id, last_station_id = get_line_end_stations(start_line)
                # بررسی اینکه قطار به سمت کدام سمت حرکت می‌کند
                if len(route) > 1 and route[1][0] == first_station_id:
                    direction_station_id = last_station_id
                else:
                    direction_station_id = first_station_id

                direction_station_name = stations_map[direction_station_id].fa if lang == 'fa' else stations_map[direction_station_id].en
                start_station_name = stations_map[start_station_id].fa if lang == 'fa' else stations_map[start_station_id].en

                if lang == 'fa':
                    route_info.append(
                        f"🚉 مسیر را از ایستگاه {start_station_name} در {translate_line_name(start_line, lang)} شروع کنید؛ "
                        f"قطار به سمت ایستگاه {direction_station_name} را سوار شوید."
                    )
                else:
                    route_info.append(
                        f"🚉 Start at {start_station_name} on {translate_line_name(start_line, lang)}; "
                        f"board the train towards {direction_station_name}."
                    )

                # --- گام‌های مسیر ---
                for i in range(len(route) - 1):
                    current_id, current_line = route[i]
                    next_id, next_line = route[i + 1]
                    current_station = stations_map[current_id]
                    next_station = stations_map[next_id]
                    name_current = current_station.fa if lang == 'fa' else current_station.en
                    name_next = next_station.fa if lang == 'fa' else next_station.en

                    # اگر خط عوض شد
                    if current_line != next_line:
                        # اعلام تعویض خط
                        if lang == 'fa':
                            route_info.append(f"🛑 تعویض خط در ایستگاه {name_current} (از {translate_line_name(current_line, lang)} به {translate_line_name(next_line, lang)})")
                        else:
                            route_info.append(f"🛑 Line change at {name_current} (from {translate_line_name(current_line, lang)} to {translate_line_name(next_line, lang)})")

                        # تعیین جهت قطار خط جدید
                        first_station_id, last_station_id = get_line_end_stations(next_line)

                        if (i + 2) < len(route):
                            next_next_station_id = route[i + 2][0]
                            if next_next_station_id == first_station_id:
                                direction_station_id = last_station_id
                            else:
                                direction_station_id = first_station_id
                        else:
                            direction_station_id = last_station_id

                        direction_station_name = stations_map[direction_station_id].fa if lang == 'fa' else stations_map[direction_station_id].en

                        if lang == 'fa':
                            route_info.append(f"🚉 پس از تعویض، قطار به سمت ایستگاه {direction_station_name} را سوار شوید.")
                        else:
                            route_info.append(f"🚉 After changing line, board the train towards {direction_station_name}.")

                    # پیام گام مسیر (حرکت از ایستگاه فعلی به بعدی)
                    if lang == 'fa':
                        route_info.append(f"از {name_current} ({translate_line_name(current_line, lang)}) به {name_next} ({translate_line_name(next_line, lang)})")
                    else:
                        route_info.append(f"From {name_current} ({translate_line_name(current_line, lang)}) to {name_next} ({translate_line_name(next_line, lang)})")

                # پیام پایان مسیر
                final_station = stations_map[route[-1][0]]
                final_station_name = final_station.fa if lang == 'fa' else final_station.en
                route_info.append("✅ رسیدی به " + final_station_name if lang == 'fa' else "✅ Arrived at " + final_station_name)
                print("Current language:", lang)

    return render_template(
        'home.html',
        stations=stations,
        route_info=route_info,
        selected_start=start_fa,
        selected_end=end_fa,
        lang=lang
    )


def initialize_db():
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

        for line in Line.query.all():
            line_stations = LineStation.query.filter_by(line_id=line.id).order_by(LineStation.station_order).all()
            for i in range(len(line_stations) - 1):
                from_station_id = line_stations[i].station_id
                to_station_id = line_stations[i + 1].station_id
                exists = Connection.query.filter(
                    ((Connection.from_id == from_station_id) & (Connection.to_id == to_station_id)) |
                    ((Connection.from_id == to_station_id) & (Connection.to_id == from_station_id))
                ).first()
                if not exists:
                    conn = Connection(from_id=from_station_id, to_id=to_station_id, line=line.name)
                    db.session.add(conn)
        db.session.commit()
        build_graph()
        print("✅ دیتابیس آماده و گراف ساخته شد.")

def get_line_end_stations(line_name):
    # پیدا کردن ایستگاه‌های اول و آخر خط
    line_stations = [station_id for (ln, station_id), order in line_station_orders.items() if ln == line_name]
    if not line_stations:
        return None, None
    # مرتب کردن بر اساس order
    sorted_stations = sorted(
        ((station_id, line_station_orders[(line_name, station_id)]) for station_id in line_stations),
        key=lambda x: x[1]
    )
    start_station_id = sorted_stations[0][0]
    end_station_id = sorted_stations[-1][0]
    return start_station_id, end_station_id

if __name__ == '__main__':
    initialize_db()
    app.run(debug=True)
