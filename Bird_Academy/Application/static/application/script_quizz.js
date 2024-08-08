let apiUserBird = '/api/user_birds/'
let apiSongBird = '/api/user_songs/'
let donneeUserBird = []
let donneSongBird = []
var mainElement = document.querySelector('.main')
var container = document.querySelector('.container')
var numberSpan = document.getElementById('number')
var currentNumber = 5 // Valeur par défaut
let maxNumber = 3 // Valeur par défaut au cas où la requête échoue

function updateNumber() {
  numberSpan.textContent = currentNumber
}

function nextNum() {
  if (currentNumber < maxNumber) {
    // Limite supérieure dynamique
    currentNumber++
  }
  updateNumber()
}

function prevNum() {
  if (currentNumber > 3) {
    // Limite inférieure
    currentNumber--
  }
  updateNumber()
}

// Initialisation de l'affichage
updateNumber()

fetch(apiUserBird)
    .then((response) => response.json())
    .then((data) => {
        donneeUserBird = data
        maxNumber = donneeUserBird.length > 0 ? donneeUserBird.length : maxNumber // Mettez à jour le maxNumber
        document.getElementById('maxQuizz').textContent = maxNumber

    if (donneeUserBird.length > 3) {
        updateNumber()
        } else {
        mainElement.innerHTML =
            "<p>Pas d'oiseau enregistré, veuillez en enregistrer sur la page . .. </p>"
        }
    })
    .catch((error) =>
        console.error('Erreur lors de la récupération des données:', error),
  )

fetch(apiSongBird)
    .then((response) => response.json())
    .then((data) => {
        donneSongBird = data
    })
    .catch((error) =>
        console.error('Erreur lors de la récupération des données:', error),
    )

let btnValider = document.getElementById('valider')
btnValider.addEventListener('click', entreeQuizz);

function entreeQuizz() {
    console.log(currentNumber)
    quizz(currentNumber)
    }

async function quizz(nbrTour) {
    mainElement.innerHTML = '<div class="audio"></div><div class="reponse"></div>';
    
    var audio = document.querySelector('.audio');
    var reponse = document.querySelector('.reponse');

    for (let i = 0; i < nbrTour; i++) {
        audio.innerHTML = ' ';
        reponse.innerHTML = ' ';
        await new Promise((resolve) => {
            while (true) {
                let index = Math.floor(Math.random() * donneeUserBird.length);
                let idBird = donneeUserBird[index];
                console.log(idBird);

                const filteredSongBirds = donneSongBird.filter(
                    (bird) => bird.Id_bird === idBird.id,
                );
                let song = filteredSongBirds[Math.floor(Math.random() * filteredSongBirds.length)];
                console.log(song);

                let engistrement = '<audio controls autoplay><source src="'
                + song.URL_Song
                + '" type="audio/mpeg">Votre navigateur ne supporte pas les fichiers audio.</audio>';

                audio.innerHTML = engistrement;

                setTimeout(() => {
                    let affichageResponse = '<span> ' + donneeUserBird[index].Fr_name + '</span>';

                    if (i != nbrTour - 1) {
                        affichageResponse += '<span><button id="nextButton">Suivant</button></span>';
                    } else {
                        affichageResponse += '<span><button onclick="location.reload()">Recommencer</button></span>';
                    }
                    reponse.innerHTML = affichageResponse;

                    let nextButton = document.getElementById('nextButton');
                    if (nextButton) {
                        nextButton.addEventListener('click', () => {
                            donneeUserBird.splice(index, 1); // Supprimer l'élément traité
                            resolve(); // Passer à l'itération suivante
                        });
                    }

                }, 10000);

                break; // Sortir de la boucle while pour attendre le clic du bouton
            }
        });
    }
}

    

console.log('res')
