# 🛡️ Selenium Automation Framework (Python)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-4.x-green?style=for-the-badge&logo=selenium&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

> **Mô tả:** Dự án kiểm thử tự động (Automation Testing) được xây dựng bằng ngôn ngữ Python và thư viện Selenium WebDriver. Framework này được thiết kế để kiểm thử chức năng (Functional Testing) và giao diện (UI Testing) cho ứng dụng web, tích hợp cơ chế báo cáo lỗi tự động qua ảnh chụp màn hình.

---

## 📑 Mục lục
1. [Giới thiệu](#-giới-thiệu)
2. [Cấu trúc dự án](#-cấu-trúc-dự-án)
3. [Yêu cầu hệ thống](#-yêu-cầu-hệ-thống)
4. [Cài đặt & Cấu hình](#-cài-đặt--cấu-hình)
5. [Hướng dẫn chạy Test](#-hướng-dẫn-chạy-test)
6. [Kết quả & Báo cáo](#-kết-quả--báo-cáo)
7. [Tác giả](#-tác-giả)

---

## 🌟 Giới thiệu
Dự án tập trung vào việc tự động hóa các kịch bản kiểm thử lặp đi lặp lại (Regression Testing). 
**Các tính năng chính:**
* 🚀 **Page Interaction:** Tương tác tự động với các phần tử web (Input, Click, Scroll...).
* 📸 **Screenshot on Failure:** Tự động chụp và lưu ảnh màn hình khi Test Case thất bại.
* 📊 **Modular Design:** Code được tách biệt giữa logic kiểm thử và các hàm tiện ích (Utils).

---

## 📂 Cấu trúc dự án
Mô hình thư mục được tổ chức theo chuẩn clean code:

```text
selenium-automation/
├── drivers/                # Chứa WebDriver (Chromedriver/Geckodriver)
├── screenshots/            # 📸 Thư mục chứa ảnh lỗi (Tự động sinh ra khi chạy)
├── tests/                  # Chứa các Test Suites và Test Cases
│   ├── __init__.py
│   └── login_test.py       # Ví dụ: Kịch bản test đăng nhập
├── utils.py                # 🛠 Các hàm tiện ích (Helper functions: Screenshot, Wait...)
├── main_test.py            # 🏁 File thực thi chính (Test Runner)
├── .gitignore              # Cấu hình file ẩn git
├── requirements.txt        # Danh sách các thư viện phụ thuộc
└── README.md               # Tài liệu hướng dẫn

```

---

## ⚙️ Yêu cầu hệ thống

* **OS:** Windows 10/11, macOS, hoặc Linux.
* **Python:** Phiên bản 3.8 trở lên.
* **Browser:** Google Chrome (Khuyến nghị) hoặc Firefox.

---

## 🚀 Cài đặt & Cấu hình

### Bước 1: Clone dự án

Mở terminal và chạy lệnh:

```bash
git clone [https://github.com/username/project-name.git](https://github.com/username/project-name.git)
cd project-name

```

### Bước 2: Tạo môi trường ảo (Virtual Environment)

Luôn khuyến khích sử dụng môi trường ảo để tránh xung đột thư viện:

* **Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate

```


* **macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate

```



### Bước 3: Cài đặt thư viện

```bash
pip install -r requirements.txt

```

### Bước 4: Cấu hình Webdriver (Tùy chọn)

Nếu bạn không sử dụng `webdriver-manager`, hãy tải `chromedriver.exe` phù hợp với phiên bản Chrome của bạn và đặt vào thư mục `drivers/`.

---

## ▶️ Hướng dẫn chạy Test

Để chạy toàn bộ kịch bản kiểm thử, sử dụng lệnh sau tại thư mục gốc:

```bash
python main_test.py

```

Nếu bạn muốn chạy một test case cụ thể (Ví dụ test login):

```bash
python tests/login_test.py

```

---

## 📊 Kết quả & Báo cáo

### Cơ chế chụp ảnh lỗi (Evidence)

Khi một Test Case bị **FAILED**, hệ thống sẽ:

1. Tự động chụp màn hình tại thời điểm lỗi.
2. Lưu ảnh vào thư mục `screenshots/`.
3. Tên file được định dạng: `TestName_YYYY-MM-DD_HH-MM-SS.png`.

*Ví dụ ảnh lỗi:*

> `screenshots/test_login_failed_2025-01-13_18-30-00.png`

---

## 👨‍💻 Tác giả

**[Tên của bạn]**

* 🎓 Sinh viên: Trường Đại học Công Thương TP.HCM (HUIT)
* 📧 Email: [Email của bạn]
* 💻 Github: [@username](https://www.google.com/search?q=https://github.com/username)

---

*Dự án này được thực hiện cho mục đích học tập và nghiên cứu môn Kiểm thử phần mềm.*

```

---

### Một việc nhỏ bạn cần làm để file README này hoạt động chuẩn:

Trong file hướng dẫn có nhắc đến `requirements.txt`. Để tạo file này chuẩn chỉnh cho người khác dùng, bạn hãy làm thao tác này **một lần duy nhất** sau khi đã cài xong các thư viện:

1.  Mở Terminal (đang bật venv).
2.  Gõ lệnh:
    ```bash
    pip freeze > requirements.txt
    ```
3.  Lúc này file `requirements.txt` sẽ tự động sinh ra chứa tên các thư viện (ví dụ `selenium==4.x.x`).

Như vậy dự án của bạn đã **đầy đủ 3 yếu tố cốt lõi**: Code (Python) + Cấu hình (Gitignore) + Tài liệu (Readme/Requirements). Cực kỳ chuyên nghiệp!

```