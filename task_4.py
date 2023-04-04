import json
from datetime import datetime

with open('task4_input.txt', "r+") as json_file:
    data = json.load(json_file)
    if data["updated"]:
        data["updated"] = datetime.now().isoformat()
    open('task4_input.txt', 'w').close()
    json_file.write(str(data))
