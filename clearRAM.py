def clearRAM(print_usage=False):

  import os
  from hurry.filesize import size
  import psutil
  import gc

  #--- clear ram
  gc.collect()

  #--- print usage
  if print_usage == True:
    process = psutil.Process(os.getpid())

    print(size(process.memory_info().rss))
