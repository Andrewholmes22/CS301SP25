import time
import csv
import random

def stopwatch(func, *args):
    start = time.perf_counter()
    func(*args)
    end = time.perf_counter()
    return (end - start) * 1e6


def write_to_csv(filename, data):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Data Structure", "Operation", "Size", "Time Taken in Ms"])
        writer.writerows(data)


def test_list_operations(sizes):
    results = []
    for size in sizes:
        testlist = list(range(size))
        
        results.append(["List", "Insert Beginning", size, stopwatch(testlist.insert, 0, -1)])

        results.append(["List", "Insert Middle", size, stopwatch(testlist.insert, size//2, -1)])

        results.append(["List", "Insert End", size, stopwatch(testlist.append, -1)])

        results.append(["List", "Delete Beginning", size, stopwatch(testlist.pop, 0)])

        results.append(["List", "Delete Middle", size, stopwatch(testlist.pop, size//2)])

        results.append(["List", "Delete End", size, stopwatch(testlist.pop)])

        results.append(["List", "Membership Test", size, stopwatch(lambda: -1 in testlist)])

    return results

def test_dict_operations(sizes):
    results = []
    for size in sizes:
        testdict = {i: i for i in range(size)}
        
        results.append(["Dict", "Insert", size, stopwatch(testdict.__setitem__, size, -1)])

        results.append(["Dict", "Delete", size, stopwatch(testdict.__delitem__, size//2)])

        results.append(["Dict", "Membership Test", size, stopwatch(lambda: -1 in testdict)])

    return results
sizes=[10,100,1000,10000,100000]  
list_results = test_list_operations(sizes)
dict_results = test_dict_operations(sizes)

write_to_csv("data.csv", list_results + dict_results)
print("Data written to data.csv")