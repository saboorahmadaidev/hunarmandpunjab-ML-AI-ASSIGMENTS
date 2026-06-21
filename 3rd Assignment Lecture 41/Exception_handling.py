# Exception_handling.py — catching multiple exceptions and logging
import traceback

def log_error(e):
    with open('error_log.txt', 'a') as f:
        f.write(str(e) + '\n')
        f.write(traceback.format_exc() + '\n')

try:
    vals = [1,2,3]
    print(vals[10])
except Exception as e:
    print('An error occurred:', e)
    log_error(e)
