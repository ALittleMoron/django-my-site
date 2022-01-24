function show_all() {
    let tables = document.querySelectorAll('.tblDiv')
    let lst = document.querySelectorAll('tr')
    tables.forEach(table => {table.style.display=''})
    lst.forEach(ev => {ev.style.display=''})

}


function hide_not_recommened(lst) {
    lst.forEach(ev => {
        if (ev.innerText.slice(-4).indexOf('Нет') != -1){
            ev.style.display = 'none'
        }

        else if (ev.innerText.slice(-4).indexOf('Да') != -1){
            ev.style.display = ''
        }
    })
}


function hide_recommend(lst) {
    lst.forEach(ev => {
        if (ev.innerText.slice(-4).indexOf('Да') != -1){
            ev.style.display = 'none'
        }

        else if (ev.innerText.slice(-4).indexOf('Нет') != -1){
            ev.style.display = ''
        }
    })
}


function all_trs_are_hidden(sequence) {
    for (let index = 1; index < sequence.length; index++) {
        if(sequence[index].style.display == ''){
            return false
        };
    }
    return true
}


function hide_empty_tables(){
    const tablesWithDiv = document.querySelectorAll('.tblDiv')
    tablesWithDiv.forEach(table => {
        let trs = table.querySelectorAll('tr')
        if (all_trs_are_hidden(trs)){
           table.style.display = 'none'
        }
    })
}


document.querySelector('#filter').addEventListener('click', function(e){
    if (e.target){
        const trs = document.querySelectorAll('tr')
        
        if(e.target.id == 'IRecommendRadio1'){show_all()}
        else if (e.target.id == 'IRecommendRadio2'){
            show_all()
            hide_not_recommened(trs)
            hide_empty_tables()
        }
        else if (e.target.id == 'IRecommendRadio3'){
            show_all()
            hide_recommend(trs)
            hide_empty_tables()
        }
    }
});