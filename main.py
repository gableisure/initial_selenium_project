from scraping import Scraping
from time import time

if __name__ == '__main__':
    start_time = time()

    scraping = Scraping()
    scraping.run()

    print('\nTempo de execução: %.2f seconds\n' %(time() - start_time))

