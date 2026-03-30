import markdown
import subprocess
import os

def create_cheatsheet_image():
    with open('Python_Features_ShortNotes.md', 'r', encoding='utf-8') as f:
        md_text = f.read()

    html_content = markdown.markdown(md_text)

    # Wrap in a beautiful HTML layout
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <style>
        body {{
            background: #0f172a;
            color: #f1f5f9;
            font-family: 'Segoe UI', Arial, sans-serif;
            margin: 0;
            padding: 50px;
            width: 1400px;
        }}
        h1 {{
            text-align: center;
            color: #38bdf8;
            font-size: 3em;
            margin-bottom: 50px;
            text-transform: uppercase;
            letter-spacing: 2px;
        }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 30px;
        }}
        .card {{
            background: #1e293b;
            border-top: 5px solid #38bdf8;
            border-radius: 12px;
            padding: 25px;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.5);
        }}
        .card h2 {{
            color: #e2e8f0;
            margin-top: 0;
            font-size: 1.5em;
            border-bottom: 2px solid #334155;
            padding-bottom: 15px;
        }}
        .card ul {{
            padding-left: 20px;
            margin: 0;
        }}
        .card li {{
            margin-bottom: 12px;
            line-height: 1.5;
            font-size: 1.1em;
            color: #cbd5e1;
        }}
        code {{
            background: #0f172a;
            color: #fcd34d;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: Consolas, monospace;
            font-size: 0.9em;
        }}
        strong {{
            color: #f8fafc;
        }}
    </style>
    </head>
    <body>
        <h1>🐍 Python Mastery: Feature Cheat Sheet</h1>
        <div class="grid" id="grid-container">
            <!-- The markdown needs to be split into cards. Let's do a simple split -->
            {convert_h2_to_cards(html_content)}
        </div>
    </body>
    </html>
    """

    with open('cheatsheet.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("HTML created. Attempting to take a screenshot with Edge...")

    # Edge command for screenshot
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    if os.path.exists(edge_path):
        # We try to capture a specific window size that fits the grid
        cmd = [
            edge_path,
            "--headless",
            "--disable-gpu",
            "--window-size=1500,1050",
            "--screenshot=Python_Features_CheatSheet.png",
            f"file:///{os.path.abspath('cheatsheet.html').replace(chr(92), '/')}"
        ]
        try:
            subprocess.run(cmd, check=True)
            print("Successfully rendered cheatsheet image using Edge!")
        except Exception as e:
            print(f"Failed to run edge snapshot: {e}")
    else:
        print("MsEdge not found at usual path")

def convert_h2_to_cards(html_content):
    # Very rudimentary split of the HTML string to put each <h2> section into a <div class="card">
    sections = html_content.split('<h2>')
    # The first element is the h1 and some text, so we ignore it
    cards = []
    for section in sections[1:]:
        # prepend h2 back and wrap in div
        cards.append(f'<div class="card"><h2>{section}</div>')
    return "".join(cards)

if __name__ == "__main__":
    create_cheatsheet_image()
