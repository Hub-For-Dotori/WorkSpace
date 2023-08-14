import urllib.request

def request_url(url_addres): # url 입력을 받아서 요청을 보내 html 소스를 파싱함.
    request_result = urllib.request.urlopen(f"{url_addres}").read().decode('utf-8')
    return request_result

