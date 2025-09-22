import allure
from pages.main_page import HeaderPage, MainPage
from pages.order_page import OrderPage
from helper.data import TestUsers


class TestLogos:

    @allure.title('Проверка редиректа по логотипу Самоката с главной страницы')
    @allure.description('Проверяем, что клик по логотипу Самоката возвращает на главную страницу')
    def test_scooter_logo_redirect_from_main_page(self, driver):
        header_page = HeaderPage(driver)
        main_page = MainPage(driver)
        
        # Запоминаем текущий URL
        initial_url = main_page.get_current_url()
        
        # Кликаем по логотипу Самоката
        header_page.click_scooter_logo()
        
        # Проверяем, что URL не изменился (остались на главной странице)
        current_url = main_page.get_current_url()
        assert current_url == initial_url, f"URL изменился после клика по логотипу Самоката: {current_url}"

    @allure.title('Проверка редиректа по логотипу Яндекса')
    @allure.description('Проверяем, что клик по логотипу Яндекса открывает новую вкладку с Дзеном')
    def test_yandex_logo_redirect(self, driver):
        header_page = HeaderPage(driver)
        main_page = MainPage(driver)
        
        # Запоминаем количество окон до клика
        initial_windows_count = main_page.get_windows_count()
        
        # Кликаем по логотипу Яндекса
        header_page.click_yandex_logo()
        
        # Ждем открытия новой вкладки
        main_page.wait_for_new_window(initial_windows_count)
        
        # Проверяем, что открылась новая вкладка
        new_windows_count = main_page.get_windows_count()
        assert new_windows_count > initial_windows_count, "Новая вкладка не открылась"
        
        # Переключаемся на новую вкладку
        header_page.switch_to_new_tab(initial_windows_count)
        
        # Ждем загрузки страницы в новой вкладке
        main_page.wait_for_page_ready(10)
        
        # Дополнительно ждем, пока URL изменится с about:blank
        main_page.wait_for_url_change_from_about_blank(10)
        
        # Проверяем URL новой вкладки
        current_url = main_page.get_current_url()
        assert "dzen.ru" in current_url, \
            f"Новая вкладка не содержит ожидаемый URL: {current_url}"
        
        # Проверяем заголовок страницы
        # Ждем загрузки заголовка страницы
        main_page.wait_for_page_title_loaded()
        page_title = main_page.get_page_title()
        assert "Дзен" in page_title or "Яндекс" in page_title or "Yandex" in page_title, \
            f"Заголовок страницы не содержит ожидаемый текст: {page_title}"

    @allure.title('Проверка редиректа по логотипу Самоката со страницы заказа')
    @allure.description('Проверяем, что клик по логотипу Самоката со страницы заказа возвращает на главную страницу')
    def test_scooter_logo_redirect_from_order_page(self, driver):
        header_page = HeaderPage(driver)
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        # Переходим на страницу заказа
        main_page.scroll_and_click_order_button()
        
        # Кликаем по логотипу Самоката со страницы заказа
        header_page.click_scooter_logo()
        
        # Проверяем, что вернулись на главную страницу
        current_url = main_page.get_current_url()
        assert "order" not in current_url, f"Не вернулись на главную страницу: {current_url}"

    @allure.title('Проверка атрибутов логотипов')
    @allure.description('Проверяем корректность атрибутов логотипов')
    def test_logos_attributes(self, driver):
        header_page = HeaderPage(driver)
        main_page = MainPage(driver)
        
        # Проверяем, что логотипы являются ссылками
        assert header_page.is_logo_link('scooter'), "Логотип Самоката не является ссылкой"
        assert header_page.is_logo_link('yandex'), "Логотип Яндекса не является ссылкой"
        
        # Проверяем target="_blank" для логотипа Яндекса
        yandex_target = header_page.get_logo_target('yandex')
        assert yandex_target == '_blank', f"Логотип Яндекса не имеет target='_blank': {yandex_target}"
        
        # Проверяем href атрибуты
        scooter_href = header_page.get_logo_href('scooter')
        yandex_href = header_page.get_logo_href('yandex')
        
        assert scooter_href is not None, "Логотип Самоката не имеет href атрибута"
        assert yandex_href is not None, "Логотип Яндекса не имеет href атрибута"