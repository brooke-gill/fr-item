from enum import auto
import string
import requests
import re

validcat = 0
print("-----------------")
print("| FLIGHT RISING |")
print("| PRICE CHECKER |")
print("-----------------")
print()
while (2 == 2):
    while validcat == 0:
        x = input('Enter a product name: ').lower()
        if x == "exit":
            print("Quitting...")
            quit()
        y = input('Category: ').lower()
        validcat = 0
        res = ['0']
        punishment = 0
        results = 0
        yeahright = ""
        if y in ['f','foodstuffs','foods','fo','m','materials','mat','ma','a','apparel','apparels','cosmetics','appa','ap','d','drag','drags','dragon','dr','familiars','fa','familiar','companion','b','bat','combat','fight','fighting','battles','coliseum','ba','sk','skin','s','sp','spec','special','o','misc','others','ot','food','mats','app','fam','battle','skins','specialty','other','trinket','trinkets','chest']:
            validcat = 1
            y_long = y
            if y in ['f','foodstuffs','foods','fo']:
                y = "food"
                y_long = "food"
            if y in ['m','materials','mat','ma']:
                y = "mats"
                y_long = "materials"
            if y in ['a','apparel','apparels','cosmetics','appa','ap']:
                y = "app"
                y_long = "apparel"
            if y in ['d','drag','drags','dragon','dr']:
                validcat = 0
                y_long = "dragons"
                print("this currently doesn't support dragons, sorry! :(")
                print()
            if y in ['familiars','fa','familiar','companion']:
                y = "fam"
                y_long = "familiars"
            if y in ['b','bat','combat','fight','fighting','battles','coliseum','ba']:
                y = "battle"
                y_long = "battle"
            if y in ['sk','skin']:
                y = "skins"
                y_long = "skins"
            if y in ['s','sp','spec','special']:
                y = "specialty"
                y_long = "specialty"
            if y in ['o','misc','others','ot','trinket','trinkets','chest']:
                y = "other"
                y_long = "other"
        if validcat == 0:
            print("You didn't specify a valid category!")
            print("Valid categories:")
            print("- [f]ood")
            print("- [m]aterials")
            print("- [a]pparel")
            print("- [d]ragons")
            print("- [fa]miliars")
            print("- [b]attle")
            print("- [sk]ins")
            print("- [s]pecialty")
            print("- [o]ther")
            print()
    validcat = 0

    def get_stuff(link, currency):
        r = s.get(link, headers={'Cache-Control': 'no-cache'})
        htmlbasic = (r.text)
        reg_str = "<img class=\"ah-listing-currency-icon\" src=\"/static/layout/icon_" + currency + ".png\"> <strong>(.*?)</strong>"
        res = re.findall(reg_str, htmlbasic)
        reg_str2 = "Results: <strong>(.*?)</strong>"
        res2 = re.findall(reg_str2, htmlbasic)
        reg_str3 = "data-name=\"(.*?)\""
        res3 = re.findall(reg_str3, htmlbasic)
        return [res, res2, res3]

    # Use 'with' to ensure the session context is closed after use.
    with requests.Session() as s:
        my_cookies = {'_lr_geo_location': 'US',
                '52d78755b5ffee3d8f6ef44edc309e5dbdbc6140': 'eyJpdiI6IitJZW9RNHpFUHdxaTBrWkRFZTc5REE9PSIsInZhbHVlIjoiWTJKbU1sUldjMkpJZUhwSlVrcFFPWGRhV2xKVWNVVjVibXczU1V0RGFIZ3lUMDl0Um1kV1JUQnFRVEJxY2tWb1FuaExSbkp4ZFVadlpVUllUREpaU2pkb1R6UkJLMjk1VVdkMFlVSXZjREUwY0RBNWFIUjBhRk5sVm05U2JHSk9jSEZ2Wm5GaGFucE5RaXQ2TlU1VFRUUTJOU3N4SzBWeVVIVkZZbVF2UTJkdFYzRjBUekV6WTNoalRYWnNTMVowWjJNclNUaE9kM2gwT1ZGcmJGTlpSMWREWjJzM2VHVjZjMVY1ZUVoM1FWZHRialUwWkVKb1JERXJTVFZSV1hwQlNsSkdTMHMxUTFCSWRIaHZNVzB6YVRGTFdubElVRXRXVEV4elYwRkZNak4wTldNeGFuUXZNbXRsU1d4TVpEbHdMMnhzU1hoaGJXZERjbm8yTVVGSVVGTlZUVnA2ZUM5T1FUbHVWWE5aYjNCdlltRTRVWGt3YUc5T2VEZzNORkp1VlVwUVJVVlFWbTB6VEdKR1dYRllRaTh6V1ZwQ1JqRjNSRTUwVjB0WFNucGxiVEV2T0cwNU4wUk5WVXB0VUVSTGJYaGFUWGx3Y0c5NFFtNVNLMUJ0VG1OeWNFMXFjVGx4WTA5M09FMUtNV1ZGUkRoQ05IaE9lRUp3WkRCaFVWVmhaVTE1UWtsR2JURnNUWEpaU1RCM00yZDRUbEZ0ZDFKVWVHZzNVelF4Tkc1RmVISnFMMkYyUVd0c1UydHFXR2hwY25sdVIydHJLM3BYVmtGcFdUaGllQT09IiwibWFjIjoiMGJhY2MwNTFkZTA4NTJhN2U2MTA3MmJkMDE2YzU4YzBkMzkxOTdiYWY4OTE5ZTJlMThkZjI0M2IxMDU4MTg1OCJ9',
                'fr_session': 'eyJpdiI6ImN3SlZIdmJ4Q2JTNTIyRDFvcFljTXc9PSIsInZhbHVlIjoiWldsVVVFWjNTMDByZW1GUlJsRmxUMDl0T0hKS1EzTmtiekJoUjFOTFdWVnpjMk40YjJaNE5FVkNXa3BrTWxWbUwwbGFZelpsTmt0b2NETkJUV1IwSzNwNFpXTjNVamx6YlVWUFp6UkpNM05FYzNKcGFtaHZhbVYyVGpZMFYwaGlhWGhpVWtOV1F6ZDJSV3M5IiwibWFjIjoiMjEzMDA1NWYyMGIyNmI4NDVhNmUwZGY3MWJiYzBkNWViOGM3N2ZiMjQyYzk5OGY1Y2FkN2UwNTI5MWU4ZWUzMyJ9',
                'frs': '25aa4800ad32dc6aa3d289648dde581382c97f7213a75a404ab238806bb1f6fd'}
                
        requests.utils.add_dict_to_cookiejar(s.cookies, my_cookies)

    gem_link = (('https://www1.flightrising.com/auction-house/buy/realm/' + y + '?itemname=' + x  + '&currency=1&collapse=1&sort=unit_cost_asc'))
    result = get_stuff(gem_link, "gems")
    
    if len(result[2]) > 0:
        autocorrect = (result[2])[0]
    else:
        result[0] = []
        autocorrect = x
        yeahright = "\""
    
    treasure_link = (('https://www1.flightrising.com/auction-house/buy/realm/' + y + '?itemname=' + autocorrect.lower()  + '&currency=0&collapse=1&sort=unit_cost_asc')) #to make the items sync

    if x.lower() != autocorrect.lower():
        print()
        print("NOTE: Flight Rising auto-completed your search to be \"" + (string.capwords(autocorrect, sep = None)) + "\".")
    if autocorrect[0].lower() in ['a','e','i','o','u']:
        top = ("------ PRICE OF AN " + yeahright + str(autocorrect).upper() + yeahright + " ------")
        print(top)
    else:
        top = ("------ PRICE OF A " + yeahright + str(autocorrect.upper()) + yeahright + " ------")
        print(top)
    print("Section: " + y_long.title())
    print()

    if len(result[0]) == 0:
        print("- Not on the Gem market!")
        punishment += 1
    else:
        print("Lowest price of 1x " + ((string.capwords(autocorrect, sep = None)) + ": " + "{:,}".format(float(f'{(float((result[0])[0])):g}')) + "g"))
        results += int((result[1])[0])
    
    result = get_stuff(treasure_link, "treasure")

    if len(result[0]) == 0:
        print("- Not on the Treasure market!")
        punishment += 1
    else:
        print("Lowest price of 1x " + (string.capwords(autocorrect, sep = None)) + ": " + str(("{:,}".format(round(float((result[0])[0])))) + "t"))
    #   print("Lowest price of 1x " + [the string in title case]                 + ": " + str(([add commas] [round]      [first n of result]+ "t"))
        results += int((result[1])[0])

    if punishment == 2:
        print("Did you spell the item correctly?")
    print()
    print(("{:,}".format(results)) + " items found")
    print("-" * len(top))
    print()
    print("Starting another search. Type \"exit\" to exit.")
    print()


'''
else:
    r = s.get(('https://www1.flightrising.com/auction-house/buy/realm/' + y + '?itemname=' + x  + '&collapse=1'), headers={'Cache-Control': 'no-cache'})
    htmlbasic = (r.text)
    reg_str = "<img class=\"ah-listing-currency-icon\" src=\"/static/layout/icon_treasure.png\"> <strong>(.*?)</strong>"
    res = re.findall(reg_str, htmlbasic)
    if len(res) > 0:
        print("lowest price of 1x " + x + ": " + res[0] + "t (" + str(round(float(res[0]))) + "g)")
    else:
        print("no matches found for \"" + x + "\" in the " + y + " category, sorry :(")
        '''
