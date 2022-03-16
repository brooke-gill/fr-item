print('enter product name (spell it correctly!!): ')
x = input()
print('section?')
y = input()

import requests
import re

# Fill in your details here to be posted to the login form.
payload = {
    'uname': '1F618',
    'pword': 'cGFzc3dvcmQ='
}

# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    my_cookies = {'_lr_geo_location': 'US',
              '52d78755b5ffee3d8f6ef44edc309e5dbdbc6140': 'eyJpdiI6IitJZW9RNHpFUHdxaTBrWkRFZTc5REE9PSIsInZhbHVlIjoiWTJKbU1sUldjMkpJZUhwSlVrcFFPWGRhV2xKVWNVVjVibXczU1V0RGFIZ3lUMDl0Um1kV1JUQnFRVEJxY2tWb1FuaExSbkp4ZFVadlpVUllUREpaU2pkb1R6UkJLMjk1VVdkMFlVSXZjREUwY0RBNWFIUjBhRk5sVm05U2JHSk9jSEZ2Wm5GaGFucE5RaXQ2TlU1VFRUUTJOU3N4SzBWeVVIVkZZbVF2UTJkdFYzRjBUekV6WTNoalRYWnNTMVowWjJNclNUaE9kM2gwT1ZGcmJGTlpSMWREWjJzM2VHVjZjMVY1ZUVoM1FWZHRialUwWkVKb1JERXJTVFZSV1hwQlNsSkdTMHMxUTFCSWRIaHZNVzB6YVRGTFdubElVRXRXVEV4elYwRkZNak4wTldNeGFuUXZNbXRsU1d4TVpEbHdMMnhzU1hoaGJXZERjbm8yTVVGSVVGTlZUVnA2ZUM5T1FUbHVWWE5aYjNCdlltRTRVWGt3YUc5T2VEZzNORkp1VlVwUVJVVlFWbTB6VEdKR1dYRllRaTh6V1ZwQ1JqRjNSRTUwVjB0WFNucGxiVEV2T0cwNU4wUk5WVXB0VUVSTGJYaGFUWGx3Y0c5NFFtNVNLMUJ0VG1OeWNFMXFjVGx4WTA5M09FMUtNV1ZGUkRoQ05IaE9lRUp3WkRCaFVWVmhaVTE1UWtsR2JURnNUWEpaU1RCM00yZDRUbEZ0ZDFKVWVHZzNVelF4Tkc1RmVISnFMMkYyUVd0c1UydHFXR2hwY25sdVIydHJLM3BYVmtGcFdUaGllQT09IiwibWFjIjoiMGJhY2MwNTFkZTA4NTJhN2U2MTA3MmJkMDE2YzU4YzBkMzkxOTdiYWY4OTE5ZTJlMThkZjI0M2IxMDU4MTg1OCJ9',
              'fr_session': 'eyJpdiI6ImN3SlZIdmJ4Q2JTNTIyRDFvcFljTXc9PSIsInZhbHVlIjoiWldsVVVFWjNTMDByZW1GUlJsRmxUMDl0T0hKS1EzTmtiekJoUjFOTFdWVnpjMk40YjJaNE5FVkNXa3BrTWxWbUwwbGFZelpsTmt0b2NETkJUV1IwSzNwNFpXTjNVamx6YlVWUFp6UkpNM05FYzNKcGFtaHZhbVYyVGpZMFYwaGlhWGhpVWtOV1F6ZDJSV3M5IiwibWFjIjoiMjEzMDA1NWYyMGIyNmI4NDVhNmUwZGY3MWJiYzBkNWViOGM3N2ZiMjQyYzk5OGY1Y2FkN2UwNTI5MWU4ZWUzMyJ9',
              'frs': '25aa4800ad32dc6aa3d289648dde581382c97f7213a75a404ab238806bb1f6fd'}
            
    requests.utils.add_dict_to_cookiejar(s.cookies, my_cookies)
    r = s.get(('https://www1.flightrising.com/auction-house/buy/realm/' + y + '?itemname=' + x  + '&collapse=1'), headers={'Cache-Control': 'no-cache'})
    htmlbasic = (r.text)

reg_str = "<img class=\"ah-listing-currency-icon\" src=\"/static/layout/icon_gems.png\"> <strong>(.*?)</strong>"
res = re.findall(reg_str, htmlbasic)
  
# printing result
print("lowest BIN of 1x " + x + ": " + res[0] + "g")