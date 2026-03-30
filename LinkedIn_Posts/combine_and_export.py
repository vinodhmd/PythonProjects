import glob
import os
import markdown

def combine_md_files(output_md_path):
    md_files = glob.glob('Post_*.md')
    md_files.sort()
    
    combined_content = []
    combined_content.append("# 🚀 Python Mastery Series: Complete Collection\n\n")
    
    for filename in md_files:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        combined_content.append(f"## --- {filename} ---\n\n")
        combined_content.append(content)
        combined_content.append("\n\n---\n\n")
        
    final_md = "".join(combined_content)
    
    with open(output_md_path, 'w', encoding='utf-8') as f:
        f.write(final_md)
        
    print(f"Successfully created: {output_md_path}")
    return final_md

def create_html(input_md_path, output_html_path):
    with open(input_md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()
        
    html_body = markdown.markdown(md_text, extensions=['fenced_code', 'codehilite', 'tables'])
    
    html_doc = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
    body {{ font-family: Segoe UI, Arial, sans-serif; max-width: 900px; margin: auto; padding: 2em; line-height: 1.6; color: #333; }}
    pre {{ background: #f4f4f4; border: 1px solid #ddd; padding: 15px; border-radius: 5px; overflow-x: auto; }}
    code {{ font-family: Consolas, monospace; }}
    h1, h2, h3 {{ color: #1a56db; }}
    hr {{ border: 0; border-top: 1px solid #ddd; margin: 30px 0; }}
</style>
</head>
<body>
{html_body}
</body>
</html>
"""
    with open(output_html_path, 'w', encoding='utf-8') as f:
        f.write(html_doc)
    print(f"Successfully generated HTML alternative: {output_html_path}")

def main():
    md_output = "All_LinkedIn_Posts.md"
    html_output = "All_LinkedIn_Posts.html"
    
    combine_md_files(md_output)
    create_html(md_output, html_output)

if __name__ == "__main__":
    main()
