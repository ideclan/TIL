// @ts-check

// aaaaaabbbbbbbaaaaaaabbbbbb...aaaaabbbbb
// 위와 같은 파일에서, a의 연속 구간(a block)의 개수와, b의 연속 구간(b block)의 개수를 세기

const fs = require('fs')

const ws = fs.createWriteStream('local/big-file')

const NUM_BLOCKS = 500

/** @type {Object.<string, number>} */
const numBlocksPerCharacter = {
  a: 0,
  b: 0,
}

for (let i = 0; i < NUM_BLOCKS; i += 1) {
  const blockLength = Math.floor(800 + Math.random() * 200) // 800 ~ 1000
  const character = i % 2 === 0 ? 'a' : 'b' // 짝수 a, 홀수 b
  ws.write('a'.repeat(1024 * blockLength))

  numBlocksPerCharacter[character] += 1
}

console.log(numBlocksPerCharacter)
