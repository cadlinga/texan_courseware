import os, sys, re
import argparse
import subprocess
import frontmatter

# return output from bash pipe cmd as decoded string
def run_cmd(cmd):
	bash_cmd = cmd
	process = subprocess.Popen(bash_cmd.split(), stdout=subprocess.PIPE)
	output = process.stdout.read()
	return output.decode('utf-8')

def sort_list(a_list):
    list_with_indeces = []
    for item in a_list:
        index = re.sub("[^0-9]", "", item)
        list_with_indeces.append([item, index])
    list_with_indeces.sort(key=lambda x: x[1]) # sort by index
    
    sorted_list = []
    for item in list_with_indeces:
        sorted_list.append(item[0])
    return sorted_list

def sort_chapter_list(a_list, path):
    list_with_indices = []
    for item in a_list:
        index = frontmatter.load(path +  "/" + item +  "/index.md")['nav_order']
        list_with_indices.append([item, index])
    list_with_indices.sort(key=lambda x: x[1]) 
    sorted_list = []
    for item in list_with_indices:
        sorted_list.append(item[0])
    return sorted_list

def sort_file_list(a_list, chapter, path):
    list_with_indices = []
    for item in a_list:
        if item.lower() == 'index.md':
            index = 0
        else:
            index = frontmatter.load(path + "/" + chapter + "/" + item)['nav_order']
        list_with_indices.append([item, index])
    list_with_indices.sort(key=lambda x: x[1]) 
    sorted_list = []
    for item in list_with_indices:
        sorted_list.append(item[0])
    return sorted_list


# get chapters first if they exist as directories
# then Scenes, or just Chapters if they are md files.
def get_list_of_files(path, extension, chapter_folders=False):
    sorted_markdown_list = []
    if chapter_folders:
        chapters_list = [ item for item in os.listdir(path) if os.path.isdir(os.path.join(path, item)) ]
        chapters_list = sort_chapter_list(chapters_list, path)
        
        for chapter in chapters_list:
            chapter_markdown_files = []
            all_files = os.listdir(path + "/" + chapter)
            for a_file in all_files:
                if a_file.endswith("." + extension):
                    # path + "/" + chapter + "/" + 
                    chapter_markdown_files.append(a_file)
            # chapter_markdown_files = sort_list(chapter_markdown_files)
            chapter_markdown_files = sort_file_list(chapter_markdown_files, chapter, path)
            # chapter_markdown_files = sort_chapter_list(chapter_markdown_files, path)
            for index in range(len(chapter_markdown_files)):
                current_path = chapter_markdown_files[index]
                chapter_markdown_files[index] = path + "/" + chapter + "/" + current_path
            sorted_markdown_list.extend(chapter_markdown_files)
    else:
        # process only MD files make sure they are numbered
        all_files = os.listdir(path)
        for a_file in all_files:
            if a_file.endswith("." + extension):
                sorted_markdown_list.append(a_file)
        sorted_markdown_list = sort_list(sorted_markdown_list)
        for index in range(len(sorted_markdown_list)):
            current_path = sorted_markdown_list[index]
            sorted_markdown_list[index] = path + "/" + current_path

    
    sorted_markdown_list.insert(0, path + "/" + "index.md")
    sorted_markdown_list.append(path + "/" + "title.md")
    return sorted_markdown_list

def export_dir_to_format(path):
    pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--root-path', help='Root path for book files', required=True)
    parser.add_argument('-c', '--using-chapter-folders', 
    help='Are you using folders for chapters?', default=False,action='store_true')
    parser.add_argument('-f', '--file-extension', default='md')
    args = parser.parse_args()

    file_list = get_list_of_files(args.root_path, args.file_extension, args.using_chapter_folders)

    if not file_list:
        print("No markdown files found, if you\'re using folder chapters use -c, else do not use -c")
        print("Exiting...")
        exit()
    
    for file in file_list:
        print(file)

    if args.root_path[-1] != '/' or args.root_path[-1] != '\\':
        args.root_path = args.root_path + '/'

    default_pandoc_cmd = 'pandoc --resource-path=./groundschool/images:./groundschool/images/do_not_delete --top-level-division=chapter -V="classoption=oneside"  --pdf-engine=xelatex --toc -o' + args.root_path +'book.pdf title.txt '
    files_string = " ".join(file_list)

    run_cmd(default_pandoc_cmd + files_string)

if __name__ == "__main__":
    main()
