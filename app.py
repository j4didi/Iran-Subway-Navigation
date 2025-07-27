from collections import defaultdict, deque
from stations import *

metro_graph = defaultdict(list)
station_lines = defaultdict(set)

def add_line_to_graph(line, line_name):
    for i in range(len(line) - 1):
        metro_graph[line[i]].append((line[i + 1], line_name))
        metro_graph[line[i + 1]].append((line[i], line_name))
    for station in line:
        station_lines[station].add(line_name)

add_line_to_graph(line1, "line1")
add_line_to_graph(line1_2, "line1(2)")
add_line_to_graph(line2, "line2")
add_line_to_graph(line3, "line3")
add_line_to_graph(line4, "line4")
add_line_to_graph(line4_2, "line4(2)")
add_line_to_graph(line5, "line5")
add_line_to_graph(line6, "line6")
add_line_to_graph(line7, "line7")

def find_paths(start, end):
    queue = deque()
    visited = dict()

    for line in station_lines[start]:
        queue.append((start, [(start, line)], line, 0))

    results = []

    while queue:
        current, path, current_line, changes = queue.popleft()

        if current == end:
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
            new_changes = changes
            if neighbor_line != current_line:
                new_changes += 1
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

start_station = ghaem
end_station = tajrish

route = find_paths(start_station, end_station)

if not route:
    print("❌ مسیر پیدا نشد.")
else:
    for i in range(len(route) - 1):
        current_station, current_line = route[i]
        next_station, next_line = route[i + 1]

        if current_line != next_line:
            print(f"🛑 تعویض خط در ایستگاه {current_station.fa} (از {current_line} به {next_line})")

        print(f"از {current_station.fa} ({current_line}) به {next_station.fa} ({next_line})")

    print(f"✅ رسیدی به {route[-1][0].fa}")
