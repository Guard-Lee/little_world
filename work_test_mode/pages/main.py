from playwright.sync_api import Page, expect
from pages.batch import BatchPage
from pages.device import DevicePage


# 处理外层壳子、菜单和语言

class MainPage:
    def __init__(self, page: Page):
        self.page = page
        # 统一管理 iframe 对讲机
        self.frame = page.frame_locator("iframe[title='content']")

    def switch_language(self, lang_code):
        """切换语言：en 或 zh-CN"""
        self.page.get_by_label("语言").select_option(lang_code)

    def navigate_to_batch(self) -> "BatchPage":
        # 录制时的 dblclick 是不必要的，单击即可
        self.page.get_by_text("凭证批次").click()
        return BatchPage(self.page)

    def navigate_to_device_ledger(self) -> "DevicePage":
        self.page.get_by_text("设备台账").click()
        return DevicePage(self.page)
    
    