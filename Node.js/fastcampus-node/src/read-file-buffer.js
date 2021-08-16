// @ts-check

const { log } = console

const fs = require('fs')

const data = fs.readFileSync('local/big-file', 'utf-8')

/** @type {Object.<string, number>} */
const numBlocksPerCharacter = {
  a: 0,
  b: 0,
}

/** @type {string | undefined} */
let prevCharacter

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

log('blockCount', numBlocksPerCharacter)
