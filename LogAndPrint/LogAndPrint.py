from __future__ import annotations
import logging

class LogAndPrint:
    '''
    A class for creating log file and printing log messages to console

    LogAndPrint allow developer to generate multiple logging entities,
    set level of logging and location of log file.

    Args:
        text_to_log: string, text that will be logged
        print_to_screen: bool, option for printing text to console output
        type_of_event: string, name of the log event attribute (debug, info, warning, error)
        formatter: string, format string content displayed by logger

    Methods:

    Returns: LogAndPrint returns its self

    Raises:

    '''
    def __init__(self, *args) -> LogAndPrint:
        self.text_to_log = args[0]
        self.print_to_screen = args[1]
        self.type_of_event = args[2]

        # create message formatter
        self.formatter = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        
        # configure how the logger is setup
        logging.basicConfig(filename='main.log', filemode='a', encoding='UTF-8', level=logging.DEBUG, format=self.formatter)

        # create new logger with name of the class and then set level
        self.Logger = logging.getLogger(__name__)
        self.Logger.setLevel(logging.DEBUG) # Debug: need to new logic to allow user to define default logging level

    def update_args(self, **kwargs):
        print(len(kwargs))
        self.text_to_log = kwargs['text']
        self.print_to_screen = kwargs['screen']
        self.type_of_event = kwargs['event']

    def arbitrate_log(self) -> int:
        success = 0
        print("Debug: %s"%(self.type_of_event))
        match self.type_of_event:
            case 'info':
                self.Logger.info(self.text_to_log)
            case 'warning':
                self.Logger.warning(self.text_to_log)
            case 'debug':
                self.Logger.debug(self.text_to_log)
            case _:
                print('Nothing can be done, try again!!!!')
                success = 1
        if (self.print_to_screen):
            print(self.text_to_log)
        return success

    def main(self, **kwargs):
        if(len(kwargs) == 0):
            exit_status = self.arbitrate_log()
        else:
            self.update_args(**kwargs)
            exit_status = self.arbitrate_log()
        return exit_status

bubba = LogAndPrint('Hey what it is man!!!', True, 'warning')
bubba.main()
bubba.type_of_event='debug'
shan = {'text':'This is my new message now!!!', 'screen':True, 'event':'info'}
bubba.main(**shan)
print(bubba.__doc__)
