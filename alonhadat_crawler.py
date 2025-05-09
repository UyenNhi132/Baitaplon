from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import schedule
import datetime

def init_driver():
    """Khởi tạo trình duyệt Chrome với cấu hình user-agent."""
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
    return webdriver.Chrome(options=options)

def get_page_data(driver, page):
    """
    Thu thập dữ liệu từ một trang cụ thể.
    Trả về danh sách dữ liệu và trạng thái có dữ liệu hay không.
    """
    url = f"https://alonhadat.com.vn/nha-dat/can-ban/can-ho-chung-cu/3/da-nang/trang--{page}.html"
    print(f"Đang crawl trang {page}...")
    driver.get(url)
    time.sleep(2)

    data = []
    titles = driver.find_elements(By.XPATH, '//*[@id="left"]/div[1]/div[*]/div[1]/div[1]/a')
    summaries = driver.find_elements(By.XPATH, '//*[@id="left"]/div[1]/div[*]/div[4]/div[1]')
    areas = driver.find_elements(By.XPATH, '//*[@id="left"]/div[1]/div[*]/div[4]/div[3]/div[1]')
    addresses = driver.find_elements(By.XPATH, '//*[@id="left"]/div[1]/div[*]/div[4]/div[4]/div[2]')
    prices = driver.find_elements(By.XPATH, '//*[@id="left"]/div[1]/div[*]/div[4]/div[4]/div[1]')

    if not titles:
        print(f" Hết dữ liệu ở trang {page}. Dừng crawl.")
        return data, False

    for i in range(len(titles)):
        data.append([
            titles[i].text.strip() if i < len(titles) else "",
            summaries[i].text.strip() if i < len(summaries) else "",
            areas[i].text.strip() if i < len(areas) else "",
            prices[i].text.strip() if i < len(prices) else "",
            addresses[i].text.strip() if i < len(addresses) else ""
        ])
    
    return data, True

def save_to_excel(data):
    """Lưu dữ liệu vào file Excel với tên file theo ngày hiện tại."""
    today = datetime.datetime.now().strftime("%Y%m%d")
    df = pd.DataFrame(data, columns=["Tiêu đề", "Mô tả", "Diện tích", "Giá", "Địa chỉ"])
    output_file = f"alonhadat{today}.xlsx"
    df.to_excel(output_file, index=False)
    print(f" Đã lưu {len(data)} tin vào {output_file}")

def crawl_alonhadat():
    """Hàm chính để crawl dữ liệu căn hộ Đà Nẵng từ alonhadat.com.vn."""
    driver = init_driver()
    all_data = []
    page = 1

    try:
        while True:
            page_data, has_data = get_page_data(driver, page)
            all_data.extend(page_data)
            if not has_data:
                break
            page += 1
        save_to_excel(all_data)
    finally:
        driver.quit()

if __name__ == "__main__":
    schedule.every().day.at("13:48").do(crawl_alonhadat)
    print(" Đã lên lịch chạy lúc 6:00 sáng mỗi ngày.")
    #crawl_alonhadat()
    while True:
        schedule.run_pending()
        time.sleep(60)