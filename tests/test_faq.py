import allure
import pytest
from helper.data import FAQData
from pages.main_page import MainPage


class TestFAQ:

    @allure.title('Проверка количества вопросов FAQ')
    @allure.description('Проверяем, что на странице отображается 8 вопросов FAQ')
    def test_faq_questions_count(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        questions_count = main_page.get_faq_questions_count()
        assert questions_count == 8, f"Ожидаемый результат: 8 вопросов, фактический: {questions_count}"

    @allure.title('Проверка видимости раздела FAQ')
    @allure.description('Проверяем, что раздел "Вопросы о важном" отображается на странице')
    def test_faq_section_visible(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        assert main_page.is_faq_section_visible(), "Раздел FAQ не отображается"

    @pytest.mark.parametrize("question_index,expected_answer", 
                            [(i, FAQData.answers[i]) for i in range(8)],
                            ids=[f"question_{i}" for i in range(8)])
    @allure.title('Проверка ответов на вопросы FAQ')
    @allure.description('Проверяем, что при клике на каждый вопрос отображается соответствующий ответ')
    def test_faq_answers(self, driver, question_index, expected_answer):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        
        # Получаем текст ответа
        actual_answer = main_page.get_faq_answer_text(question_index)
        
        # Проверяем соответствие ожидаемого и фактического ответа
        assert actual_answer == expected_answer, \
            f"Ожидаемый результат: '{expected_answer}', фактический: '{actual_answer}'"