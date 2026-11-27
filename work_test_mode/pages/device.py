from playwright.sync_api import Page, expect
from pages.batch import BatchPage


class DevicePage:
    def __init__(self, page):
        self.page = page
        self.frame = page.frame_locator("iframe[title='content']")

# 在 DevicePage 类中补上这个方法
    def open_device_auth_guide(self):
        """点击设备授权说明，并进入新标签页"""
        with self.page.expect_popup() as popup_info:
            self.frame.get_by_role("button", name="设备授权说明").click()
        
        new_page = popup_info.value
        expect(new_page.get_by_role("button", name="关闭窗口")).to_be_visible()
        new_page.get_by_role("button", name="关闭窗口").click()
        new_page.close()
        
        # ========== 设备台账相关的动作 ==========
    def restore_factory_settings(self):
        """设备恢复出厂设置（点击取消）"""
        self.frame.get_by_text("详情").first.click()
        self.frame.get_by_role("button", name="恢复出厂").click()
        self.frame.get_by_role("button", name="取消").click()
        self.frame.get_by_role("button", name="×").click()