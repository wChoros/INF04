import { Router } from "express";
import path from 'path'
import fs from 'fs'

const router = Router()
const booksPath = path.join(import.meta.dirname, "../data/books.json")

router.get('/books/', (req, res) => {
    res.sendFile(booksPath)
})

router.get('/books/:id', (req, res) => {
    fs.readFile(booksPath, (err, data) => {
        if (err) throw err;
        const books = JSON.parse(data);
        let book = books[0]
        try {
            book = books[parseInt(req.params.id) - 1]
            if (book) {
                res.send(book)
            }
            else {
                res.status(404)
                res.send({ "code": 404, "message": "not found" })
            }
        }
        catch {

        }
    });
})

router.post('/books/', (req, res) => {
    const { title, author, year } = req.body;

    if (!title || !author || !year) {
        return res.status(400).send({ message: "bad request" });
    }
    fs.readFile(booksPath, (err, data) => {
        if (err) throw err;
        const books = JSON.parse(data);
        console.log(books)
        console.log(books)

        books.push({ id: books.length + 1, title, author, year })

        fs.writeFile(booksPath, JSON.stringify(books, null, 4), "utf8", (err) => {
            if (err) {
                console.error(err);
                return res.status(500).send({ message: "file write error" });
            }
            res.status(200).send({ status: "success" });
        });
    });
    
});

export default router;