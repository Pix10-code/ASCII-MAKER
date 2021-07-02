import ascii_magic
output = ascii_magic.from_image_file("output.jpg",columns=200,char="#")
ascii_magic.to_terminal(output)
