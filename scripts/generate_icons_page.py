import pathlib
from pathlib import Path
import sys

def generate_img_tag(file):
    return (
        f'<a href="https://cdn.jsdelivr.net/gh/walkxcode/dashboard-icons/webp/{file.name}">'
        f'<img src="https://cdn.jsdelivr.net/gh/walkxcode/dashboard-icons/webp/{file.name}" '
        f'alt="{file.stem}" height="50"></a>'
    )

if __name__ == "__main__":
    root = pathlib.Path(__file__).parent.resolve()
    template_path = root / "TEMPLATE.md"
    icons_md_path = root.parent / "ICONS.md"

    imgs = sorted((root.parent / "webp").glob("*.webp"))
    img_tags = [generate_img_tag(x) for x in imgs]

    # Read the template file
    with open(template_path, "r", encoding="UTF-8") as f:
        lines = f.readlines()

    # Find the line that starts with "<!-- ICONS -->"
    try:
        line_number = lines.index("<!-- ICONS -->\n")
    except ValueError:
        print("<!-- ICONS --> placeholder not found in TEMPLATE.md")
        sys.exit(1)

    # Insert the icons after the placeholder
    lines.insert(line_number + 1, " ".join(img_tags) + "\n")

    # Write the new ICONS.md file
    with open(icons_md_path, "w", encoding="UTF-8") as f:
        f.writelines(lines)

    print("ICONS.md has been successfully generated.")