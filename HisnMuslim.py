from requests import get;import re

#سكربت بسيط لحصن المسلم ينزل لك مقطع صوتي للاذكار التي تختارها السكربت كامل باللغة العربية
#https://www.hisnmuslim.com

def Stage_0():
    print('''
╦ ╦┬┌─┐┌┐┌   ╔═╗╦  ┌┬┐╦ ╦╔═╗╦  ╦╔╦╗
╠═╣│└─┐│││───╠═╣║  │││║ ║╚═╗║  ║║║║
╩ ╩┴└─┘┘└┘   ╩ ╩╩═╝┴ ┴╚═╝╚═╝╩═╝╩╩ ╩

    By @TweakPY - @vv1ck\n''')
    Stage_1()
def Stage_1():
    try:
        Finder=re.findall('''
		{
			"ID": (.*?),
			"TITLE": "(.*?)",
			"AUDIO_URL": "(.*?)",
			"TEXT": "(.*?)"
		}''',get('https://www.hisnmuslim.com/api/ar/husn_ar.json').text)
        for ID,title,audio_url,text in Finder:
            print(f'{ID} -  {title}')
        ID=input('\n[?] ادخل رقم او ايدي الذكر المطلوب من القائمة بالاعلى: ')
        Stage_2(ID)
    except Exception as e:print('[!] هناك مشكلة بالمرحلة رقم 1 ');exit(1)
def Stage_2(ID):
    try:
        Finder1=re.findall('''
		{
			"ID": '''+f"{ID}"+''',
			"TITLE": "(.*?)",
			"AUDIO_URL": "(.*?)",
			"TEXT": "(.*?)"
		}''',get('https://www.hisnmuslim.com/api/ar/husn_ar.json').text)[0]
        title=Finder1[0]
        mp3url=Finder1[1]
        fname=str(title)+".mp3" 
        with open(f'{fname}',"wb") as f:
            f.write(get(mp3url).content)
            print('[+] تم الانتهاء من تحميل مقطع صوتي للذكر المطلوب')
    except Exception as e:print('[!] هناك مشكلة بالمرحلة رقم 2 ');exit(2) 
Stage_0()