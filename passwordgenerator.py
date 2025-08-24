#import necessary libraries
import random
import math

#data
PHILOSOPHERS = [
    {'Name': 'Plato', 'City': 'Athens', 'School': 'Epistemology', 'Year': -428},
    {'Name': 'Aristotle', 'City': 'Athens', 'School': 'Peripatetic', 'Year': -384},
    {'Name': 'Socrates', 'City': 'Athens', 'School': 'Classical', 'Year': -470},
    {'Name': 'Haraclitus', 'City': 'Ephesus', 'School': 'Ionian',  'Year': -500},
    {'Name': 'Diogenes', 'City': 'Sinope', 'School': 'Cynicism', 'Year': -413},
    {'Name': 'Lucretius', 'City': 'Rome', 'School': 'Epicureanism', 'Year': -99},
    {'Name': 'Cicero', 'City': 'Arpinum', 'School': 'Scepticism', 'Year': -106},
    {'Name': 'Seneca', 'City': 'Corduba', 'School': 'Stoicism', 'Year': -4},
    {'Name': 'Aurelius', 'City': 'Rome', 'School': 'Stoicism', 'Year': -121},
    {'Name': 'Epictetus', 'City': 'Hierapolis', 'School': 'Stoicism', 'Year': -135}
]
SYMBOLS = ["!", "@", "#", "$", "%", "^", "&", "*", "?", ";"]

#creating mix of upper and lowercase letters
def randomize_case(text):
    result = ""
    for c in text:
        if random.choice([True, False]):
            result += c.upper()
        else:
            result += c.lower()
    return result

#Generating password
def generate_password(max_len=15):
    Philosopher = random.choice(PHILOSOPHERS)
    year = Philosopher['Year']
    school = Philosopher['School']
    symbol = random.choice(SYMBOLS)
    nums = [
        int(abs(math.sqrt(abs(year)))),
        int(abs(year)) % 100,  # duże liczby sprowadzone do max 2 cyfr
        int(math.pi*10) % 100,
        int(math.e*10) % 100,
        abs(int(math.sin(year)*100)) % 100,
        abs(int(math.cos(year)*100)) % 100
    ]
    number = random.choice(nums)
    number_str = f"{number:02d}"

    name = randomize_case(Philosopher['Name'])
    city = randomize_case(Philosopher['City'])
    school = randomize_case(Philosopher['School'])

    password = name + symbol + city + symbol + number_str + symbol + school
    return password[:max_len]

#creating multiple password
def generate_multiple_passwords(n=5, min_len = 15, max_len=30):
    results = []
    for _ in range(n):
        h = generate_password(max_len)
        results.append(h)
    return results

#saving password in local folder
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
local_path = os.path.join(script_dir, "password.txt") 

def save_password(password):
    with open(local_path, "a", encoding="utf-8") as f:
        f.write(password + "\n")
    print(f"Passwords created: {password}")

#output
if __name__ == "__main__":
    passwords = generate_multiple_passwords(10, 20)
    print("Generated password suggestions:")
    for h in passwords:
        print(h)
        save_password(h)


