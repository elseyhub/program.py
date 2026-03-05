import time
import traceback
import sys
import os

def main():
    
    print("script is running...")
    
    x = 1/0 

def run_with_self_healing():
    while True:
        try:
            main()
            break # 
        except Exception as e:
            print("Error occured:",e)
            traceback.print_exc()
            print("Attempting to recover in 5 seconds...")
            time.sleep(5)
if _name_ == "__main__":
    run_with_self_healing()

    
