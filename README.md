# Minecraft Mod Manager (mmm)

The Minecraft Mod Manager (mmm) project is inspired by package managers like npm and yarn. The main goal of the project is to facilitate the distribution of custom modpacks using a `mods.json` file, similar to `package.json`, which speeds up the process of downloading modpacks. **IMPORTANT:** This project is currently in the early stages of development, and as my first project in Python, it may contain bugs and efficiency issues.

## Features

- **Primary Feature:** Downloads mods by reading from a `mods.json` file using the Modrinth API (currently).
- **Advanced Search:** Utilizes numerous options provided by the Modrinth API to help users find the desired mods. [Modrinth API](https://modrinth.com/api).
- **Update:** Allows you to update individual mods to your preferred version or update all mods based on the Minecraft version.

## Installation

To install the Minecraft Mod Manager (mmm), follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/mmm.git
   cd mmm
   ```

2. Install the required dependencies:

   ```bash
   pipx install .
   ```

3. Ensure you have Python 3.6 or higher installed on your machine.

## Usage

- `mmm init`: Initializes the `mods.json` file required for the program to function.
- `mmm install [mod_name...]`: Finds and downloads the specified mod(s) along with their dependencies.
- `mmm update [mod_name] -l -v`: Updates the selected mod or updates all mods.

## Contributing

Contributions are welcome! If you want to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to the [Modrinth API](https://modrinth.com/api) for providing the mod search functionality.
- Inspiration from npm and yarn for creating a user-friendly package manager experience.

**Note:** This project is still under development, and feedback is greatly appreciated!
