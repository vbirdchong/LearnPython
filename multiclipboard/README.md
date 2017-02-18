##### Mulit Clip Board

1. nothing in clipboard
@DESKTOP-T9C6AK0[D:multiclipboard]|20> python multiClipBoard.py list
@DESKTOP-T9C6AK0[D:multiclipboard]|21> []

2. clipboard = 'hello world'  --> key1
@DESKTOP-T9C6AK0[D:multiclipboard]|21> python multiClipBoard.py save key1    --> save 'hello world' to file
@DESKTOP-T9C6AK0[D:multiclipboard]|22> python multiClipBoard.py key1 		--> load 'hello world' from file
@DESKTOP-T9C6AK0[D:multiclipboard]|23> hello world	--> ctrl+v 


3. clipboard = 'good bye' 	--> key2
@DESKTOP-T9C6AK0[D:multiclipboard]|23> python multiClipBoard.py save key2	--> save 'good bye' to file
@DESKTOP-T9C6AK0[D:multiclipboard]|24> python multiClipBoard.py key2		--> load 'good bye' from file
@DESKTOP-T9C6AK0[D:multiclipboard]|25> good bye		--> ctrl+v

4. show all keywords 
@DESKTOP-T9C6AK0[D:multiclipboard]|25> python multiClipBoard.py list
@DESKTOP-T9C6AK0[D:multiclipboard]|26> ['key1', 'key2']  --> ctrl+v

5.delete the keyword

@DESKTOP-T9C6AK0[D:multiclipboard]|42> python multiClipBoard.py  delete key2	--> delete 'good bye' from file

@DESKTOP-T9C6AK0[D:multiclipboard]|43>		--> ctrl+v, clean the clipboard and nothing output