#project euler problem 16

import time

start = time.time()

answer = sum(map(int, str(2**1000)))
print(answer)

end = time.time()
print('time:',int(end-start))

