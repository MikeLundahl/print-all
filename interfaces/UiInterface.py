class UiInterface:

  def show_documents_information(print_jobs_all, print_jobs_divided):
    print("Documents to print: " + str(len(print_jobs_all)))
    print("Chunks to print: " + str(len(print_jobs_divided)))

  def show_documents_list(print_jobs_divided):
    print("Following documents are to be printed:")
    batch = 1
    for chunk in print_jobs_divided:
        print("-" * 50)
        print("BATCH NUMBER " + str(batch))
        batch += 1
        for file in chunk:
            print(file)
    print("End of file list ------------------------------------------>")

  def show_files_in_chunk_end():
    print("End of chunk ---------------------------->")

  def show_instructions():
    print("Press ENTER to continue | S to show list of files | Q to cancel")
  
  def update_cli(updateText):
    print("\r{}".format(updateText), end="")