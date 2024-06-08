num_processes = int(input('Enter number of processes: '))
arrival_times = []
req_times = []

print("Enter arrival times:")
for i in range(num_processes):
    arrival = int(input(f"P{i}: "))
    arrival_times.append(arrival)

print('Enter request times:')
for i in range(num_processes):
    burst = int(input(f"P{i}: "))
    req_times.append(burst)

quantum = int(input('Enter time quantum: '))


processes = []
for i in range(num_processes):
    processes.append([f'P{i}', arrival_times[i], req_times[i]])




def round_robin(processes, quantum):
    n = len(processes)
    remaining_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    total_waiting_time = 0
    total_turnaround_time = 0
    time = 0

    # copying burst times
    for i in range(n):
        remaining_time[i] = processes[i][2]

    # simulating round robin 
    while True:
        done = True
        for i in range(n):
            if remaining_time[i] > 0:
                done = False
                if remaining_time[i] > quantum:
                    time += quantum
                    remaining_time[i] -= quantum
                    print(f'P{i}', end=' ')
                else:
                    time += remaining_time[i]
                    waiting_time[i] = time - processes[i][1] - processes[i][2]
                    remaining_time[i] = 0
                    turnaround_time[i] = time
                    print(f'P{i}', end=' ')
        if done:
            break

    # calculating total waiting time and turnaround time
    for i in range(n):
        total_waiting_time += waiting_time[i]
        total_turnaround_time += turnaround_time[i]

    # calculating average waiting time and turnaround time
    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n

    return avg_waiting_time, avg_turnaround_time

avg_waiting_time, avg_turnaround_time = round_robin(processes, quantum)

print("\n Average Waiting Time:", avg_waiting_time)
print("Average Turn around Time:", avg_turnaround_time)
