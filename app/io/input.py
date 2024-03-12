import pandas as pd


def input_text() -> str:
    """
    function that will read the content from the terminal

    :return: content from the terminal
    """
    user_input = input("Enter text to terminal: ")
    return user_input


def read_file(filename: str) -> str:
    """
    function that write content from the .txt file

    :param filename: name of the file that will be read
    :return: content from file
    """
    try:
        with open(file=filename, mode='r') as file:
            content = file.read()
        return content
    except FileNotFoundError as e:
        print(e)
        return None


def read_csv_with_pandas(filename: str) -> pd.DataFrame:
    """
    function that will read dataframe from .csv file using pandas

    :param filename: name of the file that will be read
    :return: dataframe read from .csv file
    """
    df = pd.read_csv(filename)
    return df

