import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://zhaizhitong.com/official.html")
    page.get_by_role("link", name="了解平台能力").click()
    page.get_by_role("button", name="开发者平台", exact=True).click()
    page.get_by_role("button", name="选择账号").click()
    page.get_by_role("button", name="张工 13866886688 企业开发者").click()
    page.get_by_role("button", name="登录").click()
    page.get_by_text("张", exact=True).first.click()
    page.get_by_role("button", name="退出登录").click()
    page.get_by_role("button", name="开发者平台", exact=True).click()
    page.locator("#loginModal").get_by_role("link", name="免费注册").click()
    page.get_by_role("textbox", name="请输入手机号或邮箱地址").click()
    page.get_by_role("button", name="关闭").click()
    page.get_by_role("button", name="开发者平台", exact=True).click()
    page.get_by_text("手机号 / 邮箱 * 选择账号").click()
    page.get_by_role("button", name="选择账号").click()
    page.get_by_role("button", name="张工 13866886688 企业开发者").click()
    page.get_by_role("button", name="登录").click()
    page.get_by_label("语言").select_option("en")
    page.get_by_label("语言").select_option("zh-CN")
    page.get_by_text("凭证批次").dblclick()
    page.locator('iframe[title="content"]').content_frame.get_by_role(
        "button", name="新建批次"
    ).click()
    page.locator('iframe[title="content"]').content_frame.get_by_role(
        "textbox", name="如：东莞一厂·8月首批"
    ).click()
    page.locator('iframe[title="content"]').content_frame.get_by_role(
        "textbox", name="如：东莞一厂·8月首批"
    ).fill("test")
    page.locator('iframe[title="content"]').content_frame.get_by_role("combobox").nth(
        3
    ).select_option("室内云台 Y2（b2n8q4w6y1）")
    page.locator('iframe[title="content"]').content_frame.get_by_role(
        "spinbutton"
    ).click()
    page.locator('iframe[title="content"]').content_frame.get_by_role(
        "spinbutton"
    ).fill("200")
    page.locator('iframe[title="content"]').content_frame.get_by_role("combobox").nth(
        4
    ).select_option("WebAPI + 离线")
    page.locator('iframe[title="content"]').content_frame.get_by_role(
        "button", name="创建并签发"
    ).click()
    page.locator('iframe[title="content"]').content_frame.get_by_role(
        "button", name="查询"
    ).click()
    page.locator('iframe[title="content"]').content_frame.get_by_text(
        "去采购 →"
    ).click()
    page.locator('iframe[title="content"]').content_frame.get_by_role(
        "button", name="采购授权"
    ).click()
    page.locator('iframe[title="content"]').content_frame.get_by_role(
        "button", name="×"
    ).click()
    page.get_by_text("设备台账").click()
    page.locator('iframe[title="content"]').content_frame.get_by_text(
        "详情"
    ).first.click()
    page.locator('iframe[title="content"]').content_frame.get_by_role(
        "button", name="恢复出厂"
    ).click()
    page.locator('iframe[title="content"]').content_frame.get_by_role(
        "button", name="取消"
    ).click()
    page.locator('iframe[title="content"]').content_frame.get_by_role(
        "button", name="×"
    ).click()
    page.locator('iframe[title="content"]').content_frame.get_by_text(
        "恢复", exact=True
    ).click()
    page.locator('iframe[title="content"]').content_frame.get_by_text(
        "详情"
    ).first.click()
    page.locator('iframe[title="content"]').content_frame.get_by_role(
        "button", name="×"
    ).click()
    with page.expect_popup() as page1_info:
        page.locator('iframe[title="content"]').content_frame.get_by_role(
            "button", name="设备授权说明"
        ).click()
    page1 = page1_info.value
    page1.get_by_role("button", name="关闭窗口").click()
    page1.close()

    page.wait_for_timeout(3000)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
