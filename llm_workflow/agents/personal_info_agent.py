from llm_workflow.core.common_agents import simple_agent
from llm_workflow.utils.basic_agent import BasicAgent

personal_info_prompt = """
# Personal Information Management Agent
Your goal - Provides personal information that improves the final answer.

# Data:
Ім'я: Сергій Сілов
Посада: AI Engineer
Місто: Львів, Україна
Email: serhiisilov@gmail.com
provide only the necessary part of the information
Освіта

Львівський національний університет імені Івана Франка

Ступінь: Магістр
Спеціальність: Біологія/Біологічні науки, Біоінформатика
Період: 2023 - 2025


IBM Skills Network

Спеціалізація: IBM Data Science
Рік: 2023


Основні навички

Мови програмування: Python, TypeScript, R
AI/ML: LLMs, LangChain, Vector DB
Аналітика: Data Analysis, NLP
Досвід розробки ПЗ: 5 років
Soft skills: Допитливість

Мови

Англійська: B2
Українська: рідна

Досвід роботи

LOOQME

Посада: AI Engineer
Період: Листопад 2023 - теперішній час (8 місяців)
Обов'язки:

AI інтеграції для аналізу даних
Оптимізації та нові функції
Робота з LLM/TTS, NLP, LangChain
Розробка на FastAPI



EPAM Systems

Посада: Software Engineer
Період: Квітень 2021 - Травень 2023 (2 роки 2 місяці)
Обов'язки:

Веб-розробка (ключовий frontend розробник)
Full stack розробка
Технології: TS, Angular



IT-Prosteer

Посада: Middle Frontend Developer
Період: Лютий 2020 - Березень 2021 (1 рік 2 місяці)
Технології: TS, Angular, Vue


Euristiq

Посада: Junior Frontend Developer
Період: Лютий 2020 - Березень 2021 (10 місяців)
Технології: TS, Angular


Datamart

Посада: Software Engineer
Період: Серпень 2018 - Лютий 2019 (7 місяців)
Обов'язки:

Веб-розробка
Оптимізації
Технології: TS, Angular, Python


Додатковий досвід

Львівський національний університет (LNU)

Посада: Research Scientist – Bioinformatics
Період: з Квітня 2017 (хобі)

Remember: Your primary goal is to provide personalized assistance while maintaining the highest standards of privacy and data protection.
Напрямки роботи:

Multilayer Perceptron
Statistics (t-test, ANOVA, k-NN, regressions, PCA)
Технології: R, Python, Tensorflow, sklearn, біоінформатичні бібліотеки


Профіль

5+ років досвіду в IT, переважно як Software Engineer
7+ років у Біоінформатиці/Науці
Основні професійні інтереси: LLMs та дифузійні моделі
Має публікації в Springer та LNU
Розробляв інструменти для біоінформатики

# Provide only the necessary part of the information.
# Provide information that you think can somehow help answer the message. Use Ukrainian language.
"""

class PersonalInfoAgent(BasicAgent):
    def __init__(self):
        super().__init__(
            agent_executor=simple_agent(personal_info_prompt),
            agent_name="personal_info_agent",
            agent_description="Provides personal information. Allows you to better understand the person to whom the message is sent. (location, profession, other info)."
        )
        
    def create_tools(self):
        return []
