# Setup Guide - AI Unit Test Assistant

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git
- OpenAI API key

## Step-by-Step Installation

### 1. Clone the Repository

```bash
git clone https://github.com/chiduc544-cpu/ai-unit-test-assistant.git
cd ai-unit-test-assistant
```

### 2. Create Virtual Environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Get OpenAI API Key

1. Go to [OpenAI Platform](https://platform.openai.com)
2. Sign up or log in to your account
3. Go to API keys section
4. Create a new API key
5. Copy the key (save it safely)

### 5. Configure Environment Variables

```bash
# Copy the example file
cp .env.example .env

# Edit .env with your API key
# On Windows:
type .env
# On macOS/Linux:
cat .env

# Add your OpenAI API key:
# OPENAI_API_KEY=sk-your_actual_key_here
```

### 6. Verify Installation

```bash
# Test if everything is working
python -c "from src.ai_assistant import AITestAssistant; print('Installation successful!')"
```

## Running the Application

### Interactive CLI Mode

```bash
python src/main.py
```

This opens an interactive prompt where you can use commands like:

```
>> generate def add(a, b): return a + b
>> help
>> exit
```

### Running Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run with coverage report
pytest --cov=src

# Run specific test file
pytest tests/test_assistant.py
```

## Project Structure

```
ai-unit-test-assistant/
├── config/
│   └── settings.py              # Configuration management
├── src/
│   ├── main.py                  # CLI entry point
│   ├── ai_assistant.py          # Main AI assistant class
│   ├── test_processor.py        # Test processing logic
│   └── api_handler.py           # OpenAI API handler
├── tests/
│   ├── test_assistant.py        # Tests for assistant
│   └── test_processor.py        # Tests for processor
├── docs/
│   └── SETUP.md                 # This file
├── .env.example                 # Example environment file
├── .gitignore                   # Git ignore rules
├── README.md                    # Project documentation
└── requirements.txt             # Python dependencies
```

## Available Commands

### 1. Generate Unit Tests
```bash
generate def add(a, b): return a + b
```

### 2. Analyze Test Quality
```bash
analyze def test_add(): assert add(1, 1) == 2
```

### 3. Get Optimization Suggestions
```bash
optimize def test_add(): assert add(1, 1) == 2
```

### 4. Debug Failing Tests
```bash
debug def test_fail(): assert 1 == 2 ||| AssertionError: 1 != 2
```

### 5. Refactor Tests
```bash
refactor def test_x(): assert 1==1; assert 2==2
```

### 6. Estimate Coverage
```bash
coverage def add(a, b): return a + b ||| def test_add(): assert add(1, 1) == 2
```

### 7. Chat Mode
```bash
chat How do I write better unit tests?
```

## Troubleshooting

### "API key not found" Error

**Solution:**
- Ensure `.env` file exists in the project root
- Verify `OPENAI_API_KEY` is set in `.env`
- Check that API key is valid and not expired
- Ensure no extra spaces in the key

### "Module not found" Error

**Solution:**
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### "OpenAI API Error" Messages

**Solution:**
- Check internet connection
- Verify API key is valid
- Check OpenAI account quota
- View logs in `logs/` directory for details

### Virtual Environment Not Activating

**Windows Solution:**
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\activate
```

## Common Usage Examples

### Example 1: Generate Tests for a Function

```bash
>> generate def calculate_discount(price, discount): return price * (1 - discount/100)
```

### Example 2: Analyze Existing Tests

```bash
>> analyze def test_discount():
    assert calculate_discount(100, 10) == 90
    assert calculate_discount(100, 50) == 50
```

### Example 3: Get Help

```bash
>> help
```

### Example 4: Chat About Testing

```bash
>> chat What are the best practices for unit testing in Python?
```

## Performance Tips

1. **API Costs**: Each API call costs tokens. Long prompts use more tokens.
2. **Rate Limiting**: If you hit rate limits, wait before retrying.
3. **Token Limits**: Very long code snippets may exceed token limits.
4. **Batch Processing**: Process multiple tests separately to avoid token overflow.

## Getting Help

- **Documentation**: See README.md for full documentation
- **Issues**: Report bugs on GitHub Issues
- **OpenAI Docs**: Visit [OpenAI API Documentation](https://platform.openai.com/docs)

## Next Steps

1. Run `python src/main.py` to start using the assistant
2. Type `help` to see all available commands
3. Try generating tests with `generate`
4. Explore other features

## Security Notes

- ⚠️ Never commit `.env` file to version control
- 🔒 Keep your API key secret
- 🛡️ Regularly rotate your API keys
- 📝 Monitor API usage for unauthorized access

---

**Happy Testing! 🚀**
