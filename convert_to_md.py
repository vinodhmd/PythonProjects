import os
import re

def generate_linkedin_posts(input_file, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    posts = []
    current_post = []
    current_title = "Introduction"

    # Keywords that might start a new topic
    topic_keywords = ["String methods", "Typecasting", "Arithmetic & math", "Math module", 
                      "if conditional statements", "Logical Operators", "format specifiers", 
                      "while loop", "For Loops", "Collections", "Dictionary", "Random Numbers", 
                      "Function", "Iterables and Iterators", "Membership Operators"]

    # Simple heuristic to chunk the file
    chunk_size = 50 # lines max per post for readability, but better to group by topics.

    for line in lines:
        stripped = line.strip()
        
        # Check if line is a major topic comment
        is_topic = False
        if stripped.startswith("#"):
            for keyword in topic_keywords:
                if keyword.lower() in stripped.lower():
                    is_topic = True
                    # Clean up title
                    new_title = stripped.lstrip("# \t-")
                    break

        if is_topic and len(current_post) > 10:
            posts.append((current_title, current_post))
            current_post = []
            current_title = new_title

        current_post.append(line)

    if current_post:
        posts.append((current_title, current_post))

    post_counter = 1
    for title, content in posts:
        # Create a catchy LinkedIn Post
        md_content = f"🚀 **Python Mastery Series - Topic {post_counter}: {title.title()}!** 🐍\n\n"
        md_content += f"Hey network! 👋 Today I'm sharing some sample code on **{title.title()}** in Python. "
        md_content += "Whether you're a beginner or just brushing up your basics, I hope you find this useful! 👇\n\n"
        
        md_content += "```python\n"
        md_content += "".join(content).strip() + "\n"
        md_content += "```\n\n"
        
        md_content += "What are your favorite tips regarding this topic? Let me know in the comments! 💬\n\n"
        md_content += "#Python #Coding #Programming #Developer #Learning #Tech #PythonProgramming"

        filename = os.path.join(output_dir, f"Post_{post_counter:02d}_{re.sub(r'[^a-zA-Z0-9]', '_', title)[:20]}.md")
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        post_counter += 1

    print(f"Generated {len(posts)} LinkedIn posts in {output_dir}")

if __name__ == "__main__":
    generate_linkedin_posts("Coursepython.py", "LinkedIn_Posts")
