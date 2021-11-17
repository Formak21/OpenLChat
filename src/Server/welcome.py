# welcome message
VERSION = '1.0'
with open(file='welcome.txt', mode='r', encoding='utf-8') as f:
    print(f.read().format(VERSION))