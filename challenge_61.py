ROT_13 = {"a":"n", "b":"o", "c":"p", "d":"q", "e":"r", "f":"s", "g": "t", "h":"u", "i":"v", "j":"w", "k":"x", "l":"y", "m":"z",
		  "n":"a", "o":"b", "c":"p", "q":"d","r":"e", "s":"f", "t":"g", "u":"h", "v":"i", "w":"j", "x":"k", "y":"l", "z":"m"}
text_input = input("Enter your text: ")
text_output = ""
for i in text_input:
		text_output = text_output + ROT_13[i]
print (text_output)
