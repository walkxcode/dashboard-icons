import pathlib
from pathlib import Path

root = pathlib.Path(__file__).parent.resolve()
template_path = root / "_TEMPLATE.md"
readme_path = root / "README.md"


def generate_img_tag(file):
    return f'<img src="png/{file.name}" alt="{file.stem}" height="50">'


imgs = sorted(Path("./png").glob("*.png"))
img_tags = [generate_img_tag(x) for x in imgs]
line_number = 0

# Read the template file
with open(template_path, "r", encoding="UTF-8") as f:
    lines = f.readlines()
# Find the line that starts with "<!-- ICONS -->"
for line in lines:
    if line.startswith("<!-- ICONS -->"):
        line_number = lines.index(line)
        break
# Insert the icons after the line
lines.insert(line_number + 1, " ".join(img_tags))
# Write the new file
with open(readme_path, "w", encoding="UTF-8") as f:
    f.write("".join(lines))
    f.write("\n")
print("Done!")
print("Please commit the new README.md file.")
