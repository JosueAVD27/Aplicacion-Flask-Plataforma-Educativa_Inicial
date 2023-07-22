const fs = require('fs');

const json_usuarios = JSON.stringify(listaPrueba)

fs.writeFileSync('static/database/Usuarios.json', json_usuarios, 'utf-8')