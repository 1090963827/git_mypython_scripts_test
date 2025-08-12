from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML 模板
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>愿不愿意做爸爸的小狗？</title>
    <style>
        body {
            background-color: #f1d5da;
            text-align: center;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
            margin: 0;
            padding: 0;
            height: 100vh;
            overflow: hidden;
            -webkit-tap-highlight-color: transparent;
        }
        .container {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 90%;
            max-width: 500px;
        }
        #mainImage {
            width: 60vw;
            max-width: 200px;
            transition: all 0.3s ease;
            user-select: none;
            -webkit-user-select: none;
        }
        h1 {
            font-size: min(7vw, 28px);
            color: #68495b;
            margin: 20px 0;
            user-select: none;
            -webkit-user-select: none;
        }
        .buttons {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
        }
        button {
            font-size: min(5vw, 18px);
            padding: 12px 24px;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            margin: 10px;
            transition: all 0.3s ease;
            min-width: 100px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
            -webkit-tap-highlight-color: transparent;
        }
        #yes {
            background-color: #d4818e;
            color: white;
        }
        #no {
            background-color: #6784b1;
            color: white;
            position: relative;
        }
        .yes-screen {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background-color: #ffdae0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            z-index: 100;
        }
        .yes-text {
            font-size: min(8vw, 32px);
            color: #d4818e;
            margin-bottom: 30px;
        }
        .yes-image {
            width: 70vw;
            max-width: 300px;
            animation: bounce 0.8s infinite alternate;
        }
        @keyframes bounce {
            from { transform: translateY(0); }
            to { transform: translateY(-20px); }
        }
        @media screen and (max-width: 500px) {
            button {
                touch-action: manipulation;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <img id="mainImage" src="https://zhengdef.github.io/xg/images/001.png" alt="爱心">
        <h1 id="question">愿不愿意做爸爸的小狗？</h1>
        <div class="buttons">
            <button id="yes">爸爸</button>
            <button id="no">不愿意！</button>
        </div>
    </div>

    <script>
        let yesButton = document.getElementById("yes");
        let noButton = document.getElementById("no");
        let questionText = document.getElementById("question");
        let mainImage = document.getElementById("mainImage");
        let clickCount = 0;

        const noTexts = [
            "？你认真的吗…", 
            "要不再想想？", 
            "不许选这个！", 
            "我会很伤心…", 
            "不行:("
        ];
        const imagePaths = [
            "https://zhengdef.github.io/xg/images/001.png",
            "https://zhengdef.github.io/xg/images/003.png",
            "https://zhengdef.github.io/xg/images/002.png",
            "https://zhengdef.github.io/xg/images/002.png",
            "https://zhengdef.github.io/xg/images/004.png"
        ];

        noButton.addEventListener("click", function() {
            clickCount++;
            let yesSize = 1 + (clickCount * 1.2);
            yesButton.style.transform = `scale(${yesSize})`;
            let noOffset = clickCount * 50;
            noButton.style.transform = `translateX(${noOffset}px)`;
            let moveUp = clickCount * 25;
            mainImage.style.transform = `translateY(-${moveUp}px)`;
            questionText.style.transform = `translateY(-${moveUp}px)`;

            if (clickCount <= 5) {
                noButton.innerText = noTexts[clickCount - 1];
            }
            if (clickCount < 5) {
                mainImage.src = imagePaths[clickCount];
            } else {
                mainImage.src = imagePaths[4];
            }
        });

        yesButton.addEventListener("click", function() {
            document.body.innerHTML = `
                <div class="yes-screen">
                    <h1 class="yes-text">!!!喜欢你!! ( >᎑<)♡︎ᐝ</h1>
                    <img src="https://zhengdef.github.io/xg/images/hug.png" alt="拥抱" class="yes-image">
                </div>
            `;
            document.body.style.overflow = "hidden";
        });
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(debug=True)
