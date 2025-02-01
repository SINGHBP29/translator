import subprocess
import time
import os

# Start Redis server
redis_process = subprocess.Popen("redis-server", shell=True)

# Wait a moment to ensure Redis starts properly
time.sleep(2)

# Run Django server
os.system("python manage.py runserver")

# Stop Redis when the server stops (Optional)
redis_process.terminate()
