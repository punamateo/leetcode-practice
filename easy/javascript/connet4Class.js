
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
    constructor(rows=6, cols=7) {
        this.rows = rows;
        this.cols = cols;
        this.player1 = "A";
        this.player2 = "B";
        this.currentPlayer = this.player1;
        this.board = this.createBoard(this.rows, this.cols);
    }

    createBoard(rows,cols) {
        let board = [];
        for (let i=0; i<rows;i++) {
            board.push([]);
            for(let j=0; j< cols; j++) {
                board[i].push(".");
            }
        }
        return board;
    }

    showBoard() {
        console.table(this.board);
    }

    play(col) {


        if(col >= this.cols) {
            throw new Error("Invalid move");
        }

        if(this.board[0][col] !== ".") {
            throw new Error("Row is full");
        }

        let row = -1;
        for(let i=this.rows-1;i>=0;i--) {
            if(this.board[i][col]== ".") {
                this.board[i][col] = this.currentPlayer;
                row = i;
                break;
            }
        }

        if(this.hasWon(row, col)){
            console.log(`Player ${this.currentPlayer} has won!`);
        }

        if(this.currentPlayer == this.player1) {
            this.currentPlayer = this.player2;
        } else {
            this.currentPlayer = this.player1;
        }

    }

    hasWon(row, col) {

        const isEqual = (array1, array2) => {
            array1.length == array2.length && array1.every((val,index) => val == array2[index]);
        };

        let winningArray = Array(4).fill(this.currentPlayer);

        let startRow = row - 3;
        let startCol = col -3;
        let endRow = row + 3;
        let endCol = col + 3;

        let horizontal = [];

        for (let i=startCol; i<=endCol;i++) {
            if(i >=0 && i <= this.cols -1) {
                horizontal.push(this.board[row][i]);
            }
        }

        if(horizontal.join("").includes(winningArray.join(""))) {
            return true;
        }


        let vertical = [];
        for(let i=startRow; i<=endRow;i++) {
            if (i >=0 && i <= this.rows -1) {
                vertical.push(this.board[i][col]);
            }
        }

        if(vertical.join("").includes(winningArray.join(""))) {
            return true;
        }

        let diagLength = Math.min(endRow - startRow, endCol - startCol);

        let ascendingDiagonal = [];
        for(let i=0; i < 7;i++) {
            const currentRow = endRow - i;
            const currentCol = startCol + i;
            if (currentRow >= 0 && currentRow <= this.rows -1 && currentCol >= 0 && currentCol <= this.cols -1) {
                ascendingDiagonal.push(this.board[currentRow][currentCol]);
            }
        }

        if(ascendingDiagonal.join("").includes(winningArray.join(""))) {
            return true;
        }

        let descendingDiagonal = [];
        for(let i=0; i < 7;i++) {
            const currentRow = startRow + i;
            const currentCol = startCol + i;
            if (currentRow >= 0 && currentRow <= this.rows -1 && currentCol >= 0 && currentCol <= this.cols -1) {
                descendingDiagonal.push(this.board[currentRow][currentCol]);
            }
        }

        if(descendingDiagonal.join("").includes(winningArray.join(""))) {
            return true;
        }
        return false;
    }

}

const game = new Connect4();

descendingDiagonalGame(game)


