import json
import urllib.request

API_URL = 'https://api-flash.zczc.cz/export/github-flash-archive-project'
FLASH_KEYS = ["sha256", "size", "original", "ref"]

raw_info = json.loads(urllib.request.urlopen(API_URL).read())

# sort ref key
for info in raw_info:
    info["ref"] = dict(sorted(info["ref"].items()))

# process info
flash_info = {info['sha256']: {key: info[key] for key in FLASH_KEYS} for info in raw_info}
screenshots_info = {info['sha256']: info['screenshots'] for info in raw_info if 'screenshots' in info}

# sort dict key
flash_info = dict(sorted(flash_info.items()))
screenshots_info = dict(sorted(screenshots_info.items()))

with open('flash.json', mode='w') as f:
    json.dump(flash_info, f, indent=4, ensure_ascii=False)

with open('screenshots.json', mode='w') as f:
    json.dump(screenshots_info, f, indent=4, ensure_ascii=False)