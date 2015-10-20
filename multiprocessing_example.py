import numpy as np
import multiprocessing

#####################################################
def fct(x,y):
    return x + y**2 + 2

######################################################
def fct_star(args__):
    """Function to split input arguments,    
    """
    res = fct(*args__) 
    return res
    
######################################################
if __name__ == '__main__':
######################################################
    
    flag_parallel = True

    args_here = []
    for i in range(100):
        x = np.random.random()
        y = np.random.random()
        args_here.append([x,y])

    #flag_parallel = True
    if flag_parallel: 
   
        # set up a pool to run the parallel processing
        cpus = multiprocessing.cpu_count()
        pool = multiprocessing.Pool(processes=cpus)

        # then the map method of pool actually does the parallelisation  
        results = pool.map(fct_star, args_here)
        pool.close()
        pool.join()
        for result in results:
            print  result
    else:
        for i in range(100):
            print fct_star(args_here[i])
            
