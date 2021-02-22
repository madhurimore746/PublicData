#!/usr/bin/env python3
import os
import time
import csv
import signal
import sys
import datetime

#file create
with open('validation.csv', mode='w') as csv_file:
    fieldnames = ['CPU_utilisation(%)', 'Total_memory(Mb)', 'Free_memory(Mb)','Used_memory(Mb)','buff/cache(Mb)','shared_memory(Mb)','Total_swapped_memory(Mb)','Free_swapped_memory(Mb)','Used swapped memory(Mb)']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

sec = float(raw_input("Enter the inputs : ") or "0.5")
def calculate():
    #function to calculate min, max and avg of used memory and cpu utilization
    with open('validation.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        cpu_total = 0
        used_memory = 0
        max_used_mem = []
        min_used_mem = []
        max_cpu_utilization = []
        min_cpu_utilization = []
        cnt = 0
        next(reader)     #used to skip header line from csv file
        for row in reader:
            cpu_total += float(row['CPU_utilisation(%)'])
            used_memory +=int(row['Used_memory(Mb)'])
            cnt += 1
            max_cpu_utilization.append(float(row['CPU_utilisation(%)']))
            min_cpu_utilization.append(float(row['CPU_utilisation(%)']))
            max_used_mem.append(int(row['Used_memory(Mb)']))
            min_used_mem.append(int(row['Used_memory(Mb)']))
                #print("============",max(max_used_mem))
                #print("=========",row)

        cpu_avg = cpu_total / cnt
        used_memory_avg = used_memory / cnt
            #max_used_mem.append(int(row['Used_memory']))
            #print("============",max_used_mem)

    print("max cpu utilization : ",max(max_cpu_utilization))
    print("min cpu utilization : ",min(min_cpu_utilization))
    print("max used memory : ",max(max_used_mem))
    print("min used memory : ",min(min_used_mem))
    print("Average of CPU utilization : ",cpu_avg)
    print("Average of used memory  : ",used_memory_avg)


def check_hardware_validation():    
    try: 
        time_start = time.time()
        after_xmin = 60
        after_ymin = 300
        after_zmin = 900
        while True:
            #Number of used core
            CPU_CHECK = os.popen("top -n1 | grep -iw '%Cpu(s)' | awk {'print $2'}")
            output_cpu_check = float(CPU_CHECK.read())
             
            #Total memory present on hardware 
            TOTAL_MEM_CHECK = os.popen("free -m | grep Mem: | awk {'print $2'}")
            output_total_memory_check = int(TOTAL_MEM_CHECK.read())

            #Free memory present on hardware
            FREE_MEM_CHECK = os.popen("free -m | grep Mem: | awk {'print $4'}")
            output_free_memory_check = int(FREE_MEM_CHECK.read())

            #Used memory on hardware
            USED_MEM_CHECK = os.popen("free -m | grep Mem: | awk {'print $3'}")
            output_used_memory_check = int(USED_MEM_CHECK.read())

            #buff/cache
            BUFFERED_MEM = os.popen("free -m | grep Mem: | awk {'print $6'}")
            output_buff_mem_check = int(BUFFERED_MEM.read())

            #shared memory
            SHARED_MEM = os.popen("free -m | grep Mem: | awk {'print $5'}")
            output_shared_mem_check = int(SHARED_MEM.read())

            #total swapped memory 
            TOTAL_SWAPPED_MEM_CHECK = os.popen("free -m | grep Swap: | awk {'print $2'}")
            output_swapped_total_memory_check = int(TOTAL_SWAPPED_MEM_CHECK.read())

            #Free swapped  memory present on hardware
            FREE_SWAPPED_MEM_CHECK = os.popen("free -m | grep Swap: | awk {'print $4'}")
            output_free_swapped_memory_check = int(FREE_SWAPPED_MEM_CHECK.read())

            #Used swapped  memory present on hardware
            USED_SWAPPED_MEM_CHECK = os.popen("free -m | grep Swap: | awk {'print $3'}")
            output_used_swapped_memory_check = int(USED_SWAPPED_MEM_CHECK.read())

            with open('validation.csv', mode='a') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writerow({'CPU_utilisation(%)':output_cpu_check, 'Total_memory(Mb)':output_total_memory_check,'Free_memory(Mb)':output_free_memory_check,'Used_memory(Mb)':output_used_memory_check,'buff/cache(Mb)':output_buff_mem_check,'shared_memory(Mb)':output_shared_mem_check,'Total_swapped_memory(Mb)':output_swapped_total_memory_check,'Free_swapped_memory(Mb)':output_free_swapped_memory_check,'Used swapped memory(Mb)':output_used_swapped_memory_check })
      
            #to print the load of cpu after given timer i.e. after 1min,5min,15min
            time_after_some_time = int(time.time() - time_start)
            if time_after_some_time >= after_xmin:
                print("load on cpu after "+str(after_xmin)+" sec-------------",output_cpu_check)
               # time_start = time.time()
            if time_after_some_time >= after_ymin:
                print("load on cpu after "+str(after_ymin)+" sec-------------",output_cpu_check)
                #time_start = time.time()
            if time_after_some_time >= after_zmin:
                print("load on cpu after "+str(after_zmin)+" sec-------------",output_cpu_check)
                time_start = time.time()


            time.sleep(sec)

    except KeyboardInterrupt:
        print("--------User has explicitly stopped the execution----------")
        calculate()


def trial(_signo, _stack_frame):
    #handles about the process killed by user 
    print("--------process is killed by user----------")
    calculate()
    sys.exit(0)
signal.signal(signal.SIGTERM, trial)

def main():
    check_hardware_validation()

if __name__ == '__main__':
    main()
