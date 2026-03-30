import os
from PIL import Image, ImageDraw, ImageFont
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import ImageFormatter
import glob
import re

def get_font(font_names, size):
    for name in font_names:
        try:
            return ImageFont.truetype(name, size)
        except Exception:
            continue
    return ImageFont.load_default()

def wrap_text(text, font, max_width, draw):
    lines = []
    # If using Pillow < 10, textsize is used. If < 8, getsize. Let's just do a rough character wrap if needed.
    # We can just assume title fits or split by words.
    words = text.split()
    current_line = []
    for word in words:
        current_line.append(word)
        # Check width
        try:
            w = draw.textlength(" ".join(current_line), font=font)
        except AttributeError:
            # Fallback for older Pillow
            w = font.getsize(" ".join(current_line))[0]
        if w > max_width:
            current_line.pop()
            lines.append(" ".join(current_line))
            current_line = [word]
    if current_line:
        lines.append(" ".join(current_line))
    return lines

def create_image_for_post(md_filepath):
    with open(md_filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract title
    title = "Python Mastery Series"
    title_match = re.search(r'#*\s*(.*?)\n', content)
    if title_match:
        # cleanup title
        t = title_match.group(1).replace('*', '').replace('🚀', '').replace('🐍', '').strip()
        if t:
            title = t

    # Extract code
    code_match = re.search(r'```python(.*?)```', content, re.DOTALL | re.IGNORECASE)
    code = ""
    if code_match:
        code = code_match.group(1).strip()
    else:
        # try without python
        code_match = re.search(r'```(.*?)```', content, re.DOTALL)
        if code_match:
            code = code_match.group(1).strip()
            
    if not code:
        code = "# No code snippet in this post"

    # Limit code lines to prevent overflow
    code_lines = code.split('\n')
    if len(code_lines) > 35:
        code = '\n'.join(code_lines[:35]) + '\n# ... (code truncated)'

    # Generate Pygments Image
    try:
        formatter = ImageFormatter(
            font_name='Consolas', # Windows
            style='monokai',
            line_numbers=True,
            font_size=16,
            line_pad=4
        )
        code_bytes = highlight(code, PythonLexer(), formatter)
        import io
        code_img = Image.open(io.BytesIO(code_bytes))
    except Exception as e:
        print(f"Error generating pygments image: {e}")
        code_img = Image.new('RGB', (800, 400), color=(40, 40, 40))

    # Create background image 1080x1080
    bg = Image.new('RGB', (1080, 1080), color=(15, 23, 42)) # dark blue slate
    draw = ImageDraw.Draw(bg)

    # Load fonts
    title_font = get_font(["C:\\Windows\\Fonts\\segoeuib.ttf", "arialbd.ttf", "arial.ttf"], 40)
    
    # Draw Title
    title_lines = wrap_text(title, title_font, 980, draw)
    y_text = 60
    for line in title_lines:
        try:
            w = draw.textlength(line, font=title_font)
        except AttributeError:
            w = title_font.getsize(line)[0]
        x_text = (1080 - w) / 2
        draw.text((x_text, y_text), line, font=title_font, fill=(255, 255, 255))
        y_text += 50
    
    y_text += 20

    # Calculate padding and paste code image
    # We want to center the code_img 
    cw, ch = code_img.size
    
    # Scale down code image if it's too big
    max_cw = 960
    max_ch = 1080 - y_text - 50
    if cw > max_cw or ch > max_ch:
        ratio = min(max_cw/cw, max_ch/ch)
        new_size = (int(cw * ratio), int(ch * ratio))
        code_img = code_img.resize(new_size, Image.Resampling.LANCZOS)
        cw, ch = code_img.size

    x_code = (1080 - cw) // 2
    y_code = int(y_text) + (max_ch - ch) // 2
    
    # Draw a nice shadow/border behind code image
    border_radius = 10
    draw.rounded_rectangle(
        [x_code-10, y_code-10, x_code+cw+10, y_code+ch+10], 
        radius=15, 
        fill=(30, 41, 59)
    )

    bg.paste(code_img, (int(x_code), int(y_code)))

    # Save
    out_name = "Image_" + os.path.basename(md_filepath).replace('.md', '.png')
    out_path = os.path.join(os.path.dirname(md_filepath), out_name)
    bg.save(out_path)
    print(f"Generated {out_path}")

def main():
    md_files = glob.glob('Post_*.md')
    print(f"Found {len(md_files)} posts.")
    for md in md_files:
        create_image_for_post(md)

if __name__ == "__main__":
    main()
