import itertools
import time
import os

# Take the password that the user wants to guess as input.
u_pwd = input("Enter a password: ")

# List of characters to be used to create a password.
chrs = ['a','b','c','ç','d','e','f','g','ğ','h','ı','i','j','k','l','m',
        'n','o','ö','p','q','r','s','ş','t','u','ü','v','w','x','y','z',
        'A','B','C','Ç','D','E','F','G','Ğ','H','I','İ','J','K','L','M',
        'N','O','Ö','P','Q','R','S','Ş','T','U','Ü','V','W','X','Y','Z',
        '1','2','3','4','5','6','7','8','9','0','.',',','!','>','£','^',
        '#','+','$','%','½','&','/','{','(','[',')',']','"','','}','*']

# Initiating password guesses.
attempt_count = 0
start_time = time.time()

# Separate the password into groups of 3 characters.
password_groups = [u_pwd[i:i+3] for i in range(0, len(u_pwd), 3)]

# Loop through each group and attempt to guess the characters.
for password_group in password_groups:
    # Reset the attempt count for each group.
    attempt_count = 0

    for guess in itertools.product(chrs, repeat=len(password_group)):
        attempt_count += 1
        pw = ''.join(guess)

        if pw == password_group:
            # When you find the password group, print it on the screen.
            print("Password group found:", pw)

            # Reset the attempt count for the next group.
            attempt_count = 0

# Print the total number of attempts and the elapsed time.
end_time = time.time()
elapsed_time = end_time - start_time
print("Total attempts:", attempt_count)
print("Elapsed time:", elapsed_time, "seconds.")