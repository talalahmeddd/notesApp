from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)

# In-memory storage for notes
notes = []

# Load notes from a text file if it exists
if os.path.exists('notes.txt'):
    with open('notes.txt', 'r') as file:
        notes = file.readlines()

@app.route('/')
def index():
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['POST'])
def add_note():
    note = request.form.get('note')
    if note:
        notes.append(note + '\n')  # Add newline for better formatting
        save_notes()  # Save notes to file
        return note  # Return the added note for display
    return '', 400  # Return an error if no note is provided

@app.route('/delete', methods=['POST'])
def delete_note():
    note_index = int(request.form.get('index'))
    if 0 <= note_index < len(notes):
        notes.pop(note_index)  # Remove the note at the specified index
        save_notes()  # Save the updated notes to the file
        return '', 204  # Return no content
    return '', 400  # Return an error if the index is invalid

@app.route('/clear', methods=['POST'])
def clear_notes():
    global notes
    notes = []  # Clear the in-memory notes list
    save_notes()  # Save the empty list to the file
    return '', 204  # Return no content

@app.route('/download')
def download_notes():
    return send_file('notes.txt', as_attachment=True)

def save_notes():
    with open('notes.txt', 'w') as file:
        file.writelines(notes)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
