// @ts-check

/* eslint-disable no-console */

const express = require('express')

const app = express()
app.use(express.json())
app.set('views', 'src/views')
app.set('view engine', 'pug')

const userRouter = require('./routes/users')

app.use('/users', userRouter)
app.use('/public', express.static('src/public'))

app.use((err, req, res, next) => {
  res.statusCode = err.statusCode || 500
  res.send(err.message)
})

module.exports = app
