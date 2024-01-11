import itertools
import string

def bruteforce_attack(password):
    charset = string.ascii_lowercase  
    attempts_count = 0

    for length in range(1, len(password) + 1):
        for attempt in itertools.product(charset, repeat=length):
            attempts_count += 1
            attempt_str = ''.join(attempt)
            print(attempt_str)  
            if attempt_str == password:
                return f"Password cracked in {attempts_count} attempts. The password is {password}."

if __name__ == "__main__":
    input_password = input("Input the password: ")
    result = bruteforce_attack(input_password)
    print(result)
