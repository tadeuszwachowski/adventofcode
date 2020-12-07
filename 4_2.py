import re

def evaluate(d):
    if 'byr' in d.keys():
        if int(d['byr']) in range(1920,2002+1):
            pass
        else:
            return False
    if 'iyr' in d.keys():
        if int(d['iyr']) in range(2010,2020+1):
            pass
        else:
            return False
    if 'eyr' in d.keys():
        if int(d['eyr']) in range(2020,2030+1):
            pass
        else:
            return False
    if 'hgt' in d.keys():
        if 'cm' in d['hgt']:
            if int(d['hgt'].split("cm")[0]) in range(150,193+1):
                pass
            else:
                return False
        elif 'in' in d['hgt']:
            if int(d['hgt'].split("in")[0]) in range(59,76+1):
                pass
            else:
                return False
        else:
            return False
    if 'hcl' in d.keys():
        if "#" in d['hcl']:
            regex = r"[0-9a-f]{6}"
            if re.search(regex,d['hcl']).string == None:
                return False
            else:
                pass
        else:
            return False
    if 'ecl' in d.keys():
        if d['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth']:
            pass
        else:
            return False
    if 'pid' in d.keys():
        if len(d['pid']) == 9:
            regex = r"[0-9]*"
            if re.search(regex,d['pid']).string == None:
                return False
            else:
                pass
        else:
            return False
    return True

valid = 0
expected = [
    'byr','iyr','eyr','hgt','hcl','ecl','pid','cid'
]
with open("day4.txt","r") as file:
    fields = {}
    for line in file:
        if line == "\n":
            fields = {}
        else:
            vals = line.strip('\n').split(' ')
            # print(vals)
            for entry in vals:
                field,data = entry.split(":")
                if field in expected:
                    fields[field] = data
            
            if (len(fields.keys()) == 8) or (len(fields.keys()) == 7 and 'cid' not in fields.keys()):
                # print(fields.keys(), fields.values(), len(fields.keys()), 'cid' not in fields.keys())
                # print(fields, len(fields.keys()), "Good: ", evaluate(fields))

                if evaluate(fields) == True:
                    valid += 1
                fields = {}
print("Valid passports:", valid)