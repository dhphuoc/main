import requests, os
from pystyle import Write, Colors, Colorate
from datetime import datetime
from time import sleep
red = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lam = "\033[1;36m"
trang = "\033[1;37m"

def banner():
    os.system('cls' if os.name=='nt' else 'clear')
    Write.Print('''            ██████╗ ██╗  ██╗██████╗  ██████╗ ███████╗
            ██╔══██╗██║  ██║██╔══██╗██╔═████╗╚════██║
            ██║  ██║███████║██████╔╝██║██╔██║    ██╔╝
            ██║  ██║██╔══██║██╔═══╝ ████╔╝██║   ██╔╝ 
            ██████╔╝██║  ██║██║     ╚██████╔╝   ██║  
            ╚═════╝ ╚═╝  ╚═╝╚═╝      ╚═════╝    ╚═╝   
    ''',Colors.blue_to_cyan,interval=0.0001)
    Write.Print('''                CopyRight: © DHP07-TOOL\n''',Colors.red_to_purple,interval=0.0001)
    print(red+"-"*70)
    print(f'''{red}[{luc}<>{red}] {tim}Admin{trang}: {lam}Đàm Hữu Phước {trang}X {vang}nguyễn Đình Hùng
{red}[{luc}<>{red}] {vang}Box Zalo{trang}: {trang} https://zalo.me/g/ixhzva608
{red}[{luc}<>{red}] {luc}Youtube{trang}: {trang} https://www.youtube.com/@fuockutii
{red}[{luc}<>{red}] {lam}Web Dvmxh{trang}: {trang} https://sharegiare.xyz''')
    print(red+"-"*70)

banner()
print(f'{Colorate.Horizontal(Colors.purple_to_blue,"┌───────────────────────────────┐")}')
print(f'{Colorate.Horizontal(Colors.purple_to_blue,"│")}{Colorate.Horizontal(Colors.blue_to_cyan,"         Trao Đổi Sub        ")}{Colorate.Horizontal(Colors.blue_to_purple,"  │")}')
print(f'{Colorate.Horizontal(Colors.purple_to_blue,"└───────────────────────────────┘")}')
print(f'{red}[{trang}<>{red}] {Colorate.Horizontal(Colors.green_to_yellow,"Nhập")} {red}[{vang}1.1{red}] {Colorate.Horizontal(Colors.green_to_yellow,"Để Chọn Chế Độ Facebook Thường")}')
print(f'{red}[{trang}<>{red}] {Colorate.Horizontal(Colors.green_to_yellow,"Nhập")} {red}[{vang}1.2{red}] {Colorate.Horizontal(Colors.green_to_yellow,"Để Chọn Chế Độ Instagram")} {vang}({red}bảo Trì{vang})')
print(f'{red}[{trang}<>{red}] {Colorate.Horizontal(Colors.green_to_yellow,"Nhập")} {red}[{vang}1.3{red}] {Colorate.Horizontal(Colors.green_to_yellow,"Để Chọn Chế Độ Facebook Page")} {vang}({red}bảo Trì{vang})')
print(f'{red}[{trang}<>{red}] {Colorate.Horizontal(Colors.green_to_yellow,"Nhập")} {red}[{vang}1.4{red}] {Colorate.Horizontal(Colors.green_to_yellow,"Để Chọn Chế Độ TikTok")} {vang}({red}bảo Trì{vang})')
print(red+"-"*70)
print(f'{Colorate.Horizontal(Colors.purple_to_blue,"┌───────────────────────────────┐")}')
print(f'{Colorate.Horizontal(Colors.purple_to_blue,"│")}{Colorate.Horizontal(Colors.blue_to_cyan,"        Tương Tác Chéo        ")}{Colorate.Horizontal(Colors.blue_to_purple," │")}')
print(f'{Colorate.Horizontal(Colors.purple_to_blue,"└───────────────────────────────┘")}')
print(f'{red}[{trang}<>{red}] {Colorate.Horizontal(Colors.green_to_yellow,"Nhập")} {red}[{vang}2.1{red}] {Colorate.Horizontal(Colors.green_to_yellow,"Để Chọn Chế Độ Facebook Thường")} {vang}({red}bảo Trì{vang})')
print(f'{red}[{trang}<>{red}] {Colorate.Horizontal(Colors.green_to_yellow,"Nhập")} {red}[{vang}2.2{red}] {Colorate.Horizontal(Colors.green_to_yellow,"Để Chọn Chế Độ Instagram")} {vang}({red}bảo Trì{vang})')
print(f'{red}[{trang}<>{red}] {Colorate.Horizontal(Colors.green_to_yellow,"Nhập")} {red}[{vang}2.3{red}] {Colorate.Horizontal(Colors.green_to_yellow,"Để Chọn Chế Độ Facebook Page")} {vang}({red}bảo Trì{vang})')
print(f'{red}[{trang}<>{red}] {Colorate.Horizontal(Colors.green_to_yellow,"Nhập")} {red}[{vang}2.4{red}] {Colorate.Horizontal(Colors.green_to_yellow,"Để Chọn Chế Độ TikTok")} {vang}({red}bảo Trì{vang})')
print(red+"-"*70)
chon = input(f'{red}[{trang}<>{red}] {Colorate.Horizontal(Colors.blue_to_white,"Chọn Chế Độ")}: ')
print(f'\n{Colorate.Horizontal(Colors.cyan_to_green,"Đang Vô Tool...")}')
try:
    if chon == '1.1':
        run = requests.get(f'https://raw.githubusercontent.com/dhphuoc/main/refs/heads/main/obf-tdsfb.py').text
    elif chon == '1.2':
        run = requests.get(f'').text
    elif chon == '1.3':
        run = requests.get(f'').text
    elif chon == '1.4':
        run = requests.get(f'').text
    elif chon == '2.1':
        run = requests.get(f'').text
    elif chon == '2.2':
        run = requests.get(f'').text
    elif chon == '2.3':
        run = requests.get(f'').text 
    elif chon == '2.4':
        run = requests.get(f'').text 
    else:
        run = print(f'{Colorate.Horizontal(Colors.red_to_purple,"Lựa Chọn Không Xác Định")}')
except:
    print(f'{Colorate.Horizontal(Colors.red_to_purple,"Sever Gặp Lỗi Hãy Liên Hệ Admin !!!")}')
    exit()
exec(run)
