# sysfetcher - the alternative for neofetch
# By DevFalongor (c), GNU GPL v3, 2023
import socket
import platform
import subprocess

TEMPLATE = """

 \033[92m         a88888.                    {hostname} \033[0m
 \033[92m        d888888b.                \033[0m   {hostname_sep}
 \033[92m        d888888b.                \033[0m\033[93m · OS: {os_version}
 \033[92m        8P"YP"Y88                \033[0m\033[93m · Kernel:{kernel}
 \033[93m        8|o||o|88                \033[0m\033[93m · Cpu architecture: {cpu}
 \033[93m        8'    .88                \033[0m\033[93m · Shell: {shell}
 \033[93m        8'    .88                \033[0m\033[93m · DE(WM): {de}
 \033[93m        8`._.' Y8                \033[0m\033[93m · Uptime: {uptime}
 \033[91m       d/      `8b.              \033[0m\033[93m · Resolution: {size}
 \033[91m     .dP   .     Y8b             \033[0m\033[93m · Local IP: {local_ip}
 \033[91m     d8:'   "   `::88b.
 \033[95m    d8"           `Y88b
 \033[95m   :8P     '       :888
 \033[95m    8a.    :      _a88
 \033[94m    ._/"Yaa_ :    .| 88P|
 \033[94m     \    YP"      `| 8P  `.
 \033[94m    /     \._____.d|    .'
 \033[94m    `--..__)888888P`._.'

\033[30m███\033[0m\033[91m███\033[0m\033[92m███\033[0m\033[93m███\033[0m\033[94m███\033[0m\033[95m███\033[0m\033[96m███\0
"""


def local_ip():
    # Get local ip address
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except:
        return None


def host_name():
    # Get host name
    try:
        return socket.gethostname()
    except:
        return None
        

def os_version():
    # Get linux distro version
    try:
        return platform.linux_distribution(distname='', version='', id='', supported_dists=('SuSE', 'debian', 'redhat', 'mandrake', "ubuntu", "centos", "arch"), full_distribution_name=1)
    except:
        return "Linux-based OS"


def screen_size():
    # Get size of screen
    try:
        return subprocess.check_output(["xrandr | grep \"*\""], shell=True).decode('utf-8')
    except:
        return None
        
        
def uptime():
    # Get uptime
    try:
        return subprocess.check_output(["uptime -p"], shell=True).decode('utf-8')
    except:
        return None


def shell():
    # Get shell
    try:
        return os.environ.get('SHELL', '')
    except:
        return None


def kernel():
    # Get kernel version
    try:
        return platform.release()
    except:
        return None
        

def cpu_spec():
    # Get CPU architecture
    try:
        return platform.processor()
    except:
        return None


def de():
    # Get the de/wm
    try:
        return os.environ.get('DESKTOP_SESSION')
    except:
        return None


if __name__ == "__main__":
    print(TEMPLATE.format(hostname = host_name(),
        hostname_sep = "=" * len(host_name()),
        os_version=os_version(),
        kernel=kernel(),
        cpu=cpu_spec(),
        shell=shell(),
        de=de(),
        uptime=uptime(),
        size=screen_size(),
        local_ip=local_ip()
    ))
