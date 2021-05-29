#Python 3
from interfaces.UiInterface import UiInterface
from interfaces.LocalSystem import LocalSystem
from interfaces.PrinterInterface import PrinterInterface
from utils.Sorting import Sorting
from pynput import keyboard
import asyncio
import time

is_canceled = False

def main():
    MAX_PRINT_JOBS = 15
    PRINTER = PrinterInterface.get_default_printer()
    HPRINTER = PrinterInterface.get_printer_handle(PRINTER)

    base_folder = input("Type in your base folder:\n")
    print_jobs_all = LocalSystem.scan_dir(base_folder)
    print_jobs_divided = list(Sorting.split_print_jobs(print_jobs_all, MAX_PRINT_JOBS))

    def get_current_print_queue(printer_handle):
        print_jobs = PrinterInterface.get_printer_queue(printer_handle)
        return print_jobs

    def init_printing(jobs):
        listener = keyboard.Listener(on_press = press_on)
        listener.start()

        for index, chunk in enumerate(jobs):
                    
            if is_canceled:
                break
                
            current_chunk = index + 1
                        
            while get_current_print_queue(HPRINTER):
                if is_canceled:
                    break

                UiInterface.update_cli("Documents left before next chunk: " + str(len(get_current_print_queue(HPRINTER))))
                time.sleep(2)

            print("Now printing chunk #" + str(current_chunk))

            for file in chunk:
                if is_canceled:
                    break

                PrinterInterface.send_to_print_queue(file)
                print("File sent to print queue: " + file)
                time.sleep(3)
            
            if is_canceled:
                print("Printing canceled!")
                return

            UiInterface.show_files_in_chunk_end()
            time.sleep(5)
    
    def cancel_printing():
        current_queue = get_current_print_queue(HPRINTER)

        for job in current_queue:
            PrinterInterface.cancel_print_jobs(HPRINTER, job)
        
        PrinterInterface.close_printer(HPRINTER)

    def press_on(key):
        global is_canceled            
        if str(key) == "'q'":
            is_canceled = True
            cancel_printing()
            return False
        
        if key == keyboard.Key.enter:
            init_printing(print_jobs_divided)
            return False
        
        if str(key) == "'s'":
            UiInterface.show_documents_list(print_jobs_divided)
            UiInterface.show_instructions()
            return 

    print("^" * 50)
    UiInterface.show_documents_information(print_jobs_all, print_jobs_divided)
    print("Default printer: " + PRINTER)
    UiInterface.show_instructions()

#https://pypi.org/project/pynput/
    with keyboard.Listener(on_press = press_on) as listener:
        listener.join()
    
main()
