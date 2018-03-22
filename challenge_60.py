text_morze = {"a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".", "f":"..-.", "g":"--.", 
			  "h":"....", "i":"..", "j":".---", "k":"-.-", "l":".-..", "m":"--", "n":"-.",
			  "o":"---", "p":".--.", "q":"--.-", "r":".-.", "s":"...", "t":"-", "u":"..-",
			  "v":"..._", "w":".--", "x":"-..-", "y":"-.--", "z":"--.."}
morze_text = {".-":"a", "-...":"b", "-.-.":"c", "-..":"d", ".":"e", "..-.":"f", "--.":"g", 
			  "....":"h", "..":"i", ".---":"j", "-.-":"k", ".-..":"l", "--":"m", "-.":"n",
			  "---":"o", ".--.":"p", "--.-":"q", ".-.":"r", "...":"s", "-":"t", "..-":"u",
			  "..._":"v", ".--":"w", "-..-":"x", "-.--":"y", "--..":"z"}
text_input = input("Enter your text:")
text_output = str()
if text_input.isalpha():
	for i in text_input:
		text_output = text_output + text_morze[i] + " "
else:
	for i in text_input:
		text_output = text_output + morze_text[i] + " " 
print(text_output)
