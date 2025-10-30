import { Router } from "express";
import path from 'path'
const router = Router()


router.get('/', (req, res) => {
  res.sendFile(path.join(import.meta.dirname, '../views/index.html'))
})

router.get('/about', (req, res) => {
  res.sendFile(path.join(import.meta.dirname, '../views/about.html'))
})

export default router