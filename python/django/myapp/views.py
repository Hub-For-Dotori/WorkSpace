from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt

nextId = 4
topics = [ # 리스트를 큰 저장소로 잡고 세부 내용은 딕셔너리로 묶어둠.
    {'id':1, 'title':'routing', 'body':'routing is..'},
    {'id':2, 'title':'views', 'body':'views is..'},
    {'id':3, 'title':'Model', 'body':'Model is..'},
]
def HTMLTemplate(articleTag, id=None): # HTML의 탬플릿 지정해줌.
    global topics # 함수 밖의 topics를 사용하기 위함.
    contextUI = ''
    if id != None:
        contextUI = f'''
            <li>
                <form action="/delete/" method="post">
                    <input type="hidden" name="id" value={id}>
                    <input type="submit" value="delete">
                </form>
            </li>
            <li>
                <a href = "/update/{id}">update</a>
            <li>
        '''
    ol = '' # ol 태그 초기화
    for topic in topics: # topics의 0번 부터 topic으로 불러옴.
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>' # topic
    return f'''
    <html>
    <body>
        <h1><a href = "/">TW Page</a></h1>
        <ul>
            {ol}
        </ul>
        {articleTag}
        <ul>
            <li><a href="/create/">create page</a></li>
            {contextUI}
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
    return HttpResponse(HTMLTemplate(article, id))


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

@csrf_exempt   
def delete(request):
    global topics
    if request.method == 'POST':
        id = request.POST['id']
        newTopics = []
        for topic in topics:
            if topic['id'] != int(id):
                newTopics.append(topic)
        topics = newTopics        
        return redirect('/')

@csrf_exempt   
def update(request, id):
    global topics
    if request.method == 'GET':
        for topic in topics:
            if topic['id'] == int(id):
                selectedTopic = {
                    "title":topic['title'],
                    "body":topic['body']
                    }
        article = f'''
            <form action = "/update/{id}/" method = "post">
                <p><input type = "text" name = "title" placeholder = "title" value={selectedTopic["title"]}></p>
                <p><textarea name = "body" placeholder="body">{selectedTopic['body']}</textarea></p>
                <p><input type = "submit"></p>
            </form>
        '''
        return(HttpResponse(HTMLTemplate(article, id)))
    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        for topic in topics:
            if topic['id'] == int(id):
                topic['title'] = title
                topic['body'] = body        
        return redirect(f'/read/{id}/')