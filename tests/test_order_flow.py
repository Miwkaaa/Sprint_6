import allure
from helper.data import TestUsers
from pages.main_page import MainPage, HeaderPage
from pages.order_page import OrderPage


class TestOrderFlow:

    @allure.title('Позитивный тест оформления заказа через кнопку "Заказать" в хедере')
    @allure.description('''
                        1) На главной странице в хедере кликаем на кнопку "Заказать";
                        2) Заполняем данные на странице "Для кого самокат" и кликаем на кнопку "Далее";
                        3) Заполняем данные "Про аренду" и кликаем на кнопку "Заказать";
                        4) Подтверждаем заказ и проверяем открытие окна с текстом оформления заказа''')
    def test_order_scooter_from_header(self, driver):
        header_page = HeaderPage(driver)
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        
        # Кликаем на кнопку заказа в хедере
        header_page.click_order_button()
        
        # Выполняем полный процесс заказа
        order_page.order_scooter_full_path(TestUsers.user_1)
        
        # Проверяем успешное оформление заказа
        assert order_page.check_order_title(), "Окно подтверждения заказа не отображается"

    @allure.title('Позитивный тест оформления заказа через кнопку "Заказать" на главной странице')
    @allure.description('''
                        1) На главной странице скроллим до кнопки "Заказать" и кликаем на нее;
                        2) Заполняем данные на странице "Для кого самокат" и кликаем на кнопку "Далее";
                        3) Заполняем данные "Про аренду" и кликаем на кнопку "Заказать";
                        4) Подтверждаем заказ и проверяем открытие окна с текстом оформления заказа''')
    def test_order_scooter_from_main_page(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        # Скроллим и кликаем на кнопку заказа на главной странице
        main_page.scroll_and_click_order_button()
        
        # Выполняем полный процесс заказа с другим пользователем
        order_page.order_scooter_full_path(TestUsers.user_2)
        
        # Проверяем успешное оформление заказа
        assert order_page.check_order_title(), "Окно подтверждения заказа не отображается"