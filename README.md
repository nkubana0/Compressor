# Compressor

This Python script allows you to compress files and folders into various compressed file types such as zip, tar, or tgz.

## Usage

1. Clone the repository or download the `compressor.py` file.

2. Open a terminal and navigate to the directory containing the `compressor.py` file.

3. Run the script using the following command format:

    ```
    python compressor.py <folder_path> <compression_type>
    ```

    Replace `<folder_path>` with the path to the folder you want to compress and `<compression_type>` with one of the following options: `zip`, `tar`, or `tgz`.

    Example:
    ```
    python compressor.py /path/to/folder zip
    ```

4. The script will compress the specified folder into the chosen compression type and save it with the appropriate file extension.

5. You will see a message indicating whether the compression was successful or if there was an error.

## Notes

- Ensure that you have Python installed on your system.
- Make sure to provide the correct folder path and compression type as arguments when running the script.
- The compressed file will be saved in the same directory as the original folder.
- For tgz compression type, the compressed file will be named in the format "name_of_the_folder_date_month_year.tar.gz".
