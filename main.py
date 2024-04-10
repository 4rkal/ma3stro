import threading
import subprocess
import time

def run_script(script_name):
    subprocess.run(["python", script_name])

if __name__ == "__main__":
    script1_thread = threading.Thread(target=run_script, args=("test2.py",))
    script2_thread = threading.Thread(target=run_script, args=("record.py",))

    script1_thread.start()
    time.sleep(8)
    script2_thread.start()

    script1_thread.join()
    script2_thread.join()

    print("Both scripts have finished executing.")