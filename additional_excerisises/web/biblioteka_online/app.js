import express from 'express'
import path from 'path'
import booksRouter from './routes/booksRouter.js'
import infoRouter from './routes/infoRouter.js'
const app = express()


app.use(express.json());
app.use('/', booksRouter)
app.use('/', infoRouter)
app.use(express.static('public'))

app.listen(4001)