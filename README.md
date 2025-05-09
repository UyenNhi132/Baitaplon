# Tự Động Thu Thập Dữ Liệu Bất Động Sản Đà Nẵng từ Alonhadat.com.vn

Kho lưu trữ này chứa một script Python thực hiện việc **thu thập thông tin các căn hộ chung cư đang rao bán tại Đà Nẵng** từ website [alonhadat.com.vn](https://alonhadat.com.vn), sau đó lưu thành file Excel theo ngày. Script có thể chạy thủ công hoặc tự động mỗi ngày bằng Task Scheduler.

---

## 1. Cấu Hình

**File chính:** `alonhadat_crawler.py`  
**Đầu ra:** file Excel theo ngày, ví dụ: `alonhadat_20240509.xlsx`

Các cột dữ liệu bao gồm:

- Tiêu đề
- Mô tả
- Diện tích
- Giá
- Địa chỉ

---

## 2. Cài Đặt Phụ Thuộc

Cài đặt thư viện cần thiết bằng pip:

```bash
pip install -r requirements.txt
```

---

## 3. Chạy Script Thủ Công

Thực thi script bằng lệnh:

```bash
python alonhadat_crawler.py
```

---

## 4. Tự Động Với Task Scheduler Trên Windows

### Hướng dẫn tạo lịch tự động chạy mỗi ngày:

1. Mở **Task Scheduler**.
2. Chọn **Create Task**.
3. **Tab General**:
   - Đặt tên ví dụ: `Alonhadat Crawler`.
4. **Tab Triggers**:
   - Nhấn `New...`
   - Chọn **Daily**, đặt giờ `06:00:00 AM`.
5. **Tab Actions**:
   - **Action**: Start a program
   - **Program/script**: đường dẫn tới `python.exe` (ví dụ: `C:\Python311\python.exe`)
   - **Add arguments**: đường dẫn tới `alonhadat_crawler.py`
   - **Start in**: thư mục chứa script (ví dụ: `D:\duan`)
6. Nhấn **OK** để lưu.

---

## 5. Kết Quả

Một file `.xlsx` sẽ được tạo tự động mỗi ngày trong thư mục hiện tại với định dạng:

```
alonhadat_YYYYMMDD.xlsx
```

Ví dụ:

```
alonhadat_20240509.xlsx
