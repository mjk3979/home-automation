import http_server
import wiiu_daemon
import threading


def main():
    # wiiu = threading.Thread(target=wiiu_daemon.main)
    # wiiu.start()
    http_server.main(port=80)


if __name__ == '__main__':
    main()
