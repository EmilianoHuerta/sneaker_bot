  
from selenium import webdriver
from config import keys
import time

def timeme(method):
    def wrapper(*args, **kw):
        startTime = int(round(time.time() * 1000))
        result = method(*args, **kw)
        endTime = int(round(time.time() * 1000))
        print((endTime - startTime)/1000, 's')
        return result
    return wrapper

# will cookies improve load time?
#options = webdriver.ChromeOptions()
#options.add_argument('user-data-dir=www.supremenewyork.com')

@timeme
def order():
    # add to cart
    driver.find_element_by_class_name('fulfillment-add-to-cart-button').click()

    # wait for checkout button element to load
    time.sleep(.5)
    checkout_element = driver.find_element_by_class_name('fulfillment-add-to-cart-button')
    checkout_element.click()
    checkout_element_2 = driver.find_element_by_class_name('go-to-cart-button')
    checkout_element_2.click()
    checkout_element_3 = driver.find_element_by_class_name('btn btn-lg btn-block btn-primary')
    checkout_element_3.click()
    guest_click = driver.find_element_by_class_name('btn btn-secondary btn-lg cia-guest-content__continue js-cia-submit-button js-cia-guest-button')
    guest_click.click()
    switch_shipping = driver.find_element_by_class_name('ispu-card__switch')
    switch_shipping.click()

    # fill out checkout screen fields
    driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_5.firstName""]').send_keys(keys['first_name'])
    driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_5.lastName"]').send_keys(keys['last_name'])
    driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_5.street"]').send_keys(keys['address'])
    driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_5.city"]').send_keys(keys['city'])
    driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(keys['zip_code'])
    driver.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(keys['city'])
    payment_click = driver.find_element_by_class_name('btn btn-lg btn-block btn-secondary')
    payment_click.click()

    process_payment = driver.find_element_by_xpath('//*[@id="optimized-cc-card-number"]'.send_keys(keys['card_number']))
    driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_5.firstName""]').send_keys(keys['first_name'])
    driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_5.lastName"]').send_keys(keys['email'])
    driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_5.street"]').send_keys(keys['address'])
    driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_5.city"]').send_keys(keys['city'])
    driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(keys['zip_code'])
    driver.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(keys['city'])
    # driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(keys['card_cvv'])
    # driver.find_element_by_id('nnaerb').send_keys(keys['card_number'])




if __name__ == '__main__':
        # load chrome
    driver = webdriver.Chrome('./chromedriver')

    # get product url
    driver.get(keys['product_url'])
    order()