#!/usr/bin/env python3
import sys
import time
import re

def get_page_fault():
    """获取当前系统的缺页中断次数。"""
    try:
        with open('/proc/vmstat', 'r') as vmstat:
            content = vmstat.read()
        match = re.search(r'pgfault\s+(\d+)', content)
        if match:
            return int(match.group(1))
    except Exception as e:
        print(f"Error reading vmstat: {e}")
        return -1

def print_progress_bar(duration):
    """显示一个简单的进度条，持续给定的秒数。"""
    for i in range(duration + 1):
        percent = (i / duration) * 100
        bar = '#' * int(percent // 2) + '-' * (50 - int(percent // 2))
        sys.stdout.write(f'\r[{bar}] {i}/{duration} seconds ({percent:.0f}%)')
        sys.stdout.flush()
        time.sleep(1)
    print()  # Move to the next line

def main():
    calc_time = 10  # 默认休眠时间
    if len(sys.argv) > 1:
        try:
            calc_time = int(sys.argv[1])
        except ValueError:
            print("Invalid input. Using default duration of 10 seconds.")

    initial_faults = get_page_fault()
    if initial_faults < 0:
        print('Error reading initial page faults!')
        sys.exit(1)

    print("Starting to monitor page faults...")
    print_progress_bar(calc_time)

    final_faults = get_page_fault()
    if final_faults < 0:
        print('Error reading final page faults!')
        sys.exit(1)

    faults_diff = final_faults - initial_faults
    print(f"Initial page faults: {initial_faults}")
    print(f"Final page faults: {final_faults}")
    print(f"Page faults occurred during the interval: {faults_diff}")

if __name__ == '__main__':
    main()
