var ws = new WebSocket('ws://localhost:8000/ws/chat/room/');

ws.onopen = (e) => {
    console.log('connected: ', e);
    ws.send('client');
};


ws.onerror = (e) => {
    console.log('error: ' ,e);
};


ws.onmessage = (e) => {
    console.log('message: ', e);
    console.log('message: ', e.data);
};

ws.onclose = (e) => {
    
    console.log('closed: ' ,e);
};