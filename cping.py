import logging
import sys
import os
import colorama as color
from colorama import Fore, Back, Style
import ipaddress

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

def cping_prompt():
    count = input('Please enter how many icmp packets do you want to send per IP[1-5]: ' + Fore.GREEN)
    interval = input(Fore.RESET + 'Please enter delay in seconds between pings per next IP[1-5]: ' + Fore.GREEN)
    subnet_address = input(Fore.RESET + 'Please enter network to ping in the format of X.X.X.X/Y: ' + Fore.GREEN)
    log_msg = 'Input recived and is ready for validation'
    logging.info(log_msg)

    return count, interval, subnet_address

def validate_params(*numbers):
    validInt = False
    for num in numbers:
        try:
            num_int=int(num)
            if 1 <= num_int <= 5:
                validInt = True
                pass
            else:
                log_msg = 'Count and delay values must be in the range of 1-5'
                logging.error(log_msg)
                validInt = False
                sys.exit()
        except:
            log_msg = 'Exception occured while validating count and delay values'
            logging.error(log_msg)
            validInt = False
            sys.exit()

    if validInt:
        log_msg = 'Count and delay values have now been validated'
        logging.info(log_msg)


def validate_mask(mask):
    validMask= False
    try:
        if 22 <= int(mask) <= 32:
            validMask = True
            pass
        else:
            log_msg = 'Unsupported subnet mask value: '.format(mask)
            logging.error(log_msg)
            validMask = False
            sys.exit()
    except:
        log_msg = 'Exception occured while validating subnet mask'
        logging.error(log_msg)
        validMask = False
        sys.exit()

    if validMask:
        log_msg = 'Subnet mask have now been validated'
        logging.info(log_msg)


def validate_subnet(ip_subnet):
    try:
        if ipaddress.ip_address(ip_subnet):
            log_msg = 'Subnet address have now been validated'
            logging.info(log_msg)
            pass
        else:
            log_msg = 'Invalid subnet address.'
            logging.error(log_msg)

    except:
            log_msg = 'Exception occured while validating subnet address.'
            logging.error(log_msg)



def main():
    cping_init()
    welcome()
    count, interval, subnet_address = cping_prompt()
    print ('Count:', count, 'interval:', interval, 'subnet_address:', subnet_address)

    validate_params(count, interval)
    try:
        subnet, mask = subnet_address.split("/")
    except:
        log_msg = "{} is not correct format for subnet address. Use X.X.X.X/Y format".format(subnet_address)

    validate_mask(mask)
    validate_subnet(subnet)

    log_msg = 'Requested to ping addresses in {0} every {1} seconds with {2} packets at a time.'.format(subnet_address, interval, count)
    logging.info(log_msg)
    print(log_msg)

if __name__ == '__main__':
    main()



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
