document.querySelector('#filter').addEventListener('click', function(e){
    list = document.querySelector('tbody').querySelectorAll('tr')
    if (e.target && e.target.id == 'IRecommendRadio1'){
        list.forEach(ev => {
            ev.style.display = ''
        })
    }
    else if (e.target && e.target.id == 'IRecommendRadio2'){
        list.forEach(ev => {
            ev.style.display = ''
        })
        list.forEach(ev => {
            if (ev.innerText.slice(-4).indexOf('Нет') != -1){
                ev.style.display = 'none'
            }

            else if (ev.innerText.slice(-4).indexOf('Да') != -1){
                ev.style.display = ''
            }
        })
    }
    else if (e.target && e.target.id == 'IRecommendRadio3'){
        list.forEach(ev => {
            ev.style.display = ''
        })
        list.forEach(ev => {
            if (ev.innerText.slice(-4).indexOf('Да') != -1){
                ev.style.display = 'none'
            }

            else if (ev.innerText.slice(-4).indexOf('Нет') != -1){
                ev.style.display = ''
            }
        })
    }
});