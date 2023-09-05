from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt

nextId = 4
topics = [
    {'id':1, 'title':'routing', 'body':'routing is..'},
    {'id':2, 'title':'views', 'body':'views is..'},
    {'id':3, 'title':'Model', 'body':'Model is..'},
]
def HTMLTemplate(articleTag):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f'''
    <html>
    <body>
        <h1><a href = "/">TW Page</a></h1>
        <ul>
            {ol}
        </ul>
        {articleTag}
        <ul>
            <li><a href = "/create/">create page</a></li>
        </ul>
    </body>
    </html>
    '''
    
    
# Create your views here. 페이지를 보이게 할 템플릿 지정하는 파일
def index(request): # 인자 이름으로 request로 받음 (관습)
    article = '''
    <h2>hello welcome!!</h2>
    It is home page..
    '''
    return HttpResponse(HTMLTemplate(article)) #HttpResponse 객체로 출력


def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article))


@csrf_exempt
def create(request):
    global nextId
    print('request.method', request.method)
    if request.method == 'GET':
        article = '''
            <form action = "/create/" method = "post">
                <p><input type = "text" name = "title" placeholder = "title"></p>
                <p><textarea name = "body" placeholder="body"></textarea></p>
                <p><input type = "submit"></p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article))
    
    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        newTopic = {"id":nextId, "title":title, "body":body}
        topics.append(newTopic)
        url = '/read/'+str(nextId)
        nextId = nextId + 1
        return redirect(url)
    
    #11강 까지 함.