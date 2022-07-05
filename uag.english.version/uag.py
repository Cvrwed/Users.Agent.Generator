import os
import ua_generator
from pystyle import *

def clear(): #clean
    if os.name == "nt":
        os.system("cls")
    elif os.name == ("posix"):
        os.system("clear")

clear()

purple_to_red = Colors.purple_to_red
System.Title("Press ENTER")
Cursor.HideCursor()
banner = r"""
   _                        _                    _        
  /\_\                     / /\                 /\ \      
 / / /         _          / /  \               /  \ \     
 \ \ \__      /\_\       / / /\ \             / /\ \_\    
  \ \___\    / / /      / / /\ \ \           / / /\/_/    
   \__  /   / / /      / / /  \ \ \         / / / ______  
   / / /   / / /      / / /___/ /\ \       / / / /\_____\ 
  / / /   / / /      / / /_____/ /\ \     / / /  \/____ / 
 / / /___/ / /      / /_________/\ \ \   / / /_____/ / /  
/ / /____\/ /      / / /_       __\ \_\ / / /______\/ /   
\/_________/       \_\___\     /____/_/ \/___________/    
                                                          
                                                          

"""

Anime.Fade(Center.Center(banner), purple_to_red, Colorate.Vertical, enter=True)
System.Title("Users Agent Generator")
Cursor.HideCursor()
Write.Input(f'\n [+] Press enter to start...', purple_to_red, interval=0)
clear()
while True:
    Desktop_firefox = ua_generator.generate(device='desktop', browser='firefox')
    Android_chrome = ua_generator.generate(device='mobile', platform='android', browser='chrome')
    IOS_chrome = ua_generator.generate(platform=('ios', 'macos'), browser='chrome')
    Desktop_chrome = ua_generator.generate(device='desktop', browser='chrome')
    Android_firefox = ua_generator.generate(device='mobile', platform='android', browser='firefox')
    MacOS_safari = ua_generator.generate(platform=('ios', 'macos'), browser='safari')
    Linux_chrome = ua_generator.generate(device='desktop', browser='chrome', platform='linux')
    print(Colorate.Diagonal(purple_to_red, f""" 
    {Desktop_firefox}
    {Android_chrome}
    {IOS_chrome}
    {Desktop_chrome}
    {Android_firefox}
    {MacOS_safari}
    {Linux_chrome}"""))
    f = open('useragents.txt', "a+")
    f.write(f'{Desktop_chrome}\n')
    f.write(f'{Android_chrome}\n')
    f.write(f'{IOS_chrome}\n')
    f.write(f'{Desktop_firefox}\n')
    f.write(f'{Android_firefox}\n')
    f.write(f'{MacOS_safari}\n')
    f.write(f'{Linux_chrome}\n')
    f.close()
