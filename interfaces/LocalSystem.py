import os

class LocalSystem:
  def scan_dir(directory):
    print_jobs_all = []   

    for root_dir, sub_dir, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root_dir, file)
            print_jobs_all.append(file_path)
    
    return print_jobs_all