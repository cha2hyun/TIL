import requests, json
 
ARTICLE_LIST_MAIN_PATH = 'https://apis.naver.com/cafe-web/cafe2/ArticleList.json'

def getArticleList(CAFE_UNIQUE_ID, REQUEST_LIST_PAGE_NUM, REQUEST_LIST_SCOPE, MODULE_REQUEST_SESSION):
    # 페지네이션 20개씩 불러옴
    requestParameter = {
        "search.clubid": CAFE_UNIQUE_ID,
        "search.menuid": REQUEST_LIST_SCOPE,
        "search.page": REQUEST_LIST_PAGE_NUM
    }
    session = MODULE_REQUEST_SESSION
    request = session.get(ARTICLE_LIST_MAIN_PATH, params=requestParameter)
    resp = request.text
    if request.status_code == 200:
        return json.loads(resp)
    else:
        print("200 failed")
        return False
 
def getArticleBody(CAFE_UNIQUE_ID, ARTICLE_UNIQUE_ID, MODULE_REQUEST_SESSION):
    Request_URI = "https://apis.naver.com/cafe-web/cafe-articleapi/cafes/"+CAFE_UNIQUE_ID+"/articles/"+ARTICLE_UNIQUE_ID
    request = MODULE_REQUEST_SESSION
    resp = request.get(Request_URI)
    return json.loads(resp.text)["article"]
     
def saveToJson(contetnt, folderName, fileName):
    BASE_URL = "./" + folderName + "/" 
    URL = BASE_URL + fileName + ".json"
    with open(URL, 'w', encoding='utf-8') as outfile:
        json.dump(contetnt, outfile, indent=4, ensure_ascii=False)

def main():
    MainSession = requests.Session()
    response = getArticleList(24485008, 3, 64, MainSession)
    ArticleList = response['message']['result']['articleList']
    saveToJson(ArticleList, "test", "ArticleList")
    ArticleBody = getArticleBody("24485008", "749191", MainSession)
    saveToJson(ArticleBody, "test", "ArticleBody")
    
    # for Article in ArticleList:
    #     if '달의 이벤트' in Article["subject"]:
    #         print(Article["subject"])
    #         number = str(Article["articleId"])
    #         break
    # print(getArticleBody("25490972", number, MainSession))
 
main()