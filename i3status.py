"""
Return differents informations of the computer
"""
import time
import os
import socket
import subprocess
import psutil

def date():
    """ Return actual date"""
    print("DATE :")
    print(time.strftime("%A %d %B %Y %H:%M:%S"), end='\n\n')


def seconds_to_hours(secs):
    """ Convert Seconds to Hours """
    minute, second = divmod(secs, 60)
    hour, minute = divmod(minute, 60)
    return "%d:%02d:%02d" % (hour, minute, second)


def battery():
    """ Return battery infos """
    if not hasattr(psutil, "sensors_battery"):
        return "We can't access battery infos on this platform, sorry"
    batt = psutil.sensors_battery()
    if batt is None:
        return "No battery is installed"

    print("BATTERY :")
    print("charge:     %s%%" % round(batt.percent, 2))
    if batt.power_plugged:
        print("status:     %s" % (
            "charging" if batt.percent < 100 else "fully charged"))
        print("plugged in: yes", end='\n\n')
    else:
        print("left:       %s" % seconds_to_hours(batt.secsleft))
        print("status:     %s" % "discharging")
        print("plugged in: no", end='\n\n')


def bytes2human(byte):
    """ Convert bytes to human value """
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, j in enumerate(symbols):
        prefix[j] = 1 << (i+1)*10
    for j in reversed(symbols):
        if byte >= prefix[j]:
            value = float(byte) / prefix[j]
            return '%.1f%s' % (value, j)
    return "%sB" % byte


def bytes_available():
    """ Byte available on disk """
    free_disk = psutil.disk_usage('/')
    print("STOCKAGE AVAILABLE")
    print(bytes2human(free_disk.free), end='\n\n')


def ping():
    """ return ping """
    oui = open(os.devnull, 'w')
    retcode = subprocess.call(['ping', "-c", "1", '8.8.8.8'], stdout=oui, stderr=subprocess.STDOUT)

    if retcode == 1:
        print("Internet is OK", end='\n\n')
    else:
        print("Internet is down", end='\n\n')


def local_ip():
    """ Print hostname and IP """
    hostname = socket.gethostname()
    print(hostname)
    print(socket.gethostbyname(hostname))

def cpu():
    """ Print CPU usage """
    print("CPU usage :", psutil.cpu_percent(interval=0.5))


if __name__ == '__main__':
    os.system('clear')
    print("i3status", end='\n\n')
    date()
    battery()
    bytes_available()
    ping()
    cpu()
