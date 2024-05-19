import xmltodict
import yaml
start_time=time.perf_counter()
with open('schedule.xml', encoding='utf-8') as f:
    s = f.read()

xfile = xmltodict.parse(s)

with open('schedule.yaml', 'w', encoding='utf-8') as yfile:
    yaml.dump(xfile, yfile, default_flow_style=False, allow_unicode=True)
