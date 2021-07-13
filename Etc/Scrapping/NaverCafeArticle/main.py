import requests, json, csv
from datetime import datetime
from tqdm import tqdm

ARTICLE_LIST_MAIN_PATH = 'https://apis.naver.com/cafe-web/cafe2/ArticleList.json'
CLUB_ID = XXXXXXX              # 카페 고유번호
MENU_ID = 64                    # 카테고리 고유번호
TOTAL_ARTICLE_COUNT = 20000     # 불러올 게시글 총 갯수 (최대 2만개)
ARTICLE_LIST_COUNT = 20         # getArticleList 에서 한번에 받아 오는 param 수 (고정값이므로 수정 X)
PAGES = TOTAL_ARTICLE_COUNT // ARTICLE_LIST_COUNT + 1 if TOTAL_ARTICLE_COUNT > ARTICLE_LIST_COUNT else 1



def getArticleList(CAFE_UNIQUE_ID, REQUEST_LIST_PAGE_NUM, REQUEST_LIST_SCOPE, MODULE_REQUEST_SESSION):
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
     
def saveToJson(content, folderName, fileName):
    BASE_URL = "./" + folderName + "/" 
    PATH = BASE_URL + fileName + ".json"
    with open(PATH, 'w', encoding='utf-8') as jsonFile:
        json.dump(content, jsonFile, indent=4, ensure_ascii=False)
    
def saveToCSV(content, folderName, fileName):
    BASE_URL = "./" + folderName + "/" 
    PATH = BASE_URL + fileName + ".csv"
    with open(PATH, 'w', newline='', encoding='utf-8-sig') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(["row", "row", "row", "row", "row", "row", "row", "row", "row", "row", "row"])
        for row in content:
            writer.writerow(row)

def validateAndSaveToCSV(content, folderName, fileName):
    BASE_URL = "./" + folderName + "/" 
    PATH = BASE_URL + fileName + ".csv"
    all_article_count = 0
    all_price_total = 0
    under50_article_count = 0
    under50_price_total = 0
    over50_article_count = 0
    over50_price_total = 0
    longoni_article_count = 0
    longoni_price_total = 0
    buffalo_invick_article_count = 0
    buffalo_invick_price_total = 0


    datas = []
    data_02 = []
    data_01 = []
    data_12 = []
    data_11 = []
    for article in content:
        price = article[5]
        all_article_count += 1
        all_price_total += price

        if "02" in article[4].split("-")[1]:
            if price < 500000:           
                under50_article_count += 1
                under50_price_total += price
            if price >= 500000:
                over50_article_count += 1
                over50_price_total += price
            if article[8] == True:
                longoni_article_count += 1 
                longoni_price_total += price
            if article[9] == True or article[10] == True:
                buffalo_invick_article_count += 1
                buffalo_invick_price_total += price

        datas.append([
            all_article_count,
            all_price_total,
            0,
            under50_article_count,
            under50_price_total,
            0,
            over50_article_count,
            over50_price_total,
            0,
            longoni_article_count,
            longoni_price_total,
            0,
            buffalo_invick_article_count,
            buffalo_invick_price_total,
            0,
        ])
        with open(PATH, 'w', newline='', encoding='utf-8-sig') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(["row", "row", "row", "row", "row", "row", "row", "row", "row", "row", "row", "row", "row", "row", "row" ])
        
            for row in datas:
                writer.writerow(row)

def setCategory(MENU_ID, MainSession):
    articles = []
    count = 1
    for PAGE in tqdm(range(0, PAGES)):
        response = getArticleList(CLUB_ID, PAGE, MENU_ID, MainSession)
        ArticleList = response['message']['result']['articleList']
        for Article in ArticleList:
            articles.append([
                count,
                Article['articleId'],
                Article['subject'],
                Article['writerId'],
                datetime.fromtimestamp(Article['writeDateTimestamp'] / 1000).strftime('%Y-%m-%d %H:%M:%S'),
                Article['cost'],
                Article['readCount'],
                Article['onSale'],
                True if ("롱고니" in Article['subject']) or ("S20" in Article['subject']) or ("VP2" in Article['subject']) else False,
                True if "버팔로" in Article['subject'] else False,
                True if ("인빗큐" in Article['subject']) or ("row" in Article['subject']) else False,
            ])
            count += 1
    
    return articles

def main():
    # 세션
    MainSession = requests.Session()
    
    # 팝니다 게시판
    MENU_ID = 64
    articles = setCategory(MENU_ID, MainSession)
    saveToCSV(articles, "output", "sell-articles")
    # validateAndSaveToCSV(articles, "output", "filtered-sell-articles")

    # 삽니다 게시판
    MENU_ID = 151
    articles = setCategory(MENU_ID, MainSession)
    saveToCSV(articles, "output", "buy-articles")
 
main()
