//27min
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


const ascendingDiagonalGame = function(game){
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

const descendingDiagonalGame = function(game){
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


    createBoard(rows, cols) {
        let board = [];
        for(let i =0; i<rows;i++) {
            board.push([]);

            for(let j=0; j<cols;j++) {
                board[i].push(".");
            }
        };
        return board;
    }

    showBoard() {
        console.table(this.board);
    }

    play(col) {
        
        if(this.board[0][col] !== ".") {
            throw new Error("Col is full")
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
            console.log(`Player ${this.currentPlayer} has won!`)
        }

        if(this.currentPlayer == this.player1) {
            this.currentPlayer = this.player2;
        } else {
            this.currentPlayer = this.player1;
        }

    }


    hasWon(row, col) {

        const winningString = Array(4).fill(this.currentPlayer).join("");
        const startRow = row -3;
        const startCol = col- 3;
        const endRow = row +3;
        const endCol = col + 3;

        //h
        let h = [];
        for (let i=startCol;i<=endCol;i++){
            if(i >=0 && i < this.cols) {
                h.push(this.board[row][i]);
            }
        }

        if(h.join("").includes(winningString)) {
            return true;
        }

        //v

        let v = [];
        for (let i=startRow;i<=endRow;i++){
            if(i >=0 && i < this.rows) {
                v.push(this.board[i][col]);
            }
        }


        if(v.join("").includes(winningString)) {
            return true;
        }

        //ad

        let ad = [];
        for (let i=0;i<=7;i++){
            const currentRow = endRow - i;
            const currentCol = startCol + i;
            if(currentRow >=0 && currentRow < this.rows && currentCol >=0 && currentCol < this.cols) {
                ad.push(this.board[currentRow][currentCol]);
            }
        }


        if(ad.join("").includes(winningString)) {
            return true;
        }


        //dd

        let dd = [];
        for (let i=0;i<=7;i++){
            const currentRow = endRow + i;
            const currentCol = startCol + i;
            if(currentRow >=0 && currentRow < this.rows && currentCol >=0 && currentCol < this.cols) {
                dd.push(this.board[currentRow][currentCol]);
            }
        }


        if(ad.join("").includes(winningString)) {
            return true;
        }
    }
}


game = new Connect4();


descendingDiagonalGame(game)
game.showBoard()
