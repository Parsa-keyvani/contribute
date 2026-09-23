
import datetime

def estimeate_time(f)
  def warapper()
      start = datetime.datatime.now().minute()
      f
      end = datetime.datatime.now().minute()

      time = end - start
      

  return wrapper



@estimeate_time
def make_num()
    for i in range(1,20):
        print(i)
