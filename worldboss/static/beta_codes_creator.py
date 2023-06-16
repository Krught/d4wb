import random
import string

number_of_codes = 5


def generate_beta_code(length=10):
    characters = string.ascii_letters + string.digits
    beta_code = ''.join(random.choices(characters, k=length))
    return beta_code

beta_code = []
current_num = 0
while current_num < number_of_codes:
    beta_code.append(generate_beta_code())
    current_num += 1

print("INSERT INTO master_app_betacode (code, used) VALUES")
current_num = 0
for i in beta_code:
    if current_num + 1 >= number_of_codes:
        print("('" + str(i) + "', False);") 
    else:
        print("('" + str(i) + "', False),") 
    current_num += 1