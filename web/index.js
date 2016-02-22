function desktop() {
    request = new XMLHttpRequest();
    request.open('POST', '/desktop');
    request.send(null);
}

function off() {
    request = new XMLHttpRequest();
    request.open('POST', '/off');
    request.send(null);
}
