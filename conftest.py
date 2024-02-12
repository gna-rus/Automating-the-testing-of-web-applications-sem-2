

@pytest.fixture
def button():
    btn_selector = "//*[@id='login']/div[3]/button"
    return btn_selector

@pytest.fixture
def element():
    x_selector3 = """//*[@id="app"]/main/div/div/div[2]/h2"""
    return x_selector3

@pytest.fixture
def site(score='session'):
    site_instance = Site(testdata['address'])
    yield site_instance
    site_instance.close()

@pytest.fixture
def result():
    return "401"
