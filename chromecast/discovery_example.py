

import sys

import pychromecast

casts, browser = pychromecast.get_chromecasts()
# Shut down discovery as we don't care about updates
browser.stop_discovery()
if len(casts) == 0:
    print("No Devices Found")
    sys.exit()

print("Found cast devices:")
print(casts)