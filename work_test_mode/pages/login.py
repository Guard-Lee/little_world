# 登录和退出

from playwright.sync_api import Page, expect

class LoginPage:
    
    URL = "https://zhaizhitong.com/official.html" 
    
    def __init__(self, page: Page):
        self.page = page
        # 去掉了冗余的 click，提取干净的定位器
        self.dev_platform_btn = page.get_by_role("button", name="开发者平台", exact=True)
        self.select_account_btn = page.get_by_role("button", name="选择账号")
        self.account_btn = page.get_by_role("button", name="张工 13866886688 拥有者")
        self.login_btn = page.get_by_role("button", name="登录")

    def goto(self):
        self.page.goto(self.URL)

    def login(self):
        self.dev_platform_btn.click()
        self.select_account_btn.click()
        self.account_btn.click()
        self.login_btn.click()

    def verify_login_success(self):
        # 登录后，右上角应该出现“张”
        expect(self.page.get_by_text("张", exact=True).first).to_be_visible()

    def logout(self):
        # 录制的：点击头像 -> 退出登录
        self.page.get_by_text("张", exact=True).first.click()
        self.page.get_by_role("button", name="退出登录").click()