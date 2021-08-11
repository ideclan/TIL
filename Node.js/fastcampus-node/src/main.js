// @ts-check

const http = require('http')
const { routes } = require('./api')

const server = http.createServer((req, res) => {
  async function main() {
    const route = routes.find(
      (_route) =>
        req.url &&
        req.method &&
        _route.url.test(req.url) &&
        _route.method === req.method
    )

    if (!route) {
      res.statusCode = 404
      res.end('Not found.')
      return
    }

    const result = await route.callback()
    res.statusCode = result.statusCode
    res.end(result.body)
  }

  main()
})

const PORT = 3000

server.listen(PORT, () => {
  console.log(`The server is listening at port: ${PORT}`)
})
