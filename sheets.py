import gspread

sa = gspread.service_account()
sh = sa.open("DebtsDamir")
wks = sh.worksheet("Sheet1")