from playwright.sync_api import Page, expect

class RegisterPage:
    
    URL = "https://zhaizhitong.com/official.html" 
    
    def __init__(self, page: Page):
        # 定位
        self.page = page
        self.dev_platform_btn = page.locator("#navPrimary")
        self.phone_input = page.get_by_role("textbox", name="请输入手机号或邮箱地址")
        self.verify_code_get=page.get_by_role("button", name="获取验证码")
        self.verify_code_input = page.get_by_role("textbox", name="位验证码")
        self.password_input=page.get_by_role("textbox", name="–20 位密码")
        self.password_reinput=page.get_by_role("textbox", name="请再次输入密码")
        self.register_btn=page.get_by_role("button", name="注册并进入开发者平台")
        # 用于断言
        self.user_avatar = page.get_by_text("个", exact=True).first
        self.account_auth_btn = page.get_by_role("button", name="账号与资质")
        
    def goto(self):
        self.page.goto(self.URL)

    def register(self, phone: str, verify_code: str, password: str):
        self.dev_platform_btn.click()
        self.phone_input.click()
        self.phone_input.fill(phone)
        self.verify_code_get.click()
        self.verify_code_input.click()
        self.verify_code_input.fill(verify_code)
        self.password_input.click()
        self.password_input.fill(password)
        self.password_reinput.click()
        self.password_reinput.fill(password)
        self.register_btn.click()

    def verify_register_success(self):
        # 注册后，右上角应该出现“个”
        expect(self.page.get_by_text("个", exact=True).first).to_be_visible()