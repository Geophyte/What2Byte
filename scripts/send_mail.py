import smtplib
import ssl
from datetime import date
from load_save import file_path
import shopping_list

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "what2byte@gmail.com"
file_name = file_path.shoping_list


def get_pass():
    # return getpass.getpass(prompt="Type your password and press enter:")
    return "Pzsp1W2B"


def get_email(email=None) -> str:
    if email is None:
        return input("Proszę podać adess email: ")
    return email


def login_loop(server):
    try:
        server.login(sender_email, get_pass())
    except Exception:
        login_loop(server)


def send_list(mail):
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        login_loop(server)
        server.sendmail(
            sender_email,
            mail,
            make_shoping_list_text(file_name),
        )


def fill_items():
    if shopping_list.to_str() == "":
        return "Niczego nie brakuje"
    return shopping_list.to_str()


def make_shoping_list_text(shoping_list_file: file_path):
    msg = ""
    with open(shoping_list_file.value, "r") as shoping_list:
        msg = msg.join(_ for _ in shoping_list.readlines())
    msg = msg.format(
        current_date=get_date(),
        missing_product_list=fill_items(),
    )
    msg = msg.replace("ą", "a")
    msg = msg.replace("ę", "e")
    msg = msg.replace("ł", "l")
    msg = msg.replace("ć", "c")
    msg = msg.replace("ź", "z")
    msg = msg.replace("ż", "z")
    msg = msg.replace("ś", "s")
    msg = msg.replace("ó", "o")
    return msg


def get_date() -> str:
    return date.today().strftime("%d/%m/%Y")


if __name__ == "__main__":
    ingredients = {"a": 100, "c": 400, "b": 200, "cc": 500}
    shopping_list.add_items(ingredients)

    print(get_date())
    print(make_shoping_list_text(file_name))
    send_list(get_email())
