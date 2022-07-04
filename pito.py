import os
import ua_generator
from pystyle import Colors

os.system("cls")

while True:
    print(f"{Colors.light_green}")
    ua = ua_generator.generate(device='desktop', browser='firefox')
    print(ua.text)
    ua = ua_generator.generate(device='mobile', platform='android', browser='chrome')
    print(ua.text)
    ua = ua_generator.generate(platform=('ios', 'macos'), browser='chrome')
    print(ua.text)
    ua = ua_generator.generate(device='desktop', browser='chrome', platform='macos')
    print(ua.text)
    ua = ua_generator.generate(device='desktop', browser='chrome')
    print(ua.text)
    ua = ua_generator.generate(device='mobile', platform='android', browser='firefox')
    print(ua.text)
    ua = ua_generator.generate(platform=('ios', 'macos'), browser='safari')
    print(ua.text)
    ua = ua_generator.generate(device='desktop', browser='chrome', platform='linux')
    print(ua.text)
    ua = ua_generator.generate(device='desktop', browser='firefox')
    print(ua.text)
    ua = ua_generator.generate(device='mobile', platform='android', browser='chrome')
    print(ua.text)
