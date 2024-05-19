import time

start_time = time.perf_counter()
for i in range(100):
    import XMLtoYAML
print('0: ', time.perf_counter() - start_time)

start_time = time.perf_counter()
for i in range(100):
    import XMLtoYAMLwLib
print('1: ', time.perf_counter() - start_time)

start_time = time.perf_counter()
for i in range(100):
    import task2
print('2: ', time.perf_counter() - start_time)

start_time = time.perf_counter()
for i in range(100):
    import main
print('3: ', time.perf_counter() - start_time)

start_time = time.perf_counter()
for i in range(100):
    import XMLtoRTF
print('5: ', time.perf_counter() - start_time)
