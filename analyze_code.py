import subprocess
import os


def run_flake8(folder_path):
    """
    Run Flake8 analysis on a specified folder or file.

    Args:
        folder_path (str): The path of the folder or file to analyze with Flake8.

    Returns:
        str: The Flake8 analysis report as a string.
    """
    result = subprocess.run(["flake8", folder_path], capture_output=True, text=True)
    return result.stdout.strip()


def main():
    """
    Analyze files or folders using Flake8 and save the reports in the 'flake8_reports' folder.

    This function analyzes the specified files and folders using Flake8 and saves the reports
    in the 'flake8_reports' folder. If the folder does not exist, it will be created.
    """
    files_or_folders_to_analyze = ["Controller", "Model", "View", "DataBaseManager", "main.py"]

    if not os.path.exists("flake8_reports"):
        os.mkdir("flake8_reports")

    for item in files_or_folders_to_analyze:
        report = run_flake8(item)

        # If the item is a folder, use its name as the report file name
        if os.path.isdir(item):
            report_file_path = os.path.join("flake8_reports", f"{os.path.basename(item)}_flake8_report.txt")
        else:
            # If the item is a file, use the base name without the extension as the report file name
            file_name_without_extension = os.path.splitext(os.path.basename(item))[0]
            report_file_path = os.path.join("flake8_reports", f"{file_name_without_extension}_flake8_report.txt")
        with open(report_file_path, "w") as file:
            file.write(report)


if __name__ == "__main__":
    main()
