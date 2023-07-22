var programming_languages = [
  "hola",
  "mar",
  "sol",
  "luna",
  "cielo",
  "mano",
  "pie",
  "meta",
  "mani",
  "mora",
  "sopa",
  "plato",
  "letra",
  "loma"
]

let answer = '';
let maxWrong = 4;
let mistakes = 0;
let guessed = [];
let wordStatus = null;
let wordStatus1 = null;
const perder = document.getElementById('perder');
const no = `<img src = '../static/assets/Imagen/perder1.gif' id="img1">`
const ok = `<img src = '../static/assets/Imagen/ok.gif' id="img1">`
let audio = new Audio('../static/assets/Sonido/correcto.wav');
let audio1 = new Audio('../static/assets/Sonido/tecla.wav');
let audio2 = new Audio('../static/assets/Sonido/error.wav');
let audio3 = new Audio('../static/assets/Sonido/aplauso.wav');
audio2.volume = 0.2;
audio3.volume = 0.2;

function randomWord() {
  answer = programming_languages[Math.floor(Math.random() * programming_languages.length)];
}

function generateButtons() {
  let letras = (answer + 'wxyz');

  function barajar(array) {
    let posicionActual = array.length;

    while (0 !== posicionActual) {
      const posicionAleatoria = Math.floor(Math.random() * posicionActual);
      posicionActual--;
      //"truco" para intercambiar los valores sin necesidad de una variable auxiliar
      [array[posicionActual], array[posicionAleatoria]] = [
        array[posicionAleatoria], array[posicionActual]
      ];
    }
    return array;
  }

  function generarAleatorios(cantidad) {
    const caracteres = (answer + 'wxyz').split("");
    barajar(caracteres);
    return caracteres.slice(0, cantidad).join("")
  }

  let buttonsHTML = generarAleatorios(10).split('').map(letter =>
    `
      <button
        class="btn btn-lg btn-primary m-2" style="background-color: #6680E8 ; color: #063F56 ;font-size: 40px; ; width: 30% ;"
        id='` + letter + `'
        onClick="handleGuess('` + letter + `')"
      >
        ` + letter + `
      </button>
    `).join('');

  document.getElementById('keyboard').innerHTML = buttonsHTML;
}

function handleGuess(chosenLetter) {
  guessed.indexOf(chosenLetter) === -1 ? guessed.push(chosenLetter) : null;
  document.getElementById(chosenLetter).setAttribute('disabled', true);

  if (answer.indexOf(chosenLetter) >= 0) {
    guessedWord();
    checkIfGameWon();
    audio1.play();//tecla correcta
  } else if (answer.indexOf(chosenLetter) === -1) {
    mistakes++;
    var x = mistakes
    x = x * 25;
    var y = 100;
    w = y - x;
    updateMistakes();
    checkIfGameLost();
    updateHangmanPicture();
    const botonError = document.getElementById('a');
    botonError.className = 'botonRojo btn btn-lg btn-primary m-2';
    audio2.play();//tecla error
    document.getElementById('valorx').setAttribute('value',w);
  }
}

function updateHangmanPicture() {
  document.getElementById('hangmanPic').src = '../static/assets/Imagen/' + mistakes + '.jpg';
}

function checkIfGameWon() {
  if (wordStatus === answer) {
    //document.getElementById('keyboard').innerHTML = 'Acertaste!!!!!';
    audio.play(); //ganar
    perder.innerHTML = ok;
    document.getElementById('PEnviar').disabled = false;
    detenerse();
  }
}

function checkIfGameLost() {
  if (mistakes === maxWrong) {
    //document.getElementById('keyboard').innerHTML = 'Perdiste!!!';
    audio3.play(); //perder
    perder.innerHTML = no;
    detenerse();
  }
}


function guessedWord() {
  wordStatus1 = answer
  wordStatus = answer.split('').map(letter => (guessed.indexOf(letter) >= 0 ? letter : " _ ")).join('');
  document.getElementById('wordSpotlight').innerHTML = wordStatus1;
}

function updateMistakes() {
  document.getElementById('mistakes').innerHTML = mistakes;
  document.getElementById('valorx').setAttribute('value','100');
  
}

function reset() {
  mistakes = 0;
  guessed = [];
  perder.innerHTML = '';
  document.getElementById('PEnviar').disabled = true;

  document.getElementById('hangmanPic').src = '../static/assets/Imagen/0.jpg';
  
  randomWord();
  guessedWord();
  updateMistakes();
  generateButtons();
}

document.getElementById('maxWrong').innerHTML = maxWrong;

randomWord();
generateButtons();
guessedWord();