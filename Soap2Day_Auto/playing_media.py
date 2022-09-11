'''
allows you to connect to local chromecasts 
FUTURE SUPPORT MAY INCLUDE AIRPLAY, etc
'''
import pychromecast, time
from ffmpeg import video

cast = 0

def choose_chromecast():
    global cast
    #finds all available chromecasts
    services, browser = pychromecast.discovery.discover_chromecasts()
    pychromecast.stop_discovery(browser)

    #prints all available chromecasts via name
    print('Available Chromecasts: \n')
    for x in range(len(services)):
        print(f'({x}) : {services[x].friendly_name}')
    print('\n\n\n')

    #sets the target chromecast
    while True:
        choice = int(input('Choose the one you want to connect to: '))
        if choice in list(range(len(services))):
            print('CONNECTING....')
            chromecasts, browser = pychromecast.get_listed_chromecasts(uuids=[services[choice].uuid])
            cast = chromecasts[0]
            cast.wait()
            break

    #closes out of any running apps on the chromecast
    if not cast.is_idle:
        print("Killing current running app")
        cast.quit_app()
        t = 5
        while cast.status.app_id is not None and t > 0:
            time.sleep(0.1)
            t = t - 0.1

def send_to_chromecast(url):
    global cast
    try:
        while True:
            print('Playing media...')
            cast.media_controller.play_media(url, "video/mp4")
            try:
                time.sleep(500)
            except:
                pass

    except:
        try:
            print('Stopping')
            cast.stop()
        except:
            try:
                print('Quitting')
                cast.quit_app()
            except:
                 pass




choose_chromecast()
send_to_chromecast('https://f1.mrqls.to/a/t4/spongebob-squarepants/s04e32.mp4?tok=34386C4F506C50344C717832487137704D72426559486A544E382533444255346B694E6D75674E6D6725334447302D71483546714C45542D5A6D664257366B7A4B6869642D32516649346165576D68644D7A416954734C6461364247506C66344C71674335316579423455564C304165507163635A7068692D79434E503330334936715A507168704B30646464&valid=cW5eMhcb-wrL8RD4DOV0BA&t=1662864013')