var http = require('http');

http.createServer(function (req, res) {
	res.writeHead(200, {'Content-Type': 'text/plain'});
	res.end('Hello World\n');
}).listen(81, "0.0.0.0");

console.log('Simple web running on FOX Board G20');
