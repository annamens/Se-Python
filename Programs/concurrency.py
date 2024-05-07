import threading
from multiprocessing import Process

def worker():
    print("Worker")

# Create a process
process = Process(target=worker)

# Start the process
process.start()