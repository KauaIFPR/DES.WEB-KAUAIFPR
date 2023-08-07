let yAtor = 366;
let xAtor = 85;
let colisao = false;
let meusPontos = 0;
let vidas = 3;

function mostraAtor (){
  image(imagemDoAtor, xAtor, yAtor, 30, 30); 
}

function movimentaAtor(){
  if (keyIsDown (UP_ARROW)){
    yAtor -= 3;
  }
  if (keyIsDown (DOWN_ARROW)){
    if (yAtor < 366){
      yAtor += 3;
    }
  }

  if(keyIsDown (LEFT_ARROW)) {
    if(xAtor > 0){
      xAtor -= 3;
    }
  }
  if(keyIsDown (RIGHT_ARROW)) {
    if(xAtor < 475){
      xAtor += 3;
    }
  }
}

function verificaColisao (){
  for (let i = 0; i < imagemCarros.length; i++){
    colisao = collideRectCircle(xCarros[i], yCarros[i], comprimentoCarro, alturaCarro, xAtor, yAtor, 15)
    if(!colisao) colisao = collideRectCircle(xCarrosInvert[i], yCarrosInvert[i], comprimentoCarro, alturaCarro, xAtor, yAtor, 15)
    if(colisao){
      perdeVida();
    }
  }
}

function voltaAtorPosicaoInicial (){
  yAtor = 366;
  xAtor = 85;
}

function incluiPontos(){
  textAlign(CENTER);
  textSize(25);
  fill(color(255, 240, 60));
  text("Pontos: " + meusPontos, width / 5, 27);
}

function incluiVidas(){
  textAlign(CENTER);
  textSize(25);
  fill(color(255, 0, 0));
  text("Vidas: " + vidas, width / 2, 27);
}

function perdeVida(){
  voltaAtorPosicaoInicial();
  vidas -= 1;
  if(vidas <= 0){
    meusPontos = 0;
    vidas = 3;
  }
}

function marcaPonto(){
  if (yAtor < 15){
  meusPontos += 1;
  voltaAtorPosicaoInicial();  
  }
}

function pontosMaiorQueZero (){
  return meusPontos > 0;
}