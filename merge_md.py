import os
import glob

def merge_md_files(input_dir, output_file):
    # Find all .md files in the directory
    md_files = glob.glob(os.path.join(input_dir, "Post_*.md"))
    
    # Sort them by their post number naturally
    md_files.sort()

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write("# 🚀 Python Mastery Series - Complete LinkedIn Posts 🐍\n\n")
        outfile.write("Below is a collection of all Python sample code posts, ready for LinkedIn!\n\n")
        outfile.write("-----------------------------------------------------------------------\n\n")
        
        for file in md_files:
            with open(file, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read())
                outfile.write("\n\n---\n\n")  # Markdown separator between posts

    print(f"Successfully merged {len(md_files)} files into {output_file}")

if __name__ == "__main__":
    merge_md_files("LinkedIn_Posts", "LinkedIn_Posts_Complete.md")
