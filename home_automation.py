import http_server
import wiiu_daemon
import threading


def main():
    http_server.main(port=80)


if __name__ == '__main__':
    main()
