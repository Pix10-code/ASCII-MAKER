import ascii_magic
output = ascii_magic.from_image_file("output.png",columns=200,char="#")
ascii_magic.to_terminal(output)
