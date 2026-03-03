//Connect4

var partidaDiagonalAscendente = function(tablero, jugador_1, jugador_2) {

    var currentPlayer = jugador_1;

    playOneMove(tablero, 0, jugador_1);
    playOneMove(tablero, 1, jugador_2);
    playOneMove(tablero, 1, jugador_1);
    playOneMove(tablero, 0, jugador_2);
    playOneMove(tablero, 2, jugador_1);
    playOneMove(tablero, 2, jugador_2);
    playOneMove(tablero, 1, jugador_1);
    playOneMove(tablero, 3, jugador_2);
    playOneMove(tablero, 3, jugador_1);
    playOneMove(tablero, 3, jugador_2);
    playOneMove(tablero, 2, jugador_1);
    playOneMove(tablero, 0, jugador_2);
    playOneMove(tablero, 3, jugador_1);
    // playOneMove(tablero, 2, jugador_1);
    // playOneMove(tablero, 4, jugador_2);
    showTablero();


}

var partidaDiagonalDescendente = function(tablero, jugador_1, jugador_2) {

    var currentPlayer = jugador_1;

    playOneMove(tablero, 0, jugador_1);
    playOneMove(tablero, 1, jugador_2);
    playOneMove(tablero, 1, jugador_1);
    playOneMove(tablero, 0, jugador_2);
    playOneMove(tablero, 2, jugador_1);
    playOneMove(tablero, 4, jugador_2);
    playOneMove(tablero, 1, jugador_1);
    playOneMove(tablero, 5, jugador_2);
    playOneMove(tablero, 2, jugador_1);
    playOneMove(tablero, 6, jugador_2);
    playOneMove(tablero, 2, jugador_1);
    playOneMove(tablero, 0, jugador_2);
    playOneMove(tablero, 0, jugador_1);
    playOneMove(tablero, 4, jugador_2);
    playOneMove(tablero, 3, jugador_1);
    // playOneMove(tablero, 2, jugador_1);
    // playOneMove(tablero, 4, jugador_2);
    showTablero();


}




const COLS = 7;
const ROWS = 6;

const jugador_1 = 'A';
const jugador_2 = 'B';

var fillTablero = function(ROWS,COLS) {
    var tablero = Array(ROWS)

    for (var row = 0; row< ROWS;row++) {
        tablero[row] = Array(ROWS);
        for (var col = 0; col < COLS; col++)
        {tablero[row][col] = '.'}
    }

    return tablero;
}

var showTablero = function() {
    for (var row = 0; row < ROWS;row++) {
        console.log(tablero[row].join(' '))
    }
}

var checkWin = function(tablero, row, col, currentPlayer) {
    var winningString =  currentPlayer.repeat(4);
    var horizontal = tablero[row].join('');

    if (horizontal.includes(winningString)) {
        return true;
    }

    var vertical = [];

    for(var i = 0; i<tablero.length;i++) {
        vertical.push(tablero[i][col]);
    }

    vertical = vertical.join('');
    if (vertical.includes(winningString)) {
        return true;
    }

    var diagonalStartCoords = [row-3, col-3];
    var descendingDiagonal = [];

    for (var i = 0; i<6;i++) {
        var cur_row = diagonalStartCoords[0] + i;
        var cur_col = diagonalStartCoords[1] + i;
        if(cur_row >= 0 && cur_col>= 0 && cur_row <= tablero.length-1 && cur_col <= tablero[0].length-1) {
            descendingDiagonal.push(tablero[cur_row][cur_col])
        }
    }

    descendingDiagonal = descendingDiagonal.join('');

    if (descendingDiagonal.includes(winningString)) {
        return true;
    }

    var aDiagonalStartCoords = [row+3, col-3];
    var ascendingDiagonal = [];

    for (var i = 0; i<6;i++) {
        var cur_row = aDiagonalStartCoords[0] - i;
        var cur_col = aDiagonalStartCoords[1] + i
        if (cur_row >= 0 && cur_col >= 0 && cur_row <= tablero.length-1 && cur_col <= tablero[0].length-1) {
            ascendingDiagonal.push(tablero[cur_row][cur_col])
        }
    }

    ascendingDiagonal = ascendingDiagonal.join('');
    if (ascendingDiagonal.includes(winningString)) {
        return true;
    }
}


var playOneMove = function(tablero, col_i, current_player) {

    if (col_i < 0  || col_i >= COLS) {
        throw new Error("Invalid Move");
    }

    if (tablero[0][col_i] !== ".") {
        throw new Error("Columna llena");
    }

    var row = 0;
    for (var row_i = 0; row_i < ROWS; row_i++) {
        if(tablero[row_i][col_i] == "." ){
            if(row_i == ROWS-1) {
                tablero[row_i][col_i] = current_player;
                row = row_i;
                break;
            }
            if(tablero[row_i+1][col_i] !== ".") {
                tablero[row_i][col_i] = current_player;
                row = row_i;
                break;
            }
        }      
    }

    const hasWon = checkWin(tablero, row, col_i, current_player)

    if (hasWon) {
        console.log(`${current_player} has won`);
    }
}

var partida = function(tablero, jugador_1, jugador_2) {

    var currentPlayer = jugador_1;

    playOneMove(tablero, 0, jugador_1);
    playOneMove(tablero, 1, jugador_2);
    playOneMove(tablero, 1, jugador_1);
    playOneMove(tablero, 0, jugador_2);
    playOneMove(tablero, 2, jugador_1);
    playOneMove(tablero, 2, jugador_2);
    playOneMove(tablero, 1, jugador_1);
    playOneMove(tablero, 3, jugador_2);
    playOneMove(tablero, 3, jugador_1);
    playOneMove(tablero, 3, jugador_2);
    playOneMove(tablero, 2, jugador_1);
    playOneMove(tablero, 0, jugador_2);
    playOneMove(tablero, 3, jugador_1);
    // playOneMove(tablero, 2, jugador_1);
    // playOneMove(tablero, 4, jugador_2);
    showTablero();


}


var tablero = fillTablero(ROWS,COLS);

partidaDiagonalDescendente(tablero,jugador_1, jugador_2);
