from datetime import datetime

# Original datetime string
original_datetime_str = "2025-01-22 20:11:48.698161+00:00"

# Parsing the datetime string
dt_object = datetime.fromisoformat(original_datetime_str)

# Formatting the datetime into the desired format
formatted_datetime = f"Date: {dt_object.strftime('%d/%m/%Y')}, Time: {dt_object.strftime('%H:%M')}"

print(formatted_datetime)
