var fs = require('fs');

/*
// readFileSync
console.log('A');
var result = fs.readFileSync('syntax/sample.txt', 'utf8');
console.log(result);
console.log('C');
*/

// Sync가 없으면 비동기 -> 비동기는 3번째 인자를 callback(=함수), 리턴값이 없으므로 변수선언 X

console.log('A');
fs.readFile('syntax/sample.txt', 'utf8', function (err, result) {
    console.log(result);
});
console.log('C');