def find_loop(public_key):
    ini = 1
    loop = 0
    while True:
        loop += 1
        ini = (ini*7) % 20201227
        if ini == public_key:
            break
    return loop

def secret(public_key,loop):
    key = 1
    for _ in range(loop):
        key = (key*public_key) % 20201227
    return key

def main():
    card_pub = 12578151
    card_loop = find_loop(card_pub)
    
    door_pub = 5051300
    door_loop = find_loop(door_pub)

    print(card_loop,door_loop)
    
    enc_key = secret(door_pub,card_loop)
    print(enc_key)
    enc_key = secret(card_pub,door_loop)
    print(enc_key)
    
if __name__ == "__main__":
    main()