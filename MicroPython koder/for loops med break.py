from time import sleep
a = 102
for i in range(a):
    print(i)
    if i > 99:
        break
    sleep(0.1)

if i == 100:
    for i in range(0, 100, 4):
        print(i)
        sleep(0.1)
