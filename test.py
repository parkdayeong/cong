import tkinter as tk
from tkinter import messagebox
import csv
from datetime import datetime
from tkinter import filedialog

class QuotationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quotation Generator")

        # 견적 정보 입력 폼 생성
        self.label_date = tk.Label(master, text="Date:")
        self.label_date.grid(row=0, column=0)
        self.entry_date = tk.Entry(master)
        self.entry_date.grid(row=0, column=1)

        self.label_client = tk.Label(master, text="Client:")
        self.label_client.grid(row=1, column=0)
        self.entry_client = tk.Entry(master)
        self.entry_client.grid(row=1, column=1)

        self.label_item = tk.Label(master, text="Item:")
        self.label_item.grid(row=2, column=0)
        self.entry_item = tk.Entry(master)
        self.entry_item.grid(row=2, column=1)

        self.label_quantity = tk.Label(master, text="Quantity:")
        self.label_quantity.grid(row=3, column=0)
        self.entry_quantity = tk.Entry(master)
        self.entry_quantity.grid(row=3, column=1)

        self.label_unit_price = tk.Label(master, text="Unit Price:")
        self.label_unit_price.grid(row=4, column=0)
        self.entry_unit_price = tk.Entry(master)
        self.entry_unit_price.grid(row=4, column=1)

        self.label_vat = tk.Label(master, text="VAT:")
        self.label_vat.grid(row=5, column=0)
        self.entry_vat = tk.Entry(master)
        self.entry_vat.grid(row=5, column=1)

        self.label_conditions = tk.Label(master, text="Conditions:")
        self.label_conditions.grid(row=6, column=0)
        self.entry_conditions = tk.Entry(master)
        self.entry_conditions.grid(row=6, column=1)

        # 버튼 생성
        self.save_button = tk.Button(master, text="Save Quotation", command=self.save_quotation)
        self.save_button.grid(row=7, column=0, columnspan=2)

        self.download_button = tk.Button(master, text="Download Quotation", command=self.download_quotation)
        self.download_button.grid(row=8, column=0, columnspan=2)

    def save_quotation(self):
        # 입력된 견적 정보 가져오기
        date = self.entry_date.get()
        client = self.entry_client.get()
        item = self.entry_item.get()
        quantity = self.entry_quantity.get()
        unit_price = self.entry_unit_price.get()
        vat = self.entry_vat.get()
        conditions = self.entry_conditions.get()

        # 견적 정보를 텍스트 파일에 저장
        filename = f"{client}_quotation.txt"
        with open(filename, "a") as file:
            file.write(f"Date: {date}\n")
            file.write(f"Client: {client}\n")
            file.write(f"Item: {item}\n")
            file.write(f"Quantity: {quantity}\n")
            file.write(f"Unit Price: {unit_price}\n")
            file.write(f"VAT: {vat}\n")
            file.write(f"Conditions: {conditions}\n")
            file.write("\n")

        messagebox.showinfo("Success", "Quotation saved successfully!")

    def download_quotation(self):
        # 입력된 견적 정보 가져오기
        date = self.entry_date.get()
        client = self.entry_client.get()
        item = self.entry_item.get()
        quantity = self.entry_quantity.get()
        unit_price = self.entry_unit_price.get()
        vat = self.entry_vat.get()
        conditions = self.entry_conditions.get()

        # 현재 날짜 및 시간 가져오기 (파일명에 사용)
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        # 엑셀 파일 다운로드 경로 설정
        filepath = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if not filepath:
            return

        # 견적 정보를 CSV 파일에 저장
        with open(filepath, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Client", "Item", "Quantity", "Unit Price", "VAT", "Conditions"])
            writer.writerow([date, client, item, quantity, unit_price, vat, conditions])

        messagebox.showinfo("Success", f"Quotation downloaded successfully to {filepath}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuotationApp(root)
    root.mainloop()
