# Webhook Tự Động Trả Lời Tin Nhắn cho BotBanHang + GPT-4

## Bước 1: Cài thư viện
```bash
pip install flask openai python-dotenv
```

## Bước 2: Tạo file .env chứa API key
```env
OPENAI_API_KEY=your_openai_api_key_here
```

## Bước 3: Chạy server
```bash
python app.py
```

## Bước 4: Deploy lên Render.com
- Tạo project mới
- Upload file `app.py` và `.env`
- Đặt đường dẫn `/webhook`
- Lấy link public, gắn vào phần "Webhook URL" trên botbanhang.vn

## Bước 5: Trong BotBanHang
- Vào kịch bản hội thoại
- Thêm "Gửi webhook"
- Bot sẽ tự động gửi nội dung người dùng → GPT → nhận lại trả lời

