def check_for_log_errors(log_file_path):
    try:
        with open(log_file_path,'r') as file:

            lines=file.readlines()
            errors=[error for error in lines if 'ERROR' in error]
            if errors:
                print('Error found in the log file')
                for error in errors:
                    print(error.strip())
            else:
                print('No error found')
    except FileNotFoundError:
        print(f"Log file {log_file_path} not found.")
if __name__=="__main__":
    log_file_path="log"
    check_for_log_errors(log_file_path)
