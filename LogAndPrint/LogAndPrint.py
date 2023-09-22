from __future__ import annotations
import logging


class LogAndPrint:
    """
    A class for creating log file and printing log messages to console

    LogAndPrint allow developer to generate multiple logging entities,
    set level of logging and location of log file.

    Args:
        text_to_log -- string, text that will be logged
        print_to_screen -- bool, option for printing text to console output
        type_of_event -- string, name of the log event attribute (debug, info, warning, error)
        formatter -- string, format string content displayed by logger

    Returns: LogAndPrint returns its self, instance of LogAndPrint

    """

    def __init__(self, text: str, screen: bool, event: str, *args) -> LogAndPrint:
        set_level = ''
        """
        Initialize LogAndPrint class using *args input arguments.

        In the *args list, the first indexed argument (zero) sets the text_to_log public var. The second
        indexed argument (one) set print_to_screen public var. Following is the type_of_event public var
        set by the third indexed argument (two)

        Args:
            text_to_log -- string, text that will be logged
            print_to_screen -- bool, option for printing text to console output
            type_of_event -- string, name of the log event attribute (debug, info, warning, error)
            formatter -- string, format string content displayed by logger
            log_file_name -- name and path location of log file
            set_default_level -- set the level for logger

        Returns: LogAndPrint returns its self, instance of LogAndPrint
        """
        # dictionary for setting default logging level
        SET_LEVEL = {'info' : logging.INFO, 'debug' : logging.DEBUG, 'warning' : logging.WARNING}
        # Set public variables, these are required.
        self.text_to_log = text
        self.print_to_screen = screen
        self.type_of_event = event
        self.log_file_name = 'LogAndPrint.log'
        self.set_default_level = 'info'

        # Checking for any additional arguments log_file_name and set_defauilt_level.
        if (len(args) >= 0):
            for arg in range(len(args)):
                if (arg == 0):
                    self.log_file_name = args[arg]
                elif (arg == 1):
                    self.set_default_level = args[arg]

        # create message formatter
        self.formatter = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        
        # configure how the logger is setup
        logging.basicConfig(filename=self.log_file_name, filemode='a', encoding='UTF-8', level=logging.DEBUG, format=self.formatter)

        # create new logger with name of the class and then set level
        self.Logger = logging.getLogger(__name__)
        self.Logger.setLevel(SET_LEVEL[self.set_default_level]) # Debug: need to new logic to allow user to define default logging level

    def update_args(self, **kwargs):
        """
        Uses three keyword arguments to update public variables text_to_log, print_to_screen & type_of_event

        Args:
            text: value is stored in text_to_log
            screen: value is stored in print_to_screen
            event: value is stored in type_of_event
        """
        self.text_to_log = kwargs['text']
        self.print_to_screen = kwargs['screen']
        self.type_of_event = kwargs['event']

    def arbitrate_log(self) -> int:
        """
        This method decides which logging function to call. Available methods are
        info, warning, debug and error.

        Returns: Returns an integer, 0 for pass and 1 for fail.
        """
        success = 0
        match self.type_of_event:
            case 'info':
                self.Logger.info(self.text_to_log)
            case 'warning':
                self.Logger.warning(self.text_to_log)
            case 'debug':
                self.Logger.debug(self.text_to_log)
            case 'error':
                self.Logger.error(self.text_to_log)
            case _:
                print(f'Could not log information, did not recognize log method {self.type_of_event}')
                success = 1
        if (self.print_to_screen):
            print(self.text_to_log)
        return success

    def main(self, **kwargs) -> int:
        """
        The main method takes optional keyword arguments. text, screen, event

        Checks if kwargs are present, when arguments are available main will choose
        to run the update_args method to update public variables.

        Returns: Returns integer as the exit code status 
        """
        if(len(kwargs) == 0):
            exit_status = self.arbitrate_log()
        else:
            self.update_args(**kwargs)
            exit_status = self.arbitrate_log()
        return exit_status

if __name__ == '__main__':
    # create logger instance my_logger
    my_logger = LogAndPrint('Hey what it is man!!!', True, 'warning', 'default.log')
    print("This is my first Log And Print statement")
    my_logger.main()

    # update my_logger type of event to debug
    my_logger.type_of_event = 'debug'
    # new content being logged with debug message
    print("Here is the second Log And Print statement")
    content_to_log = {'text':'This is my new message now!!!', 'screen':True, 'event':'info'}
    my_logger.main(**content_to_log)

