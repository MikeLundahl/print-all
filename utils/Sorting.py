
class Sorting:
  def split_print_jobs(all_jobs, my_max):
    for i in range(0, len(all_jobs), my_max):
        yield all_jobs[i:i + my_max]