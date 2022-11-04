from flask import Flask, request, render_template
from flask_cors import CORS
from preprocessing_audio import preprocessing

app = Flask(__name__, static_url_path="/static", static_folder='./static')
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def predic_upload():
    print('upload file')
    if request.method == 'POST':
        _file = request.files['file']
        if _file.filename == '':
            return render_template('index.html', predict="", error="File không hợp lệ")
        
        # Lưu file vừa tải lên
        print('\n\nfile uploaded:',_file.filename)
        _file.save('./static/upload/' + _file.filename)
        print('Write file success!')

        # Audio preprocessing
        audio_path='./static/upload/' + _file.filename
        # Hàm preprocessing trả về một set(danh sách các đường dẫn file được tách file/30s)
        audios = preprocessing("./static/upload/", audio_path)
        # print(audio_paths)

        # model dự đoán
        predict = "Nguyen Thi Ngoc Huyen"

    return render_template('index.html', predict=predict, audio_path=audio_path)


if __name__ == "__main__":
    app.run(debug=True)