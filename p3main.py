"""
COMPSCI 424 Program 3
Name: Alek Ekstrand
"""

import os
import sys
import threading  # standard Python threading library
import random

# (Comments are just suggestions. Feel free to modify or delete them.)

# When you start a thread with a call to "threading.Thread", you will
# need to pass in the name of the function whose code should run in
# that thread.

# If you want your variables and data structures for the banker's
# algorithm to have global scope, declare them here. This may make
# the rest of your program easier to write. 
#  
# Most software engineers say global variables are a Bad Idea (and 
# they're usually correct!), but systems programmers do it all the
# time, so I'm allowing it here.

# Global data structures for the Banker's Algorithm
num_resources = 0
num_processes = 0
Available = []
Max = []
Allocation = []
Need = []
Total = []

# Lock for thread synchronization
lock = threading.Lock()

def check_initial_conditions():
    global num_resources, num_processes, Available, Max, Allocation, Need, Total

    # Initialize the Total list
    Total = [0] * num_resources

    # Check condition 1: Allocation <= Max for all processes and resources
    for i in range(num_processes):
        for j in range(num_resources):
            if Allocation[i][j] > Max[i][j]:
                print(f"Error: Allocation[{i}][{j}] > Max[{i}][{j}]")
                return False

    # Check condition 2: Sum of allocations + Available = Total
    for j in range(num_resources):
        total_allocated = sum(Allocation[i][j] for i in range(num_processes))
        Total[j] = total_allocated + Available[j]

    # Check if the system is in a safe state
    if not is_safe_state():
        print("Error: The system is not in a safe state")
        return False

    return True

def is_safe_state():
    global num_resources, num_processes, Available, Max, Allocation, Need

    Work = Available.copy()
    Finish = [False] * num_processes

    for i in range(num_processes):
        Need[i] = [Max[i][j] - Allocation[i][j] for j in range(num_resources)]

    safe_sequence = []

    while True:
        found = False
        for i in range(num_processes):
            if not Finish[i]:
                can_allocate = True
                for j in range(num_resources):
                    if Need[i][j] > Work[j]:
                        can_allocate = False
                        break

                if can_allocate:
                    safe_sequence.append(i)
                    Finish[i] = True
                    for j in range(num_resources):
                        Work[j] += Allocation[i][j]
                    found = True

        if not found:
            break

    return sum(Finish) == num_processes

def process_request(process_id, request):
    global Available, Allocation, Need

    with lock:
        can_allocate = True
        for j in range(num_resources):
            if request[j] > Need[process_id][j]:
                can_allocate = False
                break

        if can_allocate:
            if is_safe_state():
                for j in range(num_resources):
                    Available[j] -= request[j]
                    Allocation[process_id][j] += request[j]
                    Need[process_id][j] -= request[j]
                print(f"Process {process_id} requests {request}: granted")
            else:
                print(f"Process {process_id} requests {request}: denied")
        else:
            print(f"Process {process_id} requests {request}: denied")

def process_release(process_id, release):
    global Available, Allocation

    with lock:
        for j in range(num_resources):
            if release[j] > Allocation[process_id][j]:
                print(f"Process {process_id} cannot release {release}")
                return

        for j in range(num_resources):
            Available[j] += release[j]
            Allocation[process_id][j] -= release[j]

        print(f"Process {process_id} releases {release}")

def manual_mode():
    while True:
        command = input("Enter a command (request I of J for K, release I of J for K, or end): ")
        if command == "end":
            break

        parts = command.split()
        if parts[0] == "request":
            process_id = int(parts[-1])
            resource_id = int(parts[-3])
            amount = int(parts[1])
            request = [0] * num_resources
            request[resource_id] = amount
            process_request(process_id, request)
        elif parts[0] == "release":
            process_id = int(parts[-1])
            resource_id = int(parts[-3])
            amount = int(parts[1])
            release = [0] * num_resources
            release[resource_id] = amount
            process_release(process_id, release)
        else:
            print("Invalid command")

def automatic_mode():
    def process_thread(process_id):
        for _ in range(3):
            request = [random.randint(0, Max[process_id][j]) for j in range(num_resources)]
            process_request(process_id, request)

            release = [random.randint(0, Allocation[process_id][j]) for j in range(num_resources)]
            process_release(process_id, release)

    threads = []
    for i in range(num_processes):
        thread = threading.Thread(target=process_thread, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


def main():
    global num_resources, num_processes, Available, Max, Allocation, Need

    if len(sys.argv) < 3:
        sys.stderr.write("Not enough command-line arguments provided, exiting.")
        sys.exit(1)

    mode = sys.argv[1]
    setup_file_path = sys.argv[2]

    with open(setup_file_path, 'r') as setup_file:
        num_resources = int(setup_file.readline().split()[0])
        num_processes = int(setup_file.readline().split()[0])

        setup_file.readline()  # Skip "Available" line
        Available = [int(x) for x in setup_file.readline().split()]

        setup_file.readline()  # Skip "Max" line
        Max = [[0 for j in range(num_resources)] for i in range(num_processes)]
        for i in range(num_processes):
            Max[i] = [int(x) for x in setup_file.readline().split()]

        setup_file.readline()  # Skip "Allocation" line
        Allocation = [[0 for j in range(num_resources)] for i in range(num_processes)]
        for i in range(num_processes):
            Allocation[i] = [int(x) for x in setup_file.readline().split()]

    Need = [[0 for j in range(num_resources)] for i in range(num_processes)]

    if check_initial_conditions():
        if mode == "manual":
            manual_mode()
        elif mode == "auto":
            automatic_mode()
        else:
            print("Invalid mode specified")
    else:
        print("Initial conditions are not met")

if __name__ == "__main__":
    main()