// @ts-check

// aaaaaabbbbbbbaaaaaaabbbbbb...aaaaabbbbb
// 위와 같은 파일에서, a의 연속 구간(a block)의 개수와, b의 연속 구간(b block)의 개수를 세기

const { log } = console

const fs = require('fs')

const rs = fs.createReadStream('local/big-file', {
  encoding: 'utf-8',
  highWaterMark: 65536 * 4,
})

/** @type {Object.<string, number>} */
const numBlocksPerCharacter = {
  a: 0,
  b: 0,
}

/** @type {string | undefined} */
let prevCharacter
let chunkCount = 0

rs.on('data', (data) => {
  chunkCount += 1

  if (typeof data !== 'string') {
    return
  }

  for (let i = 0; i < data.length; i += 1) {
    if (data[i] !== prevCharacter) {
      const newCharacter = data[i]

      if (!newCharacter) {
        /* eslint-disable-next-line no-continue */
        continue
      }

      prevCharacter = newCharacter
      numBlocksPerCharacter[newCharacter] += 1
    }
  }
})

rs.on('end', () => {
  log('Event: end')
  log('blockCount', numBlocksPerCharacter)
  log('chunkCount', chunkCount)
})
