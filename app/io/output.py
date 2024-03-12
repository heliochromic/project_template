import pandas as pd


def output_text(content: str) -> None:
    """
    function that print content to the terminal

    :param content: content that will be written in to the terminal
    """
    print(content)


def write_file(filename: str, content: str) -> None:
    """
    function that write content into the .txt file

    :param filename: name of the file that will be created
    :param content: content that will be written in to the file
    """
    with open(file=filename, mode='w') as file:
        file.write(content)


def write_csv_with_pandas(filename: str, dataframe: pd.DataFrame) -> None:
    """
    function that write dataframe into the .csv file using pandas

    :param filename: name of the file that will be created
    :param dataframe: dataframe that will be written in to the file csv file
    """
    dataframe.to_csv(filename, sep=',', encoding='utf-8', index=False)

