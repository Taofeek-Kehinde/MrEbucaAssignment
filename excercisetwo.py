#(Discussion: Function-Call Stack) What happens if you keep pushing onto a stack,
#without enough popping?

def keep_pushing():
    keep_pushing()  # keeps calling itself forever, no pop

keep_pushing()  
