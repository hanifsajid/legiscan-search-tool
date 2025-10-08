import json
import csv
from io import StringIO

def build_full_query(query: str, status: str, chamber: str, bill_type: str, intro_date: str, action_date: str) -> str:
    filters = []
    if status:
        filters.append(f"status:{status}")
    if chamber:
        filters.append(f"chamber:{chamber}")
    if bill_type:
        filters.append(f"type:{bill_type}")
    if intro_date.strip():
        filters.append(f"intro:{intro_date.strip()}")
    if action_date.strip():
        filters.append(f"action:{action_date.strip()}")

    if filters:
        return f"({query}) AND " + " AND ".join(filters)
    return query


def prepare_download(data: list, format: str) -> tuple:
    # Returns (bytes content, extension string, mime string)
    if format == "json":
        content = json.dumps(data, indent=2, ensure_ascii=False)
        return content.encode("utf-8"), "json", "application/json"

    # else CSV
    output = StringIO()
    all_keys = sorted({k for d in data for k in d.keys()})
    writer = csv.DictWriter(output, fieldnames=all_keys)
    writer.writeheader()
    writer.writerows(data)
    return output.getvalue().encode("utf-8"), "csv", "text/csv"