#Python 3
import os

base_folder = input("Type in your base folder:\n")
all_folders = []
print_jobs_devided = [[1,2,3,4,5], [1,2,3,4,5]] # each list max 15

print ("the base is: ", base_folder)

#add to print queue
    #add first 15
    #when done, next 15

def scan_dir(directory):    
    for dirs in os.walk(directory):
        for dir in dirs:
            all_folders.append(dir)
    
scan_dir("All folders:\n" + all_folders)

print(all_folders)

def scan_files(directories):
    container_all = []
    for directory in directories:
        for files in os.walk(directory):
            for file in files:
                container_all.append(directory + "/" + file)
    return container_all

print_jobs_all = scan_files(all_folders)

print("All files:\n" + print_jobs_all)

#add files to print jobs all

#split jobs
    #split to 15 max list