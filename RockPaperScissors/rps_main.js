// Score and game logic
const game = () => {
    let playerScore = 0;
    let computerScore = 0;
    let moves = 0;
}

// Game buttons and Options logic
const playGame = () => {
    const rockBtn = document.getElementsByClassName('rockBtn');
    const paperBtn = document.getElementsByClassName('paperBtn');
    const scissorsBtn = document.getElementsByClassName('scissorsBtn');
    const playerOptions = [rockBtn, paperBtn, scissorsBtn];
    const computerOptions = [rockBtn, paperBtn, scissorsBtn];

    playerOptions.forEach(Option => {
        playerOptions.addEventLister ('click', function {
            const movesLeft = document.querySelector('.movesleft')
        })
    } );
}