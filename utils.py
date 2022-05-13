import sheets

def createNewDept(user_name, propose, debt_sum):
    user = sheets.wks.row_values(1).index(user_name) + 1
    row_number = len(sheets.wks.col_values(user)) + 1

    sheets.wks.update_cell(row_number, user, propose)
    sheets.wks.update_cell(row_number, user + 1, debt_sum)

    return (f"Текущий долг у пользователя {user_name}: {sheets.wks.cell(3, user + 1).value}")

def get_users():
    row_values = sheets.wks.row_values(1)
    users_list = [x for x in row_values if x]
    return users_list