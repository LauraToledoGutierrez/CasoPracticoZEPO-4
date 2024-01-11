from django.http import JsonResponse
import itertools
import string

# Bruteforce_attack
def bruteforce_attack(target_password):
    charset = string.ascii_lowercase
    attempts = 0

    for current_length in range(1, len(target_password) + 1):
        for attempt in itertools.product(charset, repeat=current_length):
            attempts += 1
            if ''.join(attempt) == target_password:
                return attempts
    return attempts

# The view that will connect to a URL, show the results
def attack_view(request, password):
    attempts = bruteforce_attack(password)
    return JsonResponse({
        "-----": "ZEPO Practical Case 4 -> Brute Force Attack",
        "message": f"Password cracked in {attempts} attempts. The password is {password}."
    })
