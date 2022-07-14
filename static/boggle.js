class BoggleGame {
    constructor(boardId, secs = 60) {
        this.secs = secs
        this.board = $("#" + boardId)

        $(".add-word", this.board).on("submit", this.handleSubmit.bind(this))


    }
    async handleSubmit(evt) {
        evt.preventDefault()
        console.log("handleSubmit")
        const res = await axios.get("/valid", { params: { guess_word: guess_word } })
        console.log(res)
    }

}
//