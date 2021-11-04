document.querySelector('#IRecommendCheck').addEventListener('click', function(){
    list = document.querySelector('tbody').querySelectorAll('tr')
    if (this.checked == true){
        list.forEach(e => {
            if (e.innerText.slice(-4).indexOf('Нет') != -1) {
                e.style = 'display: none;'
            }
        });
    }
    else {
        list.forEach(e => {
            e.style = ''
        })
    }
});