let xCarros = [600, 600, 600];
let xCarrosInvert = [-50, -50, -50];
let yCarros = [40, 96, 150];
let yCarrosInvert = [210, 270, 318];
let velocidadeCarros = [4, 3.5, 6.2];
let velocidadeCarrosInvert = [4, 3.5, 6.2];
let comprimentoCarro = 50;
let alturaCarro = 40;

function mostraCarro (){
  for (let i = 0; i < imagemCarros.length; i++){
    image(imagemCarros[i], xCarros[i], yCarros[i], comprimentoCarro, alturaCarro);
  }
  for (let i = 0; i < imagemCarros.length; i++){
    image(imagemCarrosInvert[i], xCarrosInvert[i], yCarrosInvert[i], comprimentoCarro, alturaCarro);
  }
}

function movimentaCarro (){
  for (let i = 0; i < xCarros.length; i++){
    xCarros[i] -= velocidadeCarros[i];
  }
  for (let i = 0; i < xCarrosInvert.length; i++){
    xCarrosInvert[i] += velocidadeCarrosInvert[i];
  }
}

function voltaPosicaoInicialDoCarro (){
  for (let i = 0; i < xCarros.length; i++){ 
    if (xCarros[i] < -50){
      xCarros[i] = 600
    }
 }
  for (let i = 0; i < xCarrosInvert.length; i++){ 
    if (xCarrosInvert[i] > 600){
      xCarrosInvert[i] = -50
    }
 }
}
