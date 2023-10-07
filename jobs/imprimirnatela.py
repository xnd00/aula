import sched

job = sched.scheduler()

def printa():
    print("Estou rodando no servidor!")
    job.enter(delay=3, priority=0,action=printa)

printa()

job.run(blocking=True)

###  https://www.youtube.com/@pythonando

##  https://www.youtube.com/@pythonando