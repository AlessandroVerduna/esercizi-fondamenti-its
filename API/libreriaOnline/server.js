
import express from 'express';
import catalogoLibri from './model/catalogo.js';
import clienteFile from './model/clienti.js';
import bodyParser from 'body-parser';
import swaggerUi from 'swagger-ui-express';
import swaggerDocument from './doc/swagger.json' with {type: "json"};

const app = express();
app.use(bodyParser.json());
const PORT = 3000;
const BASE_PATH = "/api/v1";


//ar catalogo = catalogoLibri;
//var clienti = clienteFile;
var catalogo = [...catalogoLibri];
var clienti = [...clienteFile];
// creo una shallow copy dell'array clieni - libri per poterli modificare. prende 


// integro swaggerUi per la documentazione dell'API
app.use("/api-docs", swaggerUi.serve, swaggerUi.setup(swaggerDocument));

// avvio il server
app.listen(PORT, () => {
    console.log ("server attivo sulla porta " + PORT);
});

//endpoint che restituisce un endpoint 
app.get("/", (req, res) => {
    res.send("Benvenuto nella tua libreria online");
});

// endpoint per recuperare l'elenco fdei cataloghi libri. basta mod il path, non serve aggiornare le variabili
//app.get(BASE_PATH + "/libri", (req, res) => {
//    res.json(catalogo);
//});
// di seguito versione ottimizzata: meglio perchè non concatena due comendi ma li rende un'unica str
// e lo rende un'unico path anche concatenando più req 
app.get(`${BASE_PATH}/libri`, (req, res) => {
    res.json(catalogo);
});


// endpoint per recuperare l'elenco dei clienti
app.get(BASE_PATH + "/clienti", (req, res) => {
    res.json(clienti);
}); 

//recupera libro per titolo: /v1/catalogo/search?titolo=restful
//il path search va posizionato prima
app.get(`${BASE_PATH}/libri/search`, (req, res) =>{
    //recupero il parametro dall'url + pulizia
    let titoloParam = (req.query.titolo || "").toString().trim().toLowerCase();

    //se non c'è il parametro o è str vuota, restituisco stato 400(Bad Req)
    if (!titoloParam) return res.status(400).json({ error: "Parametro 'titolo' errato"});

    let results = catalogo.findLast(libro => libro.titolo.toLocaleLowerCase().includes(titoloParam));

    return res.json(results);
}

);

//ricerca con id
// let indica una vaiabile con visibilità interna a funz corrente
app.get(`${BASE_PATH}/libri/:id`, (req, res) => {
    let idParam = parseInt(req.params.id);

    let libroTrovato = catalogo.find(libro => libro.id === idParam);

    if (!libroTrovato) {
        res.status(404).json({ error: "Libro non trovato"});
    } else {
        res.json(libroTrovato);
    }

});

//necessita npm install body-parser
app.post(`${BASE_PATH}/libri`, (req, res) => {
    const nuovoLibro = req.body;

    if (!validaLibro(nuovoLibro) ) {
        res.status(400).json({ error: "Nessun dato fornito" });
        return;
    }
    
    // assegno un id univoco; normalmente questa operazione la farebbe il database sottostante
    const maxId = catalogo.map(item => item.id).reduce((a, b) => Math.max(a, b), 0);
    nuovoLibro.id = maxId + 1;

    
    catalogo.push(nuovoLibro);
    return res.status(201).json({ message: "Libro aggiuntocon successo" });
});


app.delete(`${BASE_PATH}/libri/:id`, (req, res) => {
    //recupero id del libro da eliminare dal path e lo converto in numero
    const idParam = parseInt(req.params.id);

    //cerco nelcatalogo index elemento corrispondente
    


});

app.put(`${BASE_PATH}/libri/:id`, (req, res) => {
    const idParam = parseInt(req.params.id);
    //recupero il libro aggiornato dalla request
    let libroAggiornato = req.body;
    
    //controllo che il libro sia valido
    if (!validaLibro(libroAggiornato)) {
        return res.status(400).json({error: 'libro non valido'});
        
    }    
    //recupero indice libro da aggiornare
    // normalmente basta passare l'id ad db per aggiornare il record
    const index = catalogo.findIndex(libro => libro.id === idParam);
    ///se non trova l'elemento restituisce errore
    if (index === -1) {
        return res.status(404).json({ error : 'Libro non trovato'});
        ;
    }

    let libroDaAggiornare = catalogo[index];

    /* l'uso dello spread operator (...) consente di creare un nuovo oggetto che
    aggiorna le proprieta esistenti di libroDaAggiornare con quelle contenute in libroAggiornato
    */
    catalogo[index] = {...libroDaAggiornare, ...libroAggiornato};

    res.json({ message: 'Libro aggiornato con successo'});
});


app.delete(`${BASE_PATH}/libri/:id`, (req, res) => {
    // recupero l'ID del libro da eliminare dal path e lo converto in numero
    const idParam = parseInt(req.params.id);
    console.log("riga 138");

    // cerco nel catalogo il libro corrispondente usando come parametro l'ID
    const index = catalogo.findIndex(libro => libro.id === idParam);

    console.log("riga 142");
    if (index === -1) {
        return res.status(404).json({ error: 'Libro non trovato' });
    }
    
    console.log("riga 147");
    catalogo.splice(index, 1);
    res.json({ message: 'Libro eliminato con successo' });

    // 
});

//----------------------------------------CLIENTI------------------------------------//

//clienti get con id
app.get(`${BASE_PATH}/clienti/:id`, (req, res) => {
    let idParam = parseInt(req.params.id);

    let clienteTrovato = clienti.find(cliente => cliente.id === idParam);

    if (!clienteTrovato) {
        res.status(404).json({ error: "Cliente non trovato"});
    } else {
        res.json(clienteTrovato);
    }

});

//post clienti

app.post(`${BASE_PATH}/clienti`, (req, res) => {
    const nuovoCliente = req.body;

    if (!validaCliente(nuovoCliente) ) {
        res.status(400).json({ error: "Nessun dato fornito" });
        return;
    }
    
    // assegno un id univoco; normalmente questa operazione la farebbe il database sottostante
    const maxId = clienti.map(item => item.id).reduce((a, b) => Math.max(a, b), 0);
    nuovoCliente.id = maxId + 1;

    
    clienti.push(nuovoCliente);
    return res.status(201).json({ message: "Cliente aggiunto con successo" });
});

// delete cliente
app.delete(`${BASE_PATH}/clienti/:id`, (req, res) => {
    
    const idParam = parseInt(req.params.id);
    //console.log("riga 138");

    // cerco nel catalogo il libro corrispondente usando come parametro l'ID
    const index = clienti.findIndex(cliente => cliente.id === idParam);

    //console.log("riga 142");
    if (index === -1) {
        return res.status(404).json({ error: 'Cliente non trovato' });
    }
    
    //console.log("riga 147");
    clienti.splice(index, 1);
    res.json({ message: 'Cliente eliminato con successo' });

    // 
});

//------------------------FUNZIONI--------------------------//

function validaLibro(libro) {
    //controlliamo che il libro esista e che abbia almeno titolo, autore e editore
    if (libro && libro.titolo && libro.autore && libro.editore){
        return true;
    } else {
        return false;
    }    
    };

function validaCliente(cliente) {
    //controlliamo che il libro esista e che abbia almeno titolo, autore e editore
    if (cliente && cliente.nome && cliente.cognome && cliente.eta){
        return true;
    } else {
        return false;
    }    
    };

