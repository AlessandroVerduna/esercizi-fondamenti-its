import express from 'express';
import { db } from '../server.js';
import { SELECT_ALL, SELECT_BY_ID, SELECT_BY_TITLE, SELECT_BY_ARTIST,
    INSERT_SONG, UPDATE_SONG, DELETE_SONG } from '../db.js';

const libriRouter = express.Router();

// | `GET`    | `/songs`          | Recupera tutti i brani                   |
// | `GET`    | `/songs?title=..` | Filtra per titolo (query param)          |
// | `GET`    | `/songs?artist=..`| Filtra per artista (query param)         |
libriRouter.get("/", (req, res) => {
    const title = req.query.title;
    const artist = req.query.artist;

    if (artist) {
            console.log(`GET /api/v2/songs?artist=${artist}`)
            db.all(SELECT_BY_ARTIST, [artist], (err, rows) => {
                if (err) {
                    res.status(500).json({ error: err.message });
                    return;
                }
                res.json(rows);
            });
    } else if (title) {
        console.log(`GET /api/v2/songs?title=${title}`)
        db.all(SELECT_BY_TITLE, [title], (err, rows) => {
            if (err) {
                res.status(500).json({ error: err.message });
                return;
            }
            res.json(rows);
        });
    } else {
        console.log("GET /api/v2/songs")
        db.all(SELECT_ALL, [], (err, rows) => {
            if (err) {
                res.status(500).json({ error: err.message });
                return;
            }
            res.json(rows);
        });
    }
});

// | `GET`    | `/songs/:id`      | Recupera un brano specifico              |
libriRouter.get("/:id", (req,res) => {
    console.log(`GET /api/v2/songs/${req.params.id}`);

    db.get(SELECT_BY_ID, [req.params.id], (err, row) => {
        if (err) {
            res.status(500).json({ erro: err.message });
        } else if (row) {
            res.json(row);
        } else {
            res.status(404).json({ error: "Canzone non trovata" });
        }
    });
});

// | `PUT`    | `/songs/:id`      | Modifica un brano (sostituzione completa)|
libriRouter.put("/:id", (req,res) => {
    console.log(`PUT /api/v2/songs/${req.params.id}`);

    const errorMessage = validaLibro(req.body);
    if (errorMessage) {
        res.status(400).json({ error: errorMessage });
        return;
    }
    const id = req.params.id;
    const { title, artist, album, genre, year } = req.body;

    db.run(UPDATE_SONG, [title, artist, album, genre, year, id], function(err) {
        if (err) {
            res.status(500).json({ error: err.message });
        } else if (this.changes > 0) {
            res.json({ message: "Libro aggiornato con successo" });
        } else {
            res.status(404).json({ error: "Libro non trovato" });
        }    
    });
});

// | `POST`   | `/songs`          | Aggiunge un nuovo brano                  |
libriRouter.post("/", (req,res) => {
    console.log("POST /api/v2/songs");
    // controllo che il body esista
    const errorMessage = validaLibro(req.body);
    if (errorMessage) {
        res.status(400).json({ error: errorMessage });
        return;
    }

    // estraggo le proprietà del body
    const { title, artist, album, genre, year } = req.body;
    db.run(INSERT_SONG, [title, artist, album, genre, year], function(err) {
        if (err) {
            res.status(500).json({ error: err.message });
        } else {
            res.status(201).json({ message: `Libro inserito con ID ${this.lastID}` });
        }
    })    
});

// | `DELETE` | `/songs/:id`      | Rimuove un brano                         |
libriRouter.delete("/:id", (req,res) => {
    const id = req.params.id; 
    console.log(`DELETE /api/v2/songs/${id}`);

    db.run(DELETE_SONG, [id], function(err) {
        if (err) {
            res.status(500).json({ error: err.message });
        } else if (this.changes === 0) {
            res.status(404).json({ message: "Canzone non presente in database" });
        } else {
            res.status(200).json({ message: "Canzone canecellata con successo" });
        }
    });
});

function validaLibro(libro) {
    let errorMessage;

    if (!libro) {
       errorMessage = "Libro non presente";
    } else if (libro.numero_pagine && isNaN(libro.numero_pagine)) {
       errorMessage = "Il numero di pagine deve essere un numero";
    }

    return errorMessage;
};

export default libriRouter;