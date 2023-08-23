import mido

# Load the MIDI file
midi_file_path = '/home/kd/Downloads/Ballin.mid'
mid = mido.MidiFile(midi_file_path)

# Create an empty list to store the text representation
text_representation = '/home/kd/Desktop/mid.txt'
# Iterate through each MIDI message in the file
for track in mid.tracks:
    for msg in track:
        if isinstance(msg, mido.Message) and msg.type == 'note_on':
            # Convert note_on events to a readable format and append to the list
            note_name = mido.note_number_to_name(msg.note)
            text_representation.append(f"Time: {msg.time}  Note: {note_name}  Velocity: {msg.velocity}")

# Write the text representation to a text file
text_file_path = 'output_text_file.txt'
with open(text_file_path, 'w') as text_file:
    text_file.write('\n'.join(text_representation))

print("MIDI file converted to text successfully.")


