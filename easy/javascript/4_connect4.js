//21 min

const horizontalGame = function(game){
    game.play(1)
    game.play(2)
    game.play(6)
    game.play(5)
    game.play(0)
    game.play(3)
    game.play(1)
    game.play(2)
    game.play(6)
    game.play(4)
}


const verticalGame = function(game){
    game.play(1)
    game.play(2)
    game.play(1)
    game.play(2)
    game.play(1)
    game.play(4)
    game.play(5)
    game.play(5)
    game.play(1)
 
}

const descendingDiagonalGame = function(game){
    game.play(1)
    game.play(2)
    game.play(6)
    game.play(5)
    game.play(0)
    game.play(3)
    game.play(1)
    game.play(2)
    game.play(6)
    game.play(4)
    game.play(0)
    game.play(1)
    game.play(0)
    game.play(0)

}

const ascendingDiagonalGame = function(game){
    game.play(1)
    game.play(2)
    game.play(6)
    game.play(5)
    game.play(2)
    game.play(6)
    game.play(4)
    game.play(3)
    game.play(4)
    game.play(3)
    game.play(4)
    game.play(5)
    game.play(3)
    game.play(5)
    game.play(4)
}

class Connect4 {
    constructor(rows=6,cols=7) {
        this.rows = rows;
        this.cols = cols;
        this.player1 = "X";
        this.player2 = "O";
        this.currentPlayer = this.player1;
        this.board = this.createBoard(this.rows,this.cols);
    }

    createBoard(rows,cols) {
        let board = [];
        for (let i = 0; i<rows;i++) {
            board.push( Array(cols).fill("."));
        }
        return board;
    }

    showBoard(){
        console.table(this.board)
    }

    play(col) {

        if(this.board[0][col] !== ".") {
            throw new Error("Row is full");
        }

        let assignedRow = null;
        for(let i=this.rows-1; i>=0; i--) {
            if(this.board[i][col] == ".") {
                this.board[i][col] = this.currentPlayer;
                assignedRow = i;
                break;
            }
        }

        if(this.hasWon(assignedRow,col)) {
            console.log(`Player ${this.currentPlayer} has won`);
            this.showBoard()

        }

        if(this.currentPlayer == this.player1) {
            this.currentPlayer = this.player2;
        } else {
            this.currentPlayer = this.player1;
        }
    }

    hasWon(row, col) {

        //h
        const winningArray = Array(4).fill(this.currentPlayer).join("");
        const startRow = row -3;
        const startCol= col-3;
        const endRow = row+3;
        const endCol = col+3

        let h = [];
        for(let i=0; i<7; i++) {
            const currentCol= startCol+i;
            if(currentCol >= 0 && currentCol <= this.cols) {
                h.push(this.board[row][currentCol])
            }
        }

        if(h.join("").includes(winningArray)){
            return true;
        }
        //v

        let v = [];
        for(let i=0; i<7; i++) {
            const currentRow = startRow+i;
            if(currentRow >= 0 && currentRow < this.rows) {
                v.push(this.board[currentRow][col])
            }
        }

        if(v.join("").includes(winningArray)){
            return true;
        }
        //ad
        let ad = [];
        for(let i=0; i<7; i++) {
            const currentRow= startRow-i;
            const currentCol = startCol+i;
            if(currentRow >= 0 && currentRow < this.rows && currentCol >=0 && currentCol < this.cols) {
                ad.push(this.board[currentRow][currentCol]);
            }
        }

        if(ad.join("").includes(winningArray)){
            return true;
        }
        //dd

        let dd = [];
        for(let i=0; i<7; i++) {
            const currentRow= startRow+i;
            const currentCol = startCol+i;
            if(currentRow >= 0 && currentRow < this.rows && currentCol >=0 && currentCol < this.cols) {
                dd.push(this.board[currentRow][currentCol]);
            }
        }

        if(dd.join("").includes(winningArray)){
            return true;
        }
    }
}


let game = new Connect4();
// horizontalGame(game);
// verticalGame(game)
// ascendingDiagonalGame(game)
descendingDiagonalGame(game)
game.showBoard()
