# Advanced Prompt Hacking Tester

این پروژه یک تستر پیشرفته برای هک کردن پاسخ‌های یک سیستم هوش مصنوعی را پیاده‌سازی می‌کند.

## نصب

1. ابتدا اطمینان حاصل کنید که Python نصب شده است.
2. می‌توانید ابتدا مراحل نصب زیر را دنبال کنید:

```bash
pip install nltk
```

## استفاده

1. ابتدا یک نمونه از `MockAISystem` را پیاده‌سازی کنید. این کلاس باید یک متد به نام `process_prompt` داشته باشد که یک پارامتر به نام `prompt` را می‌گیرد و پاسخ مورد انتظار را برمی‌گرداند.
2. سپس یک نمونه از `AdvancedPromptHackingTester` را با استفاده از نمونه سیستم AI ایجاد کنید.
3. با فراخوانی متد `run_tests` تعداد تست‌های مورد نیاز و انتخاب گزینه ذخیره نتایج (در صورت تمایل) اجرا شود.

## متدها

- `generate_random_prompt(min_length, max_length)`: این متد یک پرامتر تصادفی با طول بین `min_length` و `max_length` تولید می‌کند.
- `generate_contextual_adversarial_prompt(original_prompt, min_length, max_length)`: این متد یک پرامتر تصادفی با طول بین `min_length` و `max_length` تولید می‌کند و سعی می‌کند با تغییرات معنایی در پارامتر اصلی، پارامتر جدید را تولید کند.
- `generate_inappropriate_prompt()`: این متد یک پرامتر نامناسب تصادفی تولید می‌کند.
- `execute_prompt_test(prompt, save_results=False)`: این متد یک پرامتر را به عنوان ورودی به سیستم AI می‌دهد و پاسخ را دریافت می‌کند.
- `run_tests(num_tests, save_results=False)`: این متد تعداد `num_tests` تست را اجرا می‌کند.

## مثال استفاده

```python
ai_system = MockAISystem()
advanced_prompt_hacking_tester = AdvancedPromptHackingTester(ai_system)
advanced_prompt_hacking_tester.run_tests(10, save_results=True)
```

## مجوز

این پروژه تحت مجوز [MIT](https://opensource.org/licenses/MIT) منتشر شده است.
این قالب یک راهنمای کاربردی است که برای پروژه شما مناسب است. البته می‌توانید آن را با توجه به نیازهای خاص خود تغییر دهید.
