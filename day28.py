#string formatting
name="kenshi"
country="Bharatvarsha"
print(f"Hi, Hello, Namashkaar !, mai {name} se milna chahta hu, {country} se,nhi milne doge to mai {{country}} aake usko goli maar dunga")
txt="let me sell you for {price:.2f} dollars"
print(txt.format(price=493233.344443243224343432324432234))
paisa=000000000000000123.1223123322112002213022023032
txt2=f'"hey you!, were you sold for {paisa:.2f} dollars?,""no!, i was sold for {paisa:.2f} rupees"'
print(txt2)