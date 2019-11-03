
"""This Module manipulates the data to required output format and write them in to file.

Implements the functionality for adding dictionary data to list, Add the data list to data frame,
write the data list in to data frame, write the debug dcrt messages in to a file and format the clock time in to
required format.

"""

import os
import sys
import warnings

# Deprecation warning is suppressed from import hashtable of pandas package, cannot be resolved in test framework.
with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    import pandas as pd


class DataLogger(object):
    """DataLogger class implements the methods used to write data in to data frame and create dcrt log messages."""

    def __init__(self, filename, directory, plot_filename):
        """Constructor for DataLogger class.

        Arguments:
            filename -- Name of the file to which data has to be written.
            directory -- Directory of the data logger file.
            plot_filename -- Name of the file where plots are to be made.
        """
        self.__filename = filename
        self.__directory = directory
        self.__plot_filename = plot_filename
        self.__data_log_list = list()
        self.__df = pd.DataFrame()

    def add_data_to_data_list(self, logged_data):
        """Add dictionary to list.

        Arguments:
            logged_data -- dictionary data appended to the list.
        """
        self.__data_log_list.append(logged_data.copy())

    def add_datalist_to_dataframe(self):
        """Add list data to data frame."""
        #import pdb;pdb.set_trace()
        self.__df = pd.DataFrame(self.__data_log_list, columns=self.__data_log_list[0].keys())

    def save_data_to_csv(self):
        """Delete the duplicates in data frame if available and writes data frame to csv."""
        if self.__filename != "":
            sys.stdout.write(
                "Saving incoming messages to file: {}\n".format(os.path.join(self.__directory, self.__filename)))
            self.add_datalist_to_dataframe()
            try:
                self.__df.drop_duplicates(inplace=True)
                self.__df.to_csv(os.path.join(self.__directory, self.__filename), index=False)
            except ValueError:
                sys.stdout.write("*** Exception of type ValueError, No items to drop as data frame is empty \n")
            except AttributeError:
                sys.stdout.write("*** Exception occurred of type AttributeError, data frame is empty \n")
        else:
            sys.stdout.write("Filename is not defined and results cannot be saved.")

    def create_dcrt_log_message(self, timestamp, logged_data):
        """
        Create a dcrt messages used for debugging.

        Arguments:
             timestamp -- Time at which dcrt message is generated.
             logged_data -- Message data dictionary format.

        returns -- dcrt message prepended with formatted timestamp.
        """
        # When launching eval node manually and triggering it, this message is logged.
        message = ("-------------------------------------------------------\n"
                   "TimeStamp: {} ns ({}) \n".format(timestamp, self.format_timestamp(timestamp))
                   )
        for key, value in logged_data.items():
            message += "\n{}: {} \n".format(key, value)
        return message

    @staticmethod
    def format_timestamp(timestamp):
        """Return clock time to mins, secs and msecs format.

        Arguments:
            timestamp -- clock time at an instant ros message is generated.
        """
        secs = timestamp % 60
        mins = int(timestamp / 60)
        msecs = int(timestamp / 1e9)
        return "t{}:{:02f}.{:03f}".format(mins, secs, msecs)
