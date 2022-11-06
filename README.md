API-SpeedToText
## Cấu trúc thư mục

```bash
---API_S2T
|	|--- static
|	|	|---css
|	|	|	|---main.css
|	|	|---js
|	|	|	|---scripts.js
|	|	|---uploads
|	|---templates
|	|	|---index.html
|	|---api.zip
|	|---flask_app.py
|	|---model.py
```

## Câu lệnh thực thi

```bash
python .\flask_app.py
```

## Demo
https://user-images.githubusercontent.com/82708060/200175857-01e6e77b-9f91-44ff-8d41-870df247eba0.mp4


## Chức năng

Giống như mọi ứng dụng web Python được xấy dựng bằng Flask, thư mục gốc chứa chương trình hệ thống gồm 2 thư mục bắt buộc là static và templates chứa trang index.html cho phép người dùng tải file ghi âm. File flask_app.py là nơi khai báo các trang người dùng có thể truy cập được cũng như kết hợp với việc xử lý data đầu và và đầu ra để trả cho người dùng.

Khi người dùng truy cập hệ thống, chọn file âm thanh từ thư mục và ấn nút “Kết quả nhận dạng”. Hệ thống sẽ lưu dữ liệu file âm thanh tải lên trong thư mục static/uploads. File âm thanh sau đó đưa vào hàm preprocessing để tiền xử lý âm thanh. Sau khi tiến hành tiền xử lý văn bản, dữ liệu sẽ được đi qua model đã được training từ trước và trả về kết quả là một dãy các từ được chuyển đổi từ âm thanh thành văn bản
