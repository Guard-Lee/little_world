import pytest
from playwright.sync_api import Page
from pages.login import LoginPage
from pages.main import MainPage
import allure
import os

# 全局准备工作

@pytest.fixture
def zhaizhitong_app(page: Page):
    """前置条件：登录宅智通并进入主页"""
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login()
    login_page.verify_login_success()
    
    # 返回主页对象，后续用例直接操作
    return MainPage(page)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """全局的 Hook：无论用例用了哪个 page，只要在 call 阶段失败，就自动挂载附件。"""
    outcome = yield
    report = outcome.get_result()

    # 只在执行阶段 (call) 且失败时触发
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            # 1. 失败截图
            try:
                screenshot = page.screenshot()
                if screenshot:
                    allure.attach(screenshot, name="失败截图", attachment_type=allure.attachment_type.PNG)
            except Exception:
                pass

            # 2. 失败录屏
            video_path = None
            try:
                if page.video:
                    video_path = page.video.path()
            except Exception:
                pass

            # 关闭页面，触发 Playwright 写入视频
            try:
                page.close()
            except Exception:
                pass

            # 等待视频生成
            if video_path:
                for _ in range(20):
                    if os.path.exists(video_path) and os.path.getsize(video_path) > 0:
                        break
                    time.sleep(0.1)

                if os.path.exists(video_path) and os.path.getsize(video_path) > 0:
                    allure.attach.file(video_path, name="失败录屏", attachment_type=allure.attachment_type.WEBM)
