# Notes App

A simple web application for taking and managing notes using Flask and local storage. This app allows users to add, delete, and clear notes, with the ability to toggle between light and dark themes.

## Features

- Add notes to a list.
- Delete individual notes.
- Clear all notes.
- Toggle between light and dark themes.
- Notes are stored in the browser's local storage, ensuring persistence across page reloads.

## Technologies Used

- Flask: A lightweight WSGI web application framework in Python.
- HTML/CSS: For structuring and styling the web application.
- JavaScript: For client-side interactivity and local storage management.
- Bootstrap: For responsive design and styling.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/notes-app.git
   cd notes-app
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install Flask
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **Open your web browser and navigate to:**
   ```
   http://127.0.0.1:5001
   ```

## Usage

- To add a note, type your note in the text area and click the "Add Note" button.
- To delete a note, click the "✖" button next to the note you want to remove.
- To clear all notes, click the "Clear Notes" button.
- Use the "Download Notes" button to download your notes (if implemented).
- Toggle between light and dark themes using the theme toggle button.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 

