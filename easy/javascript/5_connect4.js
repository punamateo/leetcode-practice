//13 min!!!!



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

const noWinnerGame = function(game){
    game.play(0)
    game.play(1)
    game.play(0)
    game.play(1)
    game.play(0)
    game.play(1)
    
    game.play(1)
    game.play(0)
    game.play(1)
    game.play(0)
    game.play(1)
    game.play(0)

    game.play(2)
    game.play(3)
    game.play(2)
    game.play(3)
    game.play(2)
    game.play(3)
    
    game.play(3)
    game.play(2)
    game.play(3)
    game.play(2)
    game.play(3)
    game.play(2)

    game.play(4)
    game.play(5)
    game.play(4)
    game.play(5)
    game.play(4)
    game.play(5)
    
    game.play(5)
    game.play(4)
    game.play(5)
    game.play(4)
    game.play(5)
    game.play(4)

    game.play(6)
    game.play(6)
    game.play(6)
    game.play(6)
    game.play(6)
    game.play(6)
}

class Connect4 {
    constructor(rows=6, cols=7) {
        this.rows = rows;
        this.cols = cols;
        this.player1= "A";
        this.player2="B";
        this.currentPlayer = this.player1;
        this.board = Array.from({length:this.rows}, () => {Array(this.cols).fill(".")});
    }

        showBoard(){
            console.table(this.board);
        }

        play(col) {

            if(this.board[0][col] !== "." ) throw new Error("Col is full");
            
            let assignedRow = null;
            for(let i=this.rows-1 ;i>=0;i--) {
                if(this.board[i][col] == ".") {
                    assignedRow=i;
                    this.board[i][col]= this.currentPlayer;
                    break;
                }
            }

            if(this.hasWon(assignedRow,col)) {
                console.log(`Player ${this.currentPlayer} has won!`);
            }

            this.currentPlayer = this.currentPlayer == this.player1 ? this.player2 : this.player1;
        }

        hasWon(row, col) {
            const winS = this.currentPlayer.repeat(4);
            
            let h = [];
            for (let i=-3;i<=3;i++) {
                const currentCol = col +i;
                if(currentCol>=0 && currentCol < this.cols) {
                    h.push(this.board[row][currentCol]);
                }
            }

            if(h.join("").includes(winS)) {
                return true;
            }

            
            let v = [];
            for (let i=-3;i<=3;i++) {
                const currentRow = row +i;
                if(currentRow>=0 && currentRow < this.rows) {
                    v.push(this.board[currentRow][col]);
                }
            }

            if(v.join("").includes(winS)) {
                return true;
            }


            let ad = [];
            for (let i=-3;i<=3;i++) {
                const currentRow = row - i;
                const currentCol = col + i;
                if(currentRow>=0 && currentRow < this.rows && currentCol >=0 && currentCol < this.cols) {
                    ad.push(this.board[currentRow][currentCol]);
                }
            }

            if(ad.join("").includes(winS)) {
                return true;
            }

            let dd = "";
            for (let i=-3;i<=3;i++) {
                const currentRow = row + i;
                const currentCol = col + i;
                if(currentRow>=0 && currentRow < this.rows && currentCol >=0 && currentCol < this.cols) {
                    dd = dd + this.board[currentRow][currentCol];
                }
            }

            if(dd.includes(winS)) {
                return true;
            }

        }
    
}


let game = new Connect4();
game.showBoard()