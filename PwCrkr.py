import itertools
import time
import os

# Kullanıcının tahmin etmek istediği şifreyi giriş olarak alın.
# Take the password that the user wants to guess as input.
u_pwd = input("Enter a password: ")

# Şifre oluşturmak için kullanılacak karakterlerin listesi.
# List of characters to be used to create a password.
chrs = ['a','b','c','ç','d','e','f','g','ğ','h','ı','i','j','k','l','m','n','o','ö','p','q','r','s','ş','t','u','ü','v','w','x','y','z',
        'A','B','C','Ç','D','E','F','G','Ğ','H','I','İ','J','K','L','M','N','O','Ö','P','Q','R','S','Ş','T','U','Ü','V','W','X','Y','Z',
        '1','2','3','4','5','6','7','8','9','0','.',',','!','>','£','^','#','+','$','%','½','&','/','{','(','[',')',']','=','}','*','?',
        '\ ','-','_','|','@',':',';','~','â','ß','Â']

# Şifre tahminleri başlatılıyor.
# Initiating password guesses.
attempt_count = 0
start_time = time.time()

# Şifre uzunluğunu 1 ila 4 karakter arasında değiştirmek için döngü.
# Loop to change the password length from 1 to 4 characters.
for lenght in range(len(u_pwd)): 
    for guess in itertools.product(chrs, repeat=len(u_pwd)):
        attempt_count += 1
        pw = ''.join(guess) # Oluşturulan tahminleri birleştirin.
        print(pw)

        if pw == u_pwd:
            end_time = time.time()
            elapsed_time = end_time - start_time
            # Şifreyi bulduğunuzda ekrana yazdırın.
            # When you find the password, print it on the screen.
            print("Your Password Is: ", pw)
            print("Attempt Count: ", attempt_count)
            print("Elapsed Time: ", elapsed_time, "Seconds.")
            exit()
            # Şifreyi bulduktan sonra programı sonlandırın.
            # End the programme after finding the password.

# Şifreyi bulamazsa ekrana bir mesaj yazdırın.
# Print a message on the screen if it cannot find the password.
print("Password not found!")
