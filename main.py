import tkinter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def Send_Formatted_Message():
    global driver
    message = message_text.get("1.0", tkinter.END)
        
    input("Select chat to send message")
    passed = False

    while not passed:
        try:
            message_input = driver.find_element(
                By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
            print(message_input)
            passed = True
        except:
            input("Error,  please select chat to send message and then press ENTER")
            passed = False
    print("OK")
    message_input.send_keys(message)
    message_input.send_keys(Keys.RETURN)


def Format_Selection(type_=0):
    if not type_:  # Bold
        formatted_line = "*" + message_text.selection_get() + "*"
    elif type_ == 1:  # Italic
        formatted_line = "_" + message_text.selection_get() + "_"
    elif type_ == 2:  # Crossed
        formatted_line = "~" + message_text.selection_get() + "~"
    elif type_ == 3:  # Fixed Sys
        formatted_line = "```" + message_text.selection_get() + "```"
    else:
        return -1
    new_text = message_text.get("1.0", tkinter.END).replace(
        message_text.selection_get(), formatted_line)
    message_text.delete("1.0", tkinter.END)
    message_text.insert("1.0", new_text)

driver = webdriver.Firefox()
driver.get('https://web.whatsapp.com')
print("Don't forget to auth whatsapp session by QR code!")
root = tkinter.Tk()
root.geometry("600x550")
message_text = tkinter.Text()
message_text.pack()
set_bold = tkinter.Button(text="Bold", command=lambda: Format_Selection(0))
set_bold.pack()
set_italic = tkinter.Button(text="Italic", command=lambda: Format_Selection(1))
set_italic.pack()
set_crossed = tkinter.Button(
    text="Crossed", command=lambda: Format_Selection(2))
set_crossed.pack()
set_font_fixed_sys = tkinter.Button(
    text="Fixed Sys", command=lambda: Format_Selection(3))
set_font_fixed_sys.pack()

send_btn = tkinter.Button(text="Send", command=Send_Formatted_Message)
send_btn.pack()
root.mainloop()
