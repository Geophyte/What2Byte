import smtplib, ssl
from datetime import date
import getpass
from load_save import file_path

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "what2byte@gmail.com"
file_name = file_path.shoping_list


def get_pass():
    # return getpass.getpass(prompt="Type your password and press enter:")
    return "Pzsp1W2B"


def get_email() -> str:
    mail = input("Proszę podać adess email: ")
    return mail


def login_loop(server):
    try:
        server.login(sender_email, get_pass())
    except Exception:
        login_loop(server)


def make_and_send_list():
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        login_loop(server)
        server.sendmail(
            sender_email,
            get_email(),
            make_shoping_list_text(file_name),
        )


def fill_items(missing_items: str = "placeholder"):
    return missing_items


def make_shoping_list_text(shoping_list_file: file_path):
    msg = ""
    with open(shoping_list_file.value, "r") as shoping_list:
        msg = msg.join(_ for _ in shoping_list.readlines())
    msg = msg.format(
        current_date=get_date(),
        missing_product_list=fill_items(),
    )
    return msg


def get_date() -> str:
    return date.today().strftime("%d/%m/%Y")


if __name__ == "__main__":
    print(get_date())
    make_shoping_list_text(file_name)
    make_and_send_list()
