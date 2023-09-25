import sh
import json
from pprint import pprint



data = json.loads(sh.terraform("output", "-json"))
ip = data.get('ipv4')['value']


with open('../Management/inventory', 'w') as f:
        f.write(ip)