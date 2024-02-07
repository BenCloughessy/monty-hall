import random

options = [1, 2, 3]
num_success = 0
num_attempts = 10000

# Base success rate (without changing choices)
for _ in range(num_attempts):
    guest_choice = random.choice(options)
    prize_location = random.choice(options)

    if guest_choice == prize_location:
        num_success += 1

base_success_rate = num_success/num_attempts

print(f"base success rate: {base_success_rate}")

num_success = 0
# New success rate (change selection after one option removed)
for _ in range(num_attempts):
    original_options = [1, 2, 3]  # Reset options for each attempt
    guest_choice = random.choice(original_options)
    prize_location = random.choice(original_options)

    # Simulate removing one wrong option that is not the guest's choice (if possible)
    if guest_choice != prize_location:
        temp_options = [option for option in original_options if option != guest_choice and option != prize_location]
    else:
        temp_options = [option for option in original_options if option != guest_choice]
    
    removed_option = random.choice(temp_options)
    new_options = [option for option in original_options if option != removed_option]

    # Assume the guest always switches to the remaining option
    new_guest_choice = None
    for option in original_options:
        if option != guest_choice and option != removed_option:
            new_guest_choice = option
            break


    if new_guest_choice == prize_location:
        num_success += 1

new_success_rate = num_success / num_attempts
print(f"new success rate: {new_success_rate}")