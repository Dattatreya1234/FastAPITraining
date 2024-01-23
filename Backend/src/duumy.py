from datetime import datetime

cur=datetime.now()

date_string = "2024-01-22T04:13:43.483000Z"
# datetime_object = datetime.fromisoformat(date_string)
a=datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%fZ")
print(type(a))
print(a)
