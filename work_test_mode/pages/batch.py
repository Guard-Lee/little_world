# 处理 iframe 内的业务逻辑

from playwright.sync_api import Page, expect

class BatchPage:
    def __init__(self, page: Page):
        self.page = page
        self.frame = page.frame_locator("iframe[title='content']")

    # ========== 凭证批次相关的动作 ==========
    def create_batch(self, name: str, count: str):
        self.frame.get_by_role("button", name="新建批次").click()
        self.frame.get_by_role("textbox", name="如：东莞一厂·8月首批").fill(name)
        # 注意：nth(3) 和 nth(4) 很不稳定，这里原样保留，建议以后改用 label 定位
        self.frame.get_by_role("combobox").nth(3).select_option("室内云台 Y2（b2n8q4w6y1）")
        self.frame.get_by_role("spinbutton").fill(count)
        self.frame.get_by_role("combobox").nth(4).select_option("WebAPI + 离线")
        self.frame.get_by_role("button", name="创建并签发").click()

    # def verify_batch_created(self, name: str):
    #     """断言：表格里出现了刚刚创建的批次名称"""
    #     # 方法一：直接找表格单元格 (适合文本完全匹配)
    #     expect(self.frame.get_by_role("cell", name=name, exact=True)).to_be_visible()
        
    # def verify_batch_created(self, name: str, device_name: str):
    #     """高级断言：找到这一行，并验证这一行的设备名称是不是对的"""
    #     # 1. 找到包含批次名称的那一行 (假设 html 是 <tr>)
    #     target_row = self.frame.locator("tr", has_text=name)
        
    #     # 2. 断言这行里，确实包含了正确的设备名称
    #     expect(target_row).to_contain_text(device_name)
    #     expect(target_row).to_contain_text("WebAPI") # 验证接口类型对不对
    
    def verify_batch_created(self, name: str, device_name: str = None):
        """断言：表格里出现了刚刚创建的批次名称"""
        # 方案 A：只要出现这个名字的单元格，就代表成功
        expect(self.frame.get_by_role("cell", name=name, exact=True)).to_be_visible()
        
        # 方案 B（更高级）：如果你的设备名也是以 Cell 形式展现的，可以一起验证
        if device_name:
            expect(self.frame.get_by_role("cell", name=device_name).first).to_be_visible()

    def click_buy_authorization(self):
        """点击去采购，以及关闭弹窗"""
        self.frame.get_by_text("去采购 →").click()
        self.frame.get_by_role("button", name="采购授权").click()
        self.frame.get_by_role("button", name="×").click()

    

    # ========== 新窗口（弹窗）处理 ==========
    def open_device_auth_guide(self):
        """点击设备授权说明，并进入新标签页"""
        with self.page.expect_popup() as popup_info:
            self.frame.get_by_role("button", name="设备授权说明").click()
        
        new_page = popup_info.value
        # 断言：新窗口打开成功
        expect(new_page.get_by_role("button", name="关闭窗口")).to_be_visible()
        new_page.get_by_role("button", name="关闭窗口").click()
        new_page.close()