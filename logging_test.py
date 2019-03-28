import logging
logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
#logging.debug('Start of Program')
logging.disable(logging.CRITICAL)
def factorial(n):
    total = 1
    logging.debug('Start of factorial(%s)' % (n))
    for i in range(1,n+1):
        total*=i
        logging.debug('i is %s,total is %s' %(i,total))
    return total
logging.debug('End of Factorial')

print(factorial(5))

 