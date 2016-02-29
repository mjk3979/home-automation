function send_command(cmd) {
    request = new XMLHttpRequest();
    request.open('POST', '/' + cmd);
    request.send(null);
}
