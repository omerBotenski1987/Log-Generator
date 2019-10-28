from random import randint, choice
import requests


def loggen():
    # Create a log line constructed of various predefined variables:
    mes_list = ["HTTP error 401 (UNAUTHORIZED)", "HTTP error 400 (bad request)", "HTTP error 403 (FORBIDDEN)",
                "HTTP error 404 (not found)", "HTTP error 500 (internal server error)",
                "SECURITY ALERT - Your host is under attack!"]
    quantity = randint(1,10000)
    host = ["host_1", "host_2", "host_3", "host_4", "host_5", "host_6", "host_7", "host_8", "host_9", "host_10",
            "host_11", "host_12", "host_13", "host_666"]
    ipAddress = ["192.168.53.24", "10.10.12.138", "103.10.10.11", "192.168.1.1", "8.8.8.8", "4.4.4.4", "192.168.32.123",
                 "172.38.282.1"]
    os = ["windows", "macOS.system", "ubuntu", "linux", "android", "iOS"]
    rand_field = '"field_{index}":"same_value"'.format(index=(randint(21, 40)))
    bands = ["nirvana", "beatles", "queen", "kaveret", "ac_dc", "tallest_man_on_earth", "hiss_golden_messanger",
            "eminem", "snoop_dog", "led_zepplin", "red,comma"]
    logLevel = ["WARN", "INFO", "DEBUG", "ERROR"]
    log = '{{"message": "{message}", "type": "demo_logs", "host": "{host}", "logLevel": "{logLevel}", "quantity": {qty}, "IP_Address": "{ip}", "bands": "{bands}", "operating.system": "{opsys}", {random_field}'.format(
        message=choice(mes_list), host=choice(host), qty=quantity, ip=choice(ipAddress), bands=choice(bands), opsys=choice(os), logLevel=choice(logLevel), random_field=rand_field)
    final_log = log + '}'

    return final_log


if __name__ == '__main__':
    x = randint(20,300)
    accountUrl = "http://listener.logz.io:8070/?token=CQmkmIksjWVlxCdDFpFTFGwgXHrIajfO&type=logGen"
    data = ''
    for count in range(0, x):
        data = '{}\n{}'.format(data, loggen())

    response = requests.post(accountUrl, data)
    print(response)
    print("Number of log lines generated:" + str(x))
    print("Log output sample: " + loggen())
