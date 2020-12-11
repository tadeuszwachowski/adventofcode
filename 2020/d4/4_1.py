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
            # print(fields)
            # print(fields.keys(), len(fields.keys()), 'cid' not in fields.keys())
            if (len(fields.keys()) == 8) or (len(fields.keys()) == 7 and 'cid' not in fields.keys()):
                
                valid += 1
                fields = {}
print("Valid passports:", valid)