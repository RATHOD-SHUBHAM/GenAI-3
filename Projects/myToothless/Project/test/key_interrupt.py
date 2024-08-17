import time
try:
    for i in range(1, 10):
        print(i)
        time.sleep(10)

except KeyboardInterrupt:
    print('done')