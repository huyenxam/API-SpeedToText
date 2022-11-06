from flask import Flask, request, render_template
from flask_cors import CORS
from preprocessing_audio import preprocessing
from time import sleep

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
        predict = "dạ mobifone xin nghe em là minh anh có thể giúp được gì cho anh chị ạ chị kiểm tra giùm em cái số điện thoại này gọi lên đó em mới cài ba g d mười á mà không hoạt động nó không chạy được luôn á chị dạ vâng rất xin lỗi về sự bất tiện này cho em xin anh tên gì để em tiện xưng hô được không ạ dạ em tên minh dạ em chào anh minh số anh minh đây em kiểm tra là đúng là có đăng ký gói cước d mười cho mở thiết bị di động máy hiện ba g bốn g hay kiểu gì vậy anh minh dạ chữ h chị dạ vâng mình sẽ hỗ trợ đóng nối mở nối lại đường truyền truy cập mạng cho sim của anh minh lại kết thúc cuộc gọi này anh thông cảm tắt nguồn máy hai phút sau anh mở nguồn nên bật lại dùng lại thử xem được chưa nha được rồi ok em cám ơn dạ mình cần hỗ trợ thông tin"
        sleep(1.5)
    return render_template('index.html', predict=predict, audio_path=audio_path)


if __name__ == "__main__":
    app.run(debug=True)