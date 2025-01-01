# Pickup Line Generator: Sagar the Virtual Assistant

This repository contains a Python-powered virtual assistant named **Sagar**. It specializes in generating creative, hacker-inspired pickup lines and handling user commands interactively. Whether you're looking to impress or just have fun, Sagar is here to help!

## Features

- **AI-Powered Pickup Lines**: Generates witty, personalized pickup lines with a touch of hacker-style creativity.
- **Interactive Context**: Tracks conversations for more engaging and relevant responses.
- **Expandable Design**: Easily add new commands or tweak existing functionality.
- **Simple and Fun**: A lightweight, easy-to-use script for entertainment purposes.

## How It Works

1. **User Input**: Enter a command starting with "pickup" or any other phrase you'd like the assistant to respond to.
2. **AI Processing**: The script uses the Groq API to process the input and generate a response based on the command and context.
3. **Interactive Responses**: The assistant returns a creative and engaging reply, tailored to your input.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo-url/pickup-line-generator.git
   ```
2. Navigate to the directory:
   ```bash
   cd pickup-line-generator
   ```
3. Install the required dependencies:
   ```bash
   pip install groq
   ```

## Usage

1. Run the script:
   ```bash
   python your_script_name.py
   ```
2. Enter commands in the terminal, such as:
   ```
   ==> pickup line about cybersecurity
   ```
3. To exit the program, type:
   ```
   exit
   ```

## Example Commands

- `pickup line about coding`
- `pickup line about love`
- `pickup line about black-hat hacking`

## Customization

- Modify the **system messages** in the `aiProsses` function to adjust the assistant's tone and style.
- Add new commands or features in the `prossess_command` function.

## Contributing

Feel free to fork the repository, make changes, and submit pull requests! Suggestions and improvements are always welcome.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Have fun generating unique and entertaining pickup lines with **Sagar**!
```
