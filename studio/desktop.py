from functional import compute, construct, prepare, measure
from tools import icons, folders, records

k = icons.get_memory()
j = folders.get_record()
i = records.get_history()

a, b, c, d = compute(k), construct(i), prepare(j), measure(".")

###### INTERFACE ######
last_seen = []
recent_visit = []
all_visits = []
all_scenes = []
###### DASHBOARD ######
phases = []
optimizations = []
loops = []
solved = []
