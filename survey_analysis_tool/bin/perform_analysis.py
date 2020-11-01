import pandas as pd
import logging
import os
import sys
from typing import List


def set_log_file(target_folder: str, log_file_name: str):
    """
    Helper function to set up a log file in addition to the stdout messages.
    :param target_folder: Folder where to create the log file
    :param log_file_name: name of the log file.
    """
    # Set up log file
    log_file = os.path.join(target_folder, log_file_name)
    file_handler = logging.FileHandler(log_file, mode='a')
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    root.addHandler(file_handler)
    return root


def load_csv_file(file_path: str) -> pd.DataFrame:
    """
    Function that reads the custom '.csv' file and returns a Pandas DataFrame.
    :param file_path: Absolute path to the path file.
    :return: result_dataframe: Pandas DataFrame with the read values.
    """
    try:
        result_dataframe = pd.read_excel(file_path)
    except ValueError:
        message = 'Error loading the CSV file.'
        raise ValueError(message)
    return result_dataframe


def main():
    # Setup a logger
    # Temporary file path to the Excel file
    file_path = '/Users/nico/MEGAsync/MEGAsync/MEGAsync/Uni/Master/Insights/Customer_Feedback_xlsx.xlsx'
    # Set up the logger
    logger = set_log_file(os.path.join(os.getcwd(), 'log_files'), 'log.txt')

    # Read the Excel file
    try:
        survey_data_frame = load_csv_file(file_path)
        print('File loaded correctly!')
    except ValueError as message:
        logger.error(message)
        sys.exit(1)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('KeyboardInterrupt!')
