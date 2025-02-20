import hashlib

def find_adventcoin(secret_key, num_zeroes=5):
    prefix = '0' * num_zeroes
    number = 0
    while True:
        input_string = f"{secret_key}{number}"
        result_hash = hashlib.md5(input_string.encode()).hexdigest()
        if result_hash.startswith(prefix):
            return number
        
        number += 1

if __name__ == '__main__':
    secret_key = "bgvyzdsv"
    p1_answer = find_adventcoin(secret_key)
    print(p1_answer)
    p2_answer = find_adventcoin(secret_key, 6)
    print(p2_answer)
