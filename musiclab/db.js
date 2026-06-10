export const CREATE_SONGS_TABLE = `CREATE TABLE IF NOT EXISTS songs (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        title TEXT NOT NULL,
                                        artist TEXT NOT NULL,
                                        album TEXT,
                                        genre TEXT,
                                        year INTEGER
                                    )`;

export const SELECT_ALL = "SELECT * FROM songs";

export const SELECT_BY_ID = "SELECT * FROM songs WHERE id = ?";

export const SELECT_BY_TITLE = "SELECT * FROM songs WHERE LOWER(title) LIKE LOWER(?)";

export const SELECT_BY_ARTIST = "SELECT * FROM songs WHERE LOWER(artist) LIKE LOWER(?)";

export const INSERT_SONG = "INSERT INTO songs (title, artist, album, genre, year) VALUES (?, ?, ?, ?, ?)";

export const UPDATE_SONG = "UPDATE songs SET title = ?, artist = ?, album = ?, genre = ?, year = ? WHERE id = ?";

export const DELETE_SONG = "DELETE FROM songs WHERE id = ?";