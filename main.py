from app.io.input import input_text, read_file, read_csv_with_pandas
from app.io.output import output_text, write_file, write_csv_with_pandas


def main():
    input_content = input_text()
    britney_content = read_file('data/britney.txt')
    example_df = read_csv_with_pandas('data/example.csv')

    output_text(input_content)
    write_file('data/output_britney.txt', britney_content)
    write_csv_with_pandas('data/output_example.csv', example_df)


if __name__ == "__main__":
    main()
