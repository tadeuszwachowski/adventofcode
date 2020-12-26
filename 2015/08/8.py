with open('input.txt') as file:
    f = file.read().splitlines()

enc = 0
lon = 0
sho = 0
for line in f:
    lon += len(line)
    decoded_string = bytes(line[1:-1], "utf-8").decode("unicode_escape")
    sho += len(decoded_string)

    encoded_string = str(line.encode("utf-8"))[1:].replace("\"", "\\\"")
    enc += len(encoded_string)
    
print('Part 1:', lon-sho)
print('Part 2:', enc-lon)

    # print(decoded_string)