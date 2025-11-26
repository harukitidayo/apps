
import streamlit as st
from openpyxl import load_workbook, Workbook
from pathlib import Path
from datetime import datetime

st.title("チェックリストアプリ（スマホ対応）")

# 質問リスト
items = ["電源投入エラーなし", "温度センサー正常", "ジャム履歴なし"]
checked = []
for item in items:
    if st.checkbox(item):
        checked.append(item)

# 保存ボタン
if st.button("結果を保存"):
    target_path = Path(r"C:\temp\checklist.xlsx")
    target_path.parent.mkdir(parents=True, exist_ok=True)
    if not target_path.exists():
        wb = Workbook()
        wb.active.title = "Checklist"
        wb.save(target_path)

    wb = load_workbook(target_path)
    ws = wb.active
    start_row = ws.max_row + 1
    ws.cell(row=start_row, column=1, value=datetime.now().strftime("%Y-%m-%d %H:%M"))
    ws.cell(row=start_row, column=2, value="✔".join(checked))
    wb.save(target_path)
    st.success(f"保存しました → {target_path}")
    
    
    
