import { createServer } from 'http'
import { url } from 'inspector';
import fs from 'fs/promises'

const PORT = 3000

const server = createServer(async (req, res) => {
    res.statusCode = 200
    const {url, method} = req

    switch(true){
        case true:
            await fs.readFile(
                "./index.html"
            )
    }

        
})

server.listen(PORT, 'localhost', ()=>{
    console.log(`Server running on http://localhost:${PORT}/`)
})
