from win32 import win32api
from win32 import win32print

class PrinterInterface:

  def get_default_printer():
    return win32print.GetDefaultPrinter()

  def get_printer_handle(printer):
    return win32print.OpenPrinter(printer)

  def get_printer_queue(printer_handle):
    print_queue = win32print.EnumJobs(printer_handle, 0, -1, 1)
    return print_queue

  def send_to_print_queue(file):
    win32api.ShellExecute(0, "print", file, None,  ".",  0)