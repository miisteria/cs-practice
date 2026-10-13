def read_rows(lines):
    rows = []
    header = None

    for line in lines:
        line = line.strip()
        if line == "":
            continue

        parts = line.split(",")
        parts = [part.strip() for part in parts]

        if header is None:
            header = parts
            continue

        if len(parts) != len(header):
            continue

        row = {}
        for i in range(len(header)):
            row[header[i]] = parts[i]

        rows.append(row)

    return rows


def count_types(rows):
    counts = {}

    for row in rows:
        kind = row["тип"]

        if kind not in counts:
            counts[kind] = 0

        counts[kind] += 1

    return counts


def total_minutes(rows, kind):
    total = 0.0

    for row in rows:
        if row["тип"] == kind:
            try:
                minutes = float(row["минуты"].replace(",", "."))
            except ValueError:
                continue

            total += minutes

    return round(total, 1)


def to_csv(counts):
    result = "тип,количество\n"

    for kind in sorted(counts):
        result += f"{kind},{counts[kind]}\n"

    return result