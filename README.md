# AI Unit Test Assistant 🤖

Một trợ lý AI mạnh mẽ dùng OpenAI API để xử lý, tạo, phân tích và tối ưu hóa Unit Test.

## ✨ Tính năng chính

- **T���o Unit Test**: Tự động tạo unit test từ code
- **Phân tích Test**: Kiểm tra chất lượng test, coverage
- **Tối ưu Test**: Đề xuất cải thiện test cases
- **Debug Test**: Giúp fix các test fail
- **Báo cáo**: Tạo báo cáo chi tiết về test

## 📋 Yêu cầu

- Python 3.8+
- OpenAI API Key
- pip package manager

## 🚀 Cài đặt

### 1. Clone Repository
```bash
git clone https://github.com/chiduc544-cpu/ai-unit-test-assistant.git
cd ai-unit-test-assistant
```

### 2. Tạo Virtual Environment
```bash
python -m venv venv

# Trên Windows
venv\Scripts\activate

# Trên macOS/Linux
source venv/bin/activate
```

### 3. Cài đặt Dependencies
```bash
pip install -r requirements.txt
```

### 4. Cấu hình Environment
```bash
# Copy file example
cp .env.example .env

# Chỉnh sửa .env và thêm OpenAI API Key
nano .env
```

## 📖 Cách sử dụng

### 1. Tạo Unit Test từ Function
```python
from src.ai_assistant import AITestAssistant

assistant = AITestAssistant()

code = """
def add(a, b):
    return a + b
"""

result = assistant.generate_tests(code)
print(result)
```

### 2. Phân tích Test Hiện tại
```python
assistant.analyze_tests(test_code)
```

### 3. Tối ưu hóa Test
```python
suggestions = assistant.optimize_tests(test_code)
```

### 4. Debug Test Fail
```python
debug_result = assistant.debug_test(failed_test, error_message)
```

### 5. Chat Mode
```bash
python src/main.py
```

## 📁 Cấu trúc Dự án

```
ai-unit-test-assistant/
├── .env.example              # Ví dụ environment variables
├── .gitignore               # Git ignore rules
├── README.md                # Documentation
├── requirements.txt         # Python dependencies
├── config/
│   └── settings.py          # Configuration settings
├── src/
│   ├── __init__.py
│   ├── main.py              # Entry point (CLI/Chat)
│   ├── ai_assistant.py      # Main AI Assistant class
│   ├── test_processor.py    # Unit test processing logic
│   └── api_handler.py       # OpenAI API handler
└── tests/
    ├── __init__.py
    ├── test_assistant.py    # Tests for AI Assistant
    └── test_processor.py    # Tests for Test Processor
```

## 🔧 Các Command

```bash
# Chạy ứng dụng
python src/main.py

# Chạy tests
pytest

# Chạy tests với coverage
pytest --cov=src

# Chạy tests với output chi tiết
pytest -v
```

## 💡 Ví dụ sử dụng

### Ví dụ 1: Tạo Unit Test
```python
from src.ai_assistant import AITestAssistant

assistant = AITestAssistant()

code = """
def calculate_discount(price, discount_percent):
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount must be between 0 and 100")
    return price * (1 - discount_percent / 100)
"""

tests = assistant.generate_tests(code)
print("Generated Tests:")
print(tests)
```

### Ví dụ 2: Phân tích Test Coverage
```python
assistant.analyze_tests(test_code)
```

## 🔐 Security

- Không commit `.env` file (đã có trong `.gitignore`)
- Giữ OpenAI API key an toàn
- Không share API key công khai

## 📝 Logs

Logs được lưu trong thư mục `logs/` với format:
- `app.log` - General logs
- `error.log` - Error logs

## 🐛 Troubleshooting

### Lỗi: "API key not found"
- Kiểm tra file `.env` có chứa `OPENAI_API_KEY` không
- Chắc chắn key hợp lệ

### Lỗi: "Module not found"
```bash
pip install -r requirements.txt
```

### Lỗi: "OpenAI API Error"
- Kiểm tra kết nối internet
- Kiểm tra API key hợp lệ
- Kiểm tra quota OpenAI

## 📚 API Reference

### AITestAssistant

#### `generate_tests(code: str) -> str`
Tạo unit test từ đoạn code

#### `analyze_tests(test_code: str) -> dict`
Phân tích quality và coverage của test

#### `optimize_tests(test_code: str) -> list`
Đề xuất cải thiện test

#### `debug_test(test_code: str, error: str) -> str`
Giúp fix test fail

## 🤝 Đóng góp

Mọi đóng góp đều được chào đón! Hãy:

1. Fork repository
2. Tạo branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📄 License

MIT License - xem file LICENSE để chi tiết

## 📧 Contact

- GitHub: [@chiduc544-cpu](https://github.com/chiduc544-cpu)
- Email: your_email@example.com

## 🙏 Acknowledgments

- OpenAI API documentation
- pytest framework
- Python community

---

**Made with ❤️ by chiduc544-cpu**
