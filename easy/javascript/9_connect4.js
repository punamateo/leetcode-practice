
//10 min!
const horizontalGame = function(game){

    let h = [1,2,6,5,0,3,1,2,6,4]
}


const verticalGame = function(game){
 
    let v = [1,2,1,2,1,4,5,5,1]
}

const descendingDiagonalGame = function(game){
    let dd=[1,2,6,6,0,6,1,2,6,4,0,1,0,0,0,3]

}

const ascendingDiagonalGame = function(game){

    let ad = [1,2,6,5,2,6,4,3,4,3,4,5,3,5,4]
}

const noWinnerGame = function(game){

    let nw = [0,1,0,1,0,1,1,0,1,0,1,0,2,3,2,3,2,3]

}


class Connect4 {
    constructor(rows=6, cols=7) {
        this.rows = rows;
        this.cols = cols;
        this.player1 = 'A';
        this.player2 = 'B';
        this.currentPlayer = this.player1;
        this.winner = 0;
        this.board = Array.from({length: this.rows}, () => Array(this.cols).fill("."));
    }

    showBoard() {
        console.table(this.board);
    }

    play(col) {
        if(this.board[0][col] !== ".") throw new Error("Col is full");

        let assignedRow = null;
        for(let i = this.rows -1; i>=0;i--) {
            if(this.board[i][col] == "."){
                assignedRow = i;
                this.board[i][col] = this.currentPlayer;
                break;
            }
        }

        if(this.hasWon(assignedRow, col)) {
            console.log(`${this.currentPlayer} wins!`);
            this.winner = this.currentPlayer == this.player1 ? 1: 2 ;
        }

        this.currentPlayer = this.currentPlayer == this.player1 ? this.player2 : this.player1;


    }

    hasWon(row, col) {

        const WinS = this.currentPlayer.repeat(4);

        let h =[];

        //h
        for(let i = -3; i<=3; i++) {
            let curCol = col + i;
            if(curCol >=0 && curCol < this.cols) {
                h.push(this.board[row][curCol]);
            }
        }

        if(h.join("").includes(WinS)) return true;


        let v = [];
        for(let i = -3; i<=3; i++) {
            let curRow = row + i;
            if(curRow >=0 && curRow < this.rows) {
                v.push(this.board[curRow][col]);
            }
        }

        if(v.join("").includes(WinS)) return true;

        //ad
        let ad = [];
        for(let i = -3; i<=3; i++) {
            let curRow = row - i;
            let curCol = col +i;
            if(curRow >=0 && curRow < this.rows && curCol >=0 && curCol < this.cols) {
                ad.push(this.board[curRow][curCol]);
            }
        }

        
        if(ad.join("").includes(WinS)) return true;

        //d

        let dd = [];
        for(let i = -3; i<=3; i++) {
            let curRow = row + i;
            let curCol = col + i;
            if(curRow >=0 && curRow < this.rows && curCol >=0 && curCol < this.cols) {
                ad.push(this.board[curRow][curCol]);
            }
        }

        if(dd.join("").includes(WinS)) return true;
    }
}

let game = new Connect4();

verticalGame(game)
game.showBoard()
console.log(game.winner)


for(let i=0;i<moves.length;i++){
    game.play(moves[i])
}