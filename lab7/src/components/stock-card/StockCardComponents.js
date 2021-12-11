export class StockCardComponent {
    constructor(parent) {
        this.parent = parent;
    }
    getHTML(data) {
        return (
            `
                <div class="card" style="width: 300px;">
                    <img class="card-img-top" src="https://kuda-sochi.ru/uploads/7a3c046e1230dc19840256889c33987d.jpg" alt="картинка">
                    <div class="card-body">
                        <h5 class="card-title">${data.company_name}</h5>
                        <p class="card-text">Рейтинг: ${data.price}</p>
                        <button class="btn btn-primary" id="click-card-${data.pk}" data-id="${data.pk}">Нажми на меня</button>
                    </div>
                </div>
            `
        )
    }
    addListeners(data, listener) {
        document
            .getElementById(`click-card-${data.pk}`)
            .addEventListener("click", listener)
    }

    render(data, listener) {
        const html = this.getHTML(data)
        this.parent.insertAdjacentHTML('beforeend', html)
        this.addListeners(data, listener)
    }
}