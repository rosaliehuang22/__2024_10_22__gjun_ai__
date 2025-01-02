- 一個專案 = 一各資料夾 (但因這是小專案，目前用lesson21資料夾)

## 課程步驟
- Step 1: 新增main.py
- Step 2: 新增requirement.txt  
    Important: 安裝任何framework前，需要更新PIP檔  
    ```pip install --upgrade pip```  
    (AI assistance: 如果不會做，可參考Copilot)
- Step 3: 安裝需要使用的framework  
    先在requirement.txt輸入"framework名稱 == version"：Flask == 3.1.0  
    ```pip install -r requirements.txt```

### 建立Flask伺服器 = A Minimal Application：
- 可在Google搜尋這程式碼 "A Minimal Application Flask API"
    ```
    from flask import Flask

    app = Flask(__name__) #Create the App
    
    @app.route('/') #Sets up a URL route
    def hello_world(): #Function is called when someone visits the homepage
        return 'Hello, World!'
    ```
- 在main.py貼上該程式碼
- 在TERMINAL執行 "flask --app [module name] run"：flask --app main run
- 出現網址，可點進去查看  
    Important: 如果無法進入網站，在PORTS內刪除不用到的Ports
- 如有修改程式碼，務必Ctrl+C關掉伺服器，重新啟動才會看到喔~

### 建立第二頁 = Routing：
- 在原本檔案輸入程式碼就完成建立/hello的分頁
    ```
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    ```
## 生成式AI
- ChatGPT: https://platform.openai.com/docs/api-reference/introduction  
    Note: OPENAI_API_KEY = 需要付錢才有key
- Gemini: https://ai.google.dev/gemini-api/docs?gad_source=1&gclid=Cj0KCQiAj9m7BhD1ARIsANsIIvBH_kdQVs9PX1FzwgGvcg0ANZOb1AO3nuB-voOofjgkqK85wJkHTksaAitDEALw_wcB

### 使用Gemini Developer API
- Step 1: Get a Gemini API Key
- Step 2: Develop in your own environment
- Step 3: Create API Key
- Step 4: Copy API key adn test it here (lesson21_1.ipynb)
- Step 5: Download or install libraries to access Gemini
- Step 6: Gemini API quickstart
    ```
    import google.generativeai as genai

    genai.configure(api_key="YOUR_API_KEY")
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content("Explain how AI works")
    print(response.text)
    ```

###模擬電腦環境變數 (保護password)
使用dotenv
- 下載 + 安裝
- 在資料夾新增'.env'檔案
- 在該檔案內，輸入項隱藏的東西，如 ```Gemini_API_KEY=OXOXOXOXOXO```
- 設定不上傳github：新增'.gitignore'檔案，並在檔案內輸入不要上傳的檔名
-使用時，輸入```from dotenv import load_dotenv```

###安裝unicorn
- 下載 + 安裝
- 再次安裝"gunicorn -w 4 module:伺服器"：```gunicorn -w 4 main:app```
