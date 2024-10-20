import os
import re
import hashlib
from pathlib import Path
from PIL import Image
import cairosvg

# Define paths
ROOT_DIR = Path(__file__).resolve().parent.parent
SVG_DIR = ROOT_DIR / "svg"
PNG_DIR = ROOT_DIR / "png"
WEBP_DIR = ROOT_DIR / "webp"

# Ensure the output folders exist
PNG_DIR.mkdir(parents=True, exist_ok=True)
WEBP_DIR.mkdir(parents=True, exist_ok=True)

# Track results
failed_files = []
converted_pngs = 0
converted_webps = 0
total_icons = 0

def file_size_readable(size_bytes):
    """Convert bytes to a human-readable format."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024

def hash_file(file_path):
    """Generate an MD5 hash for a file."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def convert_to_kebab_case(name):
    """Convert a filename to kebab-case."""
    cleaned = re.sub(r'[^a-zA-Z0-9\s-]', '', name)
    kebab_case_name = re.sub(r'[\s_]+', '-', cleaned).lower()
    return kebab_case_name

def rename_if_needed(file_path):
    """Ensure the filename is in kebab-case; rename if necessary."""
    new_name = convert_to_kebab_case(file_path.stem) + file_path.suffix
    new_path = file_path.parent / new_name

    if new_path != file_path:
        if new_path.exists():
            raise FileExistsError(f"File conflict: {new_path} already exists.")
        file_path.rename(new_path)
        print(f"Renamed: {file_path} -> {new_path}")

    return new_path

def needs_conversion(output_file, data=None):
    """Check if a file needs to be converted or overwritten."""
    if output_file.exists():
        if data:
            existing_hash = hash_file(output_file)
            new_hash = hashlib.md5(data).hexdigest()
            return existing_hash != new_hash
        return False
    return True

def convert_svg_to_png(svg_path, png_path):
    """Convert SVG to PNG."""
    global converted_pngs
    try:
        png_data = cairosvg.svg2png(url=str(svg_path), output_height=512)

        if needs_conversion(png_path, png_data):
            with open(png_path, 'wb') as f:
                f.write(png_data)
            print(f"Converted PNG: {png_path} ({file_size_readable(png_path.stat().st_size)})")
            converted_pngs += 1
        else:
            print(f"PNG already up-to-date: {png_path}")

    except Exception as e:
        print(f"Failed to convert {svg_path} to PNG: {e}")
        failed_files.append(svg_path)

def convert_png_to_webp(png_path, webp_path):
    """Convert PNG to WEBP."""
    global converted_webps
    try:
        image = Image.open(png_path)

        if needs_conversion(webp_path):
            image.save(webp_path, format='WEBP')
            print(f"Converted WEBP: {webp_path} ({file_size_readable(webp_path.stat().st_size)})")
            converted_webps += 1
        else:
            print(f"WEBP already up-to-date: {webp_path}")

    except Exception as e:
        print(f"Failed to convert {png_path} to WEBP: {e}")
        failed_files.append(png_path)

def clean_up_files(folder, valid_basenames):
    """Remove files that no longer have corresponding SVG files."""
    removed_files = 0
    for file_path in folder.glob('*'):
        if file_path.stem not in valid_basenames:
            file_path.unlink()
            print(f"Removed: {file_path}")
            removed_files += 1
    return removed_files

if __name__ == "__main__":
    # Track valid basenames (existing SVG files)
    valid_basenames = set()

    # Process all SVG files
    for svg_file in SVG_DIR.glob("*.svg"):
        total_icons += 1

        # Ensure the filename is in kebab-case
        try:
            svg_path = rename_if_needed(svg_file)
        except Exception as e:
            print(f"Error renaming {svg_file}: {e}")
            failed_files.append(svg_file)
            continue

        valid_basenames.add(svg_path.stem)

        # Set paths for PNG and WEBP
        png_path = PNG_DIR / f"{svg_path.stem}.png"
        webp_path = WEBP_DIR / f"{svg_path.stem}.webp"

        # Convert SVG to PNG
        convert_svg_to_png(svg_path, png_path)

        # Convert PNG to WEBP
        if png_path.exists():
            convert_png_to_webp(png_path, webp_path)

    # Clean up unused files
    removed_pngs = clean_up_files(PNG_DIR, valid_basenames)
    removed_webps = clean_up_files(WEBP_DIR, valid_basenames)

    # Display summary
    if converted_pngs == 0 and converted_webps == 0 and removed_pngs == 0 and removed_webps == 0:
        print("\nAll icons are already up-to-date.")
    else:
        print(f"\nConverted {converted_pngs} PNGs and {converted_webps} WEBPs out of {total_icons} icons.")
        print(f"Removed {removed_pngs} PNGs and {removed_webps} WEBPs.")

    # Display any failed conversions
    if failed_files:
        print("\nThe following files failed to convert:")
        for file in failed_files:
            print(file)