import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Test:

    driver = webdriver.Chrome()
    driver.get("https://seleniumbase.io/demo_page")
    driver.maximize_window()

    c2 = driver.find_element(By.ID, "checkBox2")
    c3 = driver.find_element(By.ID, "checkBox3")
    c4 = driver.find_element(By.ID, "checkBox4")
    c5 = driver.find_element(By.ID, "checkBox5")

    def test_title(self):
        print(self.driver.title)
        print(self.driver.current_url)
        assert self.driver.title in 'Web Testing Page'

    def test_hover(self):
        hover = self.driver.find_element(By.ID, "myDropdown")
        link3 = self.driver.find_element(By.ID, "dropOption3")
        ActionChains(self.driver).move_to_element(hover).move_to_element(link3).click().perform()

    def test_textinput(self):
        textinput = self.driver.find_element(By.ID, "myTextInput")
        self.driver.save_screenshot('beforeTextinput.png')
        textinput.send_keys("Selenium Base")
        self.driver.save_screenshot('AfterTextinput.png')

    def test_myt(self):
        textinput = self.driver.find_element(By.ID, "myTextarea")
        self.driver.save_screenshot('BeforeTextarea.png')
        textinput.send_keys("You Will be a Great Tester")
        self.driver.save_screenshot('AfterTextarea.png')

    def test_prefilled(self):
        textinput = self.driver.find_element(By.ID, "myTextInput2")
        self.driver.save_screenshot('1prefillText.png')
        textinput.clear()
        textinput.send_keys("Great Tester")
        self.driver.save_screenshot('2prefillText.png')

    def test_button(self):
        buttonpress = self.driver.find_element(By.ID, "myButton")
        self.driver.save_screenshot('1buttonOn.png')
        buttonpress.click()
        self.driver.save_screenshot('2buttonOff.png')

    def test_place_text(self):
        placeholder = self.driver.find_element(By.ID, "placeholderText")
        self.driver.save_screenshot('1placeholderText.png')
        placeholder.send_keys("Google India")
        self.driver.save_screenshot('2placeholderText.png')

    def test_readonly(self):
        readonly = self.driver.find_element(By.ID, "readOnlyText")
        self.driver.save_screenshot('1readOnlyText.png')
        text = readonly.get_attribute('value')
        print(text)
        self.driver.save_screenshot('2readOnlyText.png')

    def test_svg(self):
        svg = self.driver.find_element(By.ID, "svgRect")
        svg.click()
        self.driver.save_screenshot('1SVGon.png')
        time.sleep(2)
        svg.click()
        time.sleep(2)
        self.driver.save_screenshot('2SVGoff.png')

    def test_para(self):
        para = self.driver.find_element(By.ID, "pText")
        self.driver.save_screenshot('1pText.png')
        ptext = para.text
        print(ptext)
        self.driver.save_screenshot('2pText.png')

    def test_slider(self):
        slider = self.driver.find_element(By.ID, "mySlider")
        self.driver.save_screenshot('1mySlider.png')
        time.sleep(2)
        ActionChains(self.driver).drag_and_drop_by_offset(slider, 40, 0).perform()
        time.sleep(1)
        self.driver.save_screenshot('2mySlider.png')
        time.sleep(2)
        ActionChains(self.driver).drag_and_drop_by_offset(slider, -60, 0).perform()
        time.sleep(1)
        self.driver.save_screenshot('3mySlider.png')

    def test_dlist(self):
        drop = self.driver.find_element(By.ID, "mySelect")
        self.driver.save_screenshot('1dropList.png')
        values = Select(drop)
        opts = values.options
        for value in opts:
            print(value.text)
        values.select_by_index(2)
        self.driver.save_screenshot('2dropList.png')

    def test_fimage(self):
        f1 = self.driver.find_element(By.ID, "myFrame1")
        self.driver.switch_to.frame(f1)
        img = self.driver.find_element(By.XPATH, "//img[contains(@style,'display')]").is_displayed()
        print(img)
        self.driver.switch_to.parent_frame()

    def test_ftext(self):
        f2 = self.driver.find_element(By.ID, "myFrame2")
        self.driver.switch_to.frame(f2)
        ftext = self.driver.find_element(By.XPATH, "//h4[text()='iFrame Text']").text
        print(ftext)
        self.driver.switch_to.parent_frame()

    def test_radiobutton(self):
        b1 = self.driver.find_element(By.ID, "radioButton1")
        b2 = self.driver.find_element(By.ID, "radioButton2")
        print(b1.is_selected())
        t = b1.is_selected()
        if t is True:
            b2.click()
        else:
            b1.click()

    def test_checkbutton(self):
        check1 = self.driver.find_element(By.ID, "checkBox1")
        print(check1.is_selected())
        c = check1.is_selected()
        if c is True:
            pass
        else:
            check1.click()

    # Single check Selection checkbox2
    def test_f1(self):
        print("First Check box Selection")
        if self.c2 is True:
            print("First Check box Selected")
        else:
            self.c2.click()
            print("First Check box Selected")
        time.sleep(1)
        self.c2.click()
        time.sleep(2)

    # Single check Selection checkbox
    def test_f2(self):
        print("Second Check box Selection")
        if self.c3 is True:
            print("Second Check box Selected")
        else:
            self.c3.click()
            print("Second Check box Selected")
        time.sleep(1)
        self.c3.click()
        time.sleep(2)

    # Single check Selection checkbox
    def test_f3(self):
        print("Third Check box Selection")
        if self.c4 is True:
            print("Third Check box Selected")
        else:
            self.c4.click()
            print("Third Check box Selected")
        time.sleep(1)
        self.c4.click()
        time.sleep(2)

    # Double check Selection checkbox
    def test_f4(self):
        print("first 2 Check box Selection")
        if self.c2 is True and self.c3 is True:
            print("first 2 Check box Selected")
        else:
            self.c2.click()
            self.c3.click()
            print("first 2 Check box Selected")
        time.sleep(1)
        self.c2.click()
        self.c3.click()
        time.sleep(2)

    # Double check Selection checkbox
    def test_f5(self):
        print("last 2 Check box Selection")
        if self.c3 is True and self.c4 is True:
            print("last 2 Check box Selected")
        else:
            self.c3.click()
            self.c4.click()
            print("last 2 Check box Selected")
        time.sleep(1)
        self.c3.click()
        self.c4.click()
        time.sleep(2)

    # Double check Selection checkbox
    def test_f6(self):
        print("first & last 2 Check box Selection")
        if self.c2 is True and self.c4 is True:
            print("first & last 2 Check box Selected")
        else:
            self.c2.click()
            self.c4.click()
            print("first & last 2 Check box Selected")
        time.sleep(1)
        self.c2.click()
        self.c4.click()
        time.sleep(2)

    # All checkbox Selection
    def test_f7(self):
        print("All Check box Selection")
        if self.c2 is True and self.c3 is True and self.c4 is True:
            print("All Check box Selected")
        else:
            self.c2.click()
            self.c3.click()
            self.c4.click()
            print("first & last 2 Check box Selected")
            time.sleep(2)

    def test_pk(self):
        if self.c5 is True:
            self.c5.click()
            time.sleep(3)
            self.c5.click()
            print(self.c5.is_selected())
            if self.c5 is True:
                print("Checkbox is working Fine")
            else:
                print("Try again with better efforts")
        else:
            self.c5.click()

    def test_cframe(self):
        self.driver.switch_to.frame(self.driver.find_element(By.ID, "myFrame3"))
        self.c6 = self.driver.find_element(By.ID, "checkBox6")
        if self.c6 is True:
            self.c6.click()
            time.sleep(3)
            self.c6.click()
            print(self.c6.is_selected())
            if self.c6 is True:
                print("Checkbox is working Fine")
            else:
                print("Try again with better efforts")
        else:
            self.c6.click()
            print("Checkbox is working Fine with one click selection")
        self.driver.switch_to.parent_frame()

    def test_clink(self):

        mlink = self.driver.find_element(By.ID, "myLink1")
        mlink.click()
        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to.window(handle)
            print(self.driver.title)
            print("Successfully return back to main page")
        time.sleep(2)
        self.driver.back()
        self.driver.close()

# last test for website
