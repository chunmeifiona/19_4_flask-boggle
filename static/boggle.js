class BoggleGame {
    constructor(boardId, secs = 60) {
        this.secs = secs
        this.board = $("#" + boardId)
        this.score = 0
        this.words = new Set();

        this.timer = setInterval(this.myTimer.bind(this), 1000)
        $(".add-word", this.board).on("submit", this.handleSubmit.bind(this))
    }
    showMsg(msg, cls) { // add ok and err class to msg
        $('.msg', this.board).text(msg).addClass(`msg ${cls}`)
    }
    showScore() {
        $('.score', this.board).text(this.score)
    }
    showTimer() {
        $('.timer', this.board).text(this.secs)
    }
    showWords(word) {
        $('.words', this.board).append($("<li>", { text: word }))
    }
    async handleSubmit(evt) {
        evt.preventDefault()
        console.log("handleSubmit")
        const $word = $(".guess_word", this.board)
        let word = $word.val()

        if (!word)
            return
        else if (this.words.has(word)) {
            this.showMsg(`${word} is already added. `, "err")
            $word.val("")
            return
        }

        const res = await axios.get("/valid", { params: { guess_word: word } })
        console.log(res)
        if (res.data.result === 'not-on-board')
            this.showMsg(`${word} is not a valid word on this board`, "err")
        else if (res.data.result === 'not-word')
            this.showMsg(`${word} is not a valid word`, "err")
        else {   //res.data.result === 'ok'
            this.showWords(word)
            this.showMsg(`${word} is a valid word. Added!`, "ok")
            this.words.add(word)
            this.score = this.score + word.length
            this.showScore()
        }

        $word.val("")
    }

    async myTimer() {
        this.secs = this.secs - 1
        this.showTimer()

        if (this.secs === 0) {
            clearInterval(this.timer)
            $(".add-word", this.board).hide()
            await this.endGame()
        }
    }

    async endGame() {
        const res = await axios.post("/endgame", { score: this.score })
        console.log(res)
    }


}
//