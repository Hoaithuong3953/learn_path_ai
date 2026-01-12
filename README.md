# LearnPath Chatbot

## 1. Mô tả ngắn
LearnPath chatbot là một chatbot backend sử dụng LLM, phục vụ cho việc xử lý hội thoại và sinh nội dung dựa trên đầu vào dạng text.

Hiện tại, dự án tập trung vào việc triển khai các thành phần cốt lõi của backend và luồng xử lý hội thoại, bao gồm:
- Tổ chức module rõ ràng
- Luồng xử lý hội thoại chính
- Tích hợp LLM thật với cơ chế streaming
- Logging, cấu hình và xử lý lỗi theo hướng production
---

## 2. Phạm vi hiện tại của dự án
- Core logic xử lý hội thoại
- Kết nối trực tiếp tới Google Gemini API
- Cơ chế streaming response
- Hệ thống logging và error handling
- Quản lý cấu hình thông qua biến môi trường

---

## 3. Cấu trúc thư mục
learnpath_chatbot/
- ai/ — LLM client và xử lý tương tác với Gemini
- config/ — Cấu hình ứng dụng
- domain/ — Domain models
- memory/ — Quản lý trạng thái / lịch sử hội thoại
- services/ — Business logic cho luồng xử lý hiện tại
- utils/ — Logging, exceptions, helpers
- requirements.txt
- app.py — Entry point (đang phát triển)

---

## 4. Luồng xử lý chính
1. Nhận input dạng text
2. Service layer tiếp nhận và xử lý nghiệp vụ
3. Gửi request tới LLM thông qua client
4. Nhận phản hồi streaming từ LLM
5. Trả kết quả về cho tầng gọi

Luồng xử lý sử dụng **code thật**, không mock response.

---

## 5. Yêu cầu môi trường
- Python >= 3.9
- Google Gemini API Key

---

## 6. Cài đặt
git clone https://github.com/Hoaithuong3953/learn_path_ai.git
cd learnpath_chatbot
pip install -r requirements.txt

---

## 7. Cấu hình môi trường
Tạo file `.env`:

GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-2.5-flash
LOG_LEVEL=INFO
---

## 8. Chạy dự án
Tính năng này đang được phát triển (file `app.py` chưa sẵn sàng).
Sau khi hoàn thiện, dự án sẽ chạy thông qua:
- python app.py
- hoặc streamlit run app.py

---

## 9. Logging & Error Handling
- Logging được cấu hình trong `utils/logger.py`
- Hỗ trợ ghi log ra console và file
- Có cơ chế xoay vòng file log
- Các lỗi nghiệp vụ và lỗi LLM được chuẩn hóa thông qua custom exception