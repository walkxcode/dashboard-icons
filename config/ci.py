from pathlib import Path

config = Path(__file__).parent.resolve()
root = config.parent
template_path = config / "TEMPLATE.md"
icons = root / "ICONS.md"


def generate_img_tag(file: Path) -> str:
    return f'<a href="https://cdn.jsdelivr.net/gh/walkxcode/dashboard-icons/png/{file.name}"><img src="https://cdn.jsdelivr.net/gh/walkxcode/dashboard-icons/png/{file.name}" alt="{file.stem}" height="50"></a>'


img_tags = [generate_img_tag(x) for x in sorted((root / "png").glob("*.png"))]
line_number = 0

# Read the template file
with template_path.open("r", encoding="UTF-8") as f:
    lines = f.readlines()

# Find the line that starts with "<!-- ICONS -->"
for line in lines:
    if line.startswith("<!-- ICONS -->"):
        line_number = lines.index(line)
        break

# Insert the icons after the line
lines.insert(line_number + 1, " ".join(img_tags))

# Write the new file
with icons.open("w", encoding="UTF-8") as f:
    f.write("".join(lines))
    f.write("\n")

print("Done!")
print("Please commit the new ICONS.md file.")
