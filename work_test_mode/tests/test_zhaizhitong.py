from pages.main import MainPage
from pages.register import RegisterPage
import allure

# 业务测试用例

@allure.title("创建凭证批次并去采购")
def test_create_batch_and_buy_auth(zhaizhitong_app: MainPage):
    """测试：创建凭证批次并去采购"""
    app = zhaizhitong_app

    # 1. 进入批次页面
    with allure.step("进入批次页面"):
        batch_page = app.navigate_to_batch()

    # 2. 创建批次（把你原代码里的 200 传进去）
    with allure.step("创建批次"):
        batch_page.create_batch(name="test", count="200")

    # 3. 断言结果（验证列表中出现新东西）
    with allure.step("断言批次创建成功"):
        batch_page.verify_batch_created(name="test", device_name="室内云台 Y2")

    # 4. 点击去采购并授权
    with allure.step("点击去采购并授权"):
        batch_page.click_buy_authorization()

@allure.title("设备台账恢复出厂设置并查看授权说明")
def test_device_factory_restore(zhaizhitong_app: MainPage):
    """测试：设备台账恢复出厂设置，并查看授权说明新窗口"""
    app = zhaizhitong_app

    # 1. 切换语言（复现你原代码的切语言动作）
    with allure.step("切换语言"):
        app.switch_language("en")
        app.switch_language("zh-CN")

    # 2. 进入设备台账
    with allure.step("进入设备台账"):
        device_page = app.navigate_to_device_ledger()

    # 3. 恢复出厂设置（并取消）
    with allure.step("恢复出厂设置"):
        device_page.restore_factory_settings()

    # 4. 测试多窗口（新标签页）
    with allure.step("打开授权说明"):
        device_page.open_device_auth_guide()

@allure.title("退出登录")
def test_logout(zhaizhitong_app: MainPage):
    """测试：退出登录"""
    # 因为你的 fixture 返回的是 main_page，
    # 退出登录属于 LoginPage 的动作，这里稍微变通一下或者直接写在 fixture 里
    page = zhaizhitong_app.page
    page.get_by_text("张", exact=True).first.click()
    page.get_by_role("button", name="退出登录").click()

    # 断言：退出后，应该重新出现了“开发者平台”按钮
    from playwright.sync_api import expect

    expect(page.get_by_role("button", name="开发者平台", exact=True)).to_be_visible()


@allure.title("注册新账号")
def test_register(page):
    """测试：注册新账号"""
    reg_page = RegisterPage(page)
    with allure.step("打开注册页面"):
        reg_page.goto()
    with allure.step("注册新账号"):
        reg_page.register(
            phone="14776956774", verify_code="123456", password="tt12345678"
        )
    with allure.step("断言注册成功"):
        reg_page.verify_register_success()
