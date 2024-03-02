import openai
from apht import AdvancedPromptHackingTester, MockAISystem

# تنظیم کردن کلید دسترسی به OpenAI
api_key = 'YOUR_OPENAI_API_KEY'
openai.api_key = api_key

# تابع برای ارسال درخواست به وب سرویس OpenAI و دریافت پاسخ
def send_prompt_to_openai(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()

# تست ارتباط با وب سرویس OpenAI و دریافت پاسخ
def test_openai_api():
    prompt = "Once upon a time,"
    response = send_prompt_to_openai(prompt)
    print("پاسخ دریافتی از OpenAI:", response)

# تست ارتباط با ChatGPT
def test_chatgpt_api():
    ai_system = MockAISystem()
    advanced_prompt_hacking_tester = AdvancedPromptHackingTester(ai_system)
    advanced_prompt_hacking_tester.run_tests(10, save_results=True)

if __name__ == "__main__":
    test_openai_api()
    test_chatgpt_api
