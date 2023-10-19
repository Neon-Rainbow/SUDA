class Process:
    def __init__(self, arrival_time, priority, execution_time, process_id):
        self.arrival_time = arrival_time
        self.priority = priority
        self.execution_time = execution_time
        self.state = "未到达"  # Possible states: 未到达, 处于就绪队列但未在运行, 处于运行状态
        self.wait_time = 0  # Time spent waiting in the ready queue
        self.process_id = process_id  # Unique identifier for each process


class Scheduler:
    def __init__(self):
        self.ready_queue = []
        self.current_time = 0
        self.running_process = None

    def add_process(self, process):
        if process.arrival_time <= self.current_time:
            process.state = "处于就绪队列但未在运行"
            self.ready_queue.append(process)
        else:
            # Assume processes are added in order of arrival time
            self.ready_queue.append(process)

    def update_priority(self):
        for process in self.ready_queue:
            if process.state == "处于就绪队列但未在运行":
                process.priority -= 2
            elif process.state == "处于运行状态":
                process.priority -= 1

    def display_process_info(self):
        print(f"Time: {self.current_time}")
        for process in self.ready_queue:
            print(f"Process {process.process_id}: State: {process.state}, Priority: {process.priority}")

    def schedule(self):
        while self.ready_queue:
            if self.current_time > 30:
                print("Time out!")
                break
            self.current_time += 1
            self.update_priority()

            # Sort the ready queue by priority, breaking ties by arrival time
            self.ready_queue.sort(key=lambda p: (-p.priority, p.arrival_time))

            # Update the state of the running process, if any
            if self.running_process:
                self.running_process.execution_time -= 1
                if self.running_process.execution_time == 0:
                    self.ready_queue.remove(self.running_process)
                    self.running_process = None

            # If no process is running, start the highest priority process
            if not self.running_process and self.ready_queue:
                next_process = self.ready_queue[0]
                if next_process.state == "处于就绪队列但未在运行" and next_process.arrival_time <= self.current_time:
                    next_process.state = "处于运行状态"
                    self.running_process = next_process

            # Display process information at each time step
            self.display_process_info()


# Example Usage:
p1 = Process(arrival_time=0, priority=8, execution_time=5, process_id=1)
p2 = Process(arrival_time=1, priority=4, execution_time=6, process_id=2)
p3 = Process(arrival_time=2, priority=6, execution_time=3, process_id=3)
p4 = Process(arrival_time=3, priority=2, execution_time=4, process_id=4)
p5 = Process(arrival_time=4, priority=10, execution_time=2, process_id=5)
scheduler = Scheduler()
scheduler.add_process(p1)
scheduler.add_process(p2)
scheduler.add_process(p3)
scheduler.add_process(p4)
scheduler.add_process(p5)
scheduler.schedule()
