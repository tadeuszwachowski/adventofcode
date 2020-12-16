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

            for entry in vals:
                field,data = entry.split(":")
                if field in expected:
                    fields[field] = data

            if (len(fields.keys()) == 8) or (len(fields.keys()) == 7 and 'cid' not in fields.keys()):
                
                valid += 1
                fields = {}
                
print("Valid passports:", valid)