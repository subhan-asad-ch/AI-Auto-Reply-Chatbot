import pyperclip
import time
from cursor-points import click_on_chrome_icon, select_text, paste_response, click_on_input_box
from Integrating Open AI import is_last_message_from_sender, get_chat_response

def main():
    click_on_chrome_icon()
    while True:
        time.sleep(5)
        select_text()
        
        chat_history = pyperclip.paste()
        print(chat_history)
        print(is_last_message_from_sender(chat_history))
        
        if is_last_message_from_sender(chat_history):
            response = get_chat_response(chat_history)
            pyperclip.copy(response)
            click_on_input_box()
            paste_response()

if __name__ == "__main__":
    main()
