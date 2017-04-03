##Author: Linda Liu
#~ run this on a cloud, it will do it periodically 
import do_scrape
import sys
sys.path.append('/Users/linda/path/') 
import config_bloomberg
import time
import sys
import traceback

if __name__ == "__main__":
    while True:
        print("{}: Starting scrape cycle".format(time.ctime()))
        try:
            do_scrape.scrape()
        except KeyboardInterrupt:
            print("Exiting....")
            sys.exit(1)
        except Exception as exc:
            print("Error with the scraping:", sys.exc_info()[0])
            traceback.print_exc()
        else:
            print("{}: Successfully finished scraping".format(time.ctime()))
        time.sleep(config_bloomberg.SLEEP_INTERVAL)