import os
import argparse
import subprocess

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# return output from bash pipe cmd as decoded string
def run_cmd(cmd):
	bash_cmd = cmd
	process = subprocess.Popen(bash_cmd.split(), stdout=subprocess.PIPE)
	output = process.stdout.read()
	return output.decode('utf-8')

def get_list_of_files(path):
    sorted_markdown_list = []
    chapters_list = [ item for item in os.listdir(path) if os.path.isdir(os.path.join(path, item)) ]
    for chapter in chapters_list:
        chapter_markdown_files = []
        all_files = os.listdir(path + "/" + chapter)
        for a_file in all_files:
            if a_file.endswith(".md"):
                chapter_markdown_files.append(a_file)
        for index in range(len(chapter_markdown_files)):
            current_path = chapter_markdown_files[index]
            chapter_markdown_files[index] = path + "/" + chapter + "/" + current_path   
        sorted_markdown_list.extend(chapter_markdown_files)

    return sorted_markdown_list

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--root-path', help='Root path for book files', required=True)
    args = parser.parse_args()

    file_list = get_list_of_files(args.root_path)
    does_not_end_with_whitespace = []

    for file in file_list:
        with open(file, 'rb+') as filehandle:
            filehandle.seek(filehandle.tell()-1, 2)
            last_char = filehandle.read().decode("utf-8") 
            if last_char.endswith('\n'):
                continue 
            else:
                does_not_end_with_whitespace.append(file)

    if does_not_end_with_whitespace:
        print(f"{bcolors.FAIL}\n\n" +  str(len(does_not_end_with_whitespace)) + " files do not end with a blank line: \n")
        for file in does_not_end_with_whitespace:
            print(file)
        print("\n\nFix these files before continuing...")
        return False
    else: 
        print(f"{bcolors.OKGREEN}All files end with at least one blank line! Well done.")
        return True 

if __name__ == "__main__":
    main()