def write_content(transcript):
    """Writes content to a docx document."""
    f = open("notes.md", "w")
    f.write(transcript)
    f.close()

# Write content to the document
def write_to_file(transcript):

    write_content(transcript)

