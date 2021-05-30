import time
import urllib.request as urllib2


def check_time(url, target):
    response = urllib2.urlopen(url)
    ts = response.headers['date']

    s_time = time.strptime(ts[5:25], "%d %b %Y %H:%M:%S")
    print("Present time(GMT): ")
    print(f'{s_time.tm_year}-{s_time.tm_mon}-{s_time.tm_mday} {s_time.tm_hour}:{s_time.tm_min}:{s_time.tm_sec}')
    t_time = target
    print("Target time(GMT): ")
    print(f'{t_time[0]}-{t_time[1]}-{t_time[2]} {t_time[3]}:{t_time[4]}:{t_time[5]}')

    present_ts = time.mktime(s_time)
    target_ts = time.mktime(t_time)
    print(f"Converted present time: {present_ts}")
    print(f"Converted target time: {target_ts}")

    if present_ts < target_ts:
        print("Stop messing around! Think for yourself! Go study NOW!!!")
    else:
        print("Congrats! Now you may take a little break!")
        # Your own account info here
        print("Your recovery e-mail account: ******@********.***")
        print("E-mail password: **********")
        print("Steam Password: **********")


if __name__ == '__main__':
    url = 'http://www.baidu.com'
    target = (2021, 6, 15, 12, 22, 30, 1, 1, 1)
    check_time(url, target)
    input('Press <Enter>')
