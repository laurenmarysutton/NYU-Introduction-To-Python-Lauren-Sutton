time = datetime.datetime.now()

def greeting(time):
  name = 'Jess'
  print('Hello {}, the time is {}''.format(name, time))

greeting(time=time)
