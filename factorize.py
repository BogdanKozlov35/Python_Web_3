from time import time
from multiprocessing import Pool, cpu_count, Process



def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


if __name__ == '__main__':

    numbers = [128, 255, 99999, 10651060]

    start_time = time()
    for n in numbers:
        end_time = time()
        print(f" speed: {round((end_time - start_time), 10)} for {n} {factorize(n)}")

    print(f" Count CPU: {cpu_count()}")

    # Pool
    pool = Pool(cpu_count())
    async_start_time = time()
    result_async = pool.map(factorize, numbers)
    async_end_time = time()
    pool.close()
    pool.join()
    print("Pool Async results:", result_async)
    print("Pool Async time:", round(async_end_time - async_start_time, 10))

    # Process
    for n in numbers:
        process_start_time = time()
        pr = Process(target=factorize, args=(n,))
        pr.start()
        pr.join()
        process_end_time = time()

    print("Process Async results:", pr)
    print("Process Async time:", round(process_end_time - process_start_time, 10))
