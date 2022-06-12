from pystyle import Colors, Write
import os, ctypes

ctypes.windll.kernel32.SetConsoleTitleW('I am Fausto, hi guys.')

Write.Print("Thanks for viewing my GitHub, and my repositories\n", Colors.green_to_yellow, interval=0.03)
print('')
Write.Print("I will try to upload good things, I will try to improve, so wait for me!\n", Colors.green_to_yellow, interval=0.03)
print('')
Write.Print("""About me? I'm from Costa Rica,
Im 15y, I really like Python, my favorite language, I like GoLang, im still learning, about C# I know a little, and C++ 
im still learning, i like HTML5 but, a bit tbh hahaha, and
I handle Batchfile well too. Sorry for my bad english i try to improve it day to day!\n\n""", Colors.green_to_yellow, interval=0.03)
os.system('pause')
