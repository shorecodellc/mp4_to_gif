#kevin fink
#kevin@shorecode.org
#Sat Apr  5 09:53:28 AM +07 2025

#.py

import logging
import traceback
import os
from valdec.decorators import validate

class CustomLogger(logging.Logger):
    def __init__(self, name):
        super().__init__(name)
    
    def trace(self, e):
        self.error(f'E: {e}, TB: {traceback.format_exc()}')  

@validate
def set_logging(name: str, filename: str) -> logging.Logger:
    """
    Creates a logging directory if one does not exist and initializes and configures a logger
    
    Args:
    name (str) : Name of the logger
    filename (str) : Name of the file to output the log to
    
    Returns:
    logging.Logger: Logger object
    """
    # Checks for a logging directory and creates one if it does not exist
    if not os.path.isdir('logging'):
        os.mkdir('logging')

    # Create a logger
    custom = CustomLogger(name)
                
    # Delete the logging file if it is greater than 10Mb
    try:
        # Get the size of the logging file
        file_size = os.path.getsize(filename)
        
        if file_size > 10000000:
            os.remove(filename)
            with open(filename, 'w', encoding='utf-8') as fn:
                fn.write('New log')  
    except (PermissionError, FileNotFoundError) as e:
        with open(filename, 'w'):
            pass
        
    # Set the logger level to ERROR
    custom.setLevel(logging.INFO)    

    return custom