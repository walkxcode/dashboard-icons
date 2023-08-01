from pathlib import Path

CDN_URL = "https://cdn.jsdelivr.net/gh/walkxcode/dashboard-icons/png/"
ICONS_START = "<!-- ICONS -->"
ICONS_END = "<!-- END ICONS -->"
TABLE_HEAD: str = (
    "\n\n"
    "| Icon name | SVG Support | Preview |\n"
    "| --------- | ----------- | ------- |\n"
)

ROOT = Path(__file__).parents[1].resolve()
PNG_FOLDER = ROOT / "png"
ICONS = ROOT / "ICONS.md"


def is_svg_support(file: Path) -> str:
    path = file.parents[1] / 'svg' / f"{file.stem}.svg"
    if path.exists():
        return "✅"
    return "❌"


def generate_img_tag(file: Path) -> str:
    return (
        f'<a href="{CDN_URL}{file.name}">'
        f'<img src="{CDN_URL}{file.name}" alt="{file.stem}" height="50"></a>'
    )


def generate_table_row(file: Path) -> str:
    return f"| `{file.stem}` | {is_svg_support(file)} | {generate_img_tag(file)} |"


TABLE_ROWS = "\n".join(
    generate_table_row(x)
    for x in sorted(PNG_FOLDER.glob("*.png"))
)

# Read the template file
with ICONS.open("r", encoding="UTF-8") as f:
    data = f.read()

# split template by ICONS and END ICONS
prefix, data = data.split(ICONS_START, 1)
_, suffix = data.split(ICONS_END, 1)

# Write the new file
with ICONS.open("w", encoding="UTF-8") as f:
    f.write(prefix)
    f.write(ICONS_START)
    f.write(TABLE_HEAD)
    f.write(TABLE_ROWS)
    f.write("\n\n")
    f.write(ICONS_END)
    f.write(suffix)

print("Done!")
print("Please commit the new ICONS.md file.")
