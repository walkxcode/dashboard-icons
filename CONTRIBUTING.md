![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen?style=flat-square)

## Contribution Guidelines

Thank you for your interest in contributing to the icon repository! To ensure smooth collaboration, please follow these guidelines. Your contributions help make this project better.

## Table of Contents

- [Contribution Guidelines](#contribution-guidelines)
- [Table of Contents](#table-of-contents)
- [Icon Specifications](#icon-specifications)
  - [Format](#format)
  - [Cropping](#cropping)
  - [Light and Dark Versions](#light-and-dark-versions)
  - [File Naming](#file-naming)
  - [Quality Requirements](#quality-requirements)
- [Git Commit Messages](#git-commit-messages)
- [Contribution Process](#contribution-process)
- [Code of Conduct](#code-of-conduct)
- [Contact](#contact)

## Icon Specifications

### Format

- **SVG Format Required**: All icons must be submitted in SVG format.
- **Automatic PNG and WEBP Generation**: PNG and WEBP versions are generated automatically from the SVG files using the following settings:
  - **Dimensions**:
    - Height: 512 pixels
    - Width: Auto (maintaining aspect ratio)
  - **Transparency**: Enabled

### Cropping

- **Remove Empty Space**: Crop any empty space from your SVG files to ensure the icon is properly centered and sized. You can use [SVG Crop](https://svgcrop.com/) to assist with this.

### Light and Dark Versions

- **Monochrome or Single Primary Color Icons**:
  - If your icon is monochrome, please provide additional versions if applicable:
    - **`-light` Version**: For icons primarily dark or using black as a main color, provide a `-light` version for light backgrounds.
    - **`-dark` Version**: For icons primarily light or using white as a main color, provide a `-dark` version for dark backgrounds.
  - **Examples**:
    - A black logo should include a `-light` version where black is inverted.
    - A multicolored logo using black should provide a `-light` version with the black replaced.
  - **Tool Recommendation**: [DEEditor](https://deeditor.com/) can help adjust icon colors if needed.

### File Naming

- **Kebab Case**: Name your files using kebab case (lowercase words separated by hyphens). For example, "Nextcloud Calendar" becomes `nextcloud-calendar.svg`.
  - **Note**: Filenames are automatically converted to kebab case, but please double-check your naming to avoid conflicts or errors.

### Quality Requirements

- **No Upscaled Images**: Icons should maintain their original quality without artificial enlargement.
- **No Embedded Raster Images in SVGs**: Ensure that SVG files are true vector graphics without embedded raster images.

## Git Commit Messages

- **Use Gitmoji**: Incorporate [Gitmoji](https://gitmoji.dev/) in your commit messages to keep the commit history clear and expressive. For example:
  - `:bento: Adds xxx` when adding new icons.

## Contribution Process

1. **Fork the Repository**: Create a fork of this repository on your GitHub account.
2. **Clone the Repository**: Clone your forked repository to your local machine.
3. **Add Your Icons**: Place your SVG icon(s) into the appropriate directory, following the specifications above.
4. **Commit Your Changes**: Commit your additions with clear and descriptive commit messages using Gitmoji.
5. **Push to Your Fork**: Push your committed changes to your forked repository on GitHub.
6. **Create a Pull Request**: Submit a pull request to the main repository for review.

## Code of Conduct

By contributing, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md). Please review it to understand the expectations for all participants.

## Contact

If you have any questions or need assistance, feel free to reach out at [bjorn@lammers.media](mailto:bjorn@lammers.media). I'm happy to help.