import logging
import sys
import os
import colorama as color
from colorama import Fore, Back, Style

def loggy(status):

    logFile = 'cping.log'
    if status == 'on':
        logging.basicConfig(
        					filename=logFile,
        					filemode='w',
        					level=logging.DEBUG,
        					format='%(name)s - %(asctime)s - %(process)d - %(levelname)s - %(message)s',
        					datefmt='%d-%b-%y %H:%M:%S'
        					)

        logging.info('Logger is on')
    else:
        print('Logger is off!')
        pass


def cping_init():
    loggy('on')
    color.init()
    logging.info("cping app initialised successfully")

def welcome():

    print(Fore.RED + 'This script helps to send multiple pings at a customized rate.' + Fore.RESET, end='\n\n')
    print(Back.RED + 'NOTE: ' + Back.RESET, end='')
    print('It is your responsibility to double-check the results and ensure accuracy!!!', end='\n\n')

def custom_ping():
    count = input('Please enter how many icmp packets do you want to send: ' + Fore.GREEN)
    interval = input(Fore.RESET + 'Please enter delay in seconds between pings per next IP: ' + Fore.GREEN)
    subnet_address = input(Fore.RESET + 'Please enter network to ping in the format of X.X.X.X/Y: ' + Fore.GREEN)
    log_msg = 'Requested to ping addresses in {0} every {1} seconds with {2} packets at a time.'.format(subnet_address, interval, count)
    logging.info(log_msg)




def main():
    cping_init()
    welcome()
    custom_ping()





# logging.debug('This is a debug message')

# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')


#     hostnames = [
#         '10.40.161.2',
#         '10.40.161.3',
#         '10.40.161.4',
#         '10.40.161.5',
#     ]
#
#     for hostname in hostnames:
#         response = os.system('ping -c 1 ' + hostname)
#         if response == 0:
#             print hostname, 'is up'
#         else:
#             print hostname, 'is down'
#
#

if __name__ == '__main__':
    main()
