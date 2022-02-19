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


function statusChecks(){
    const checks = document.querySelector('#statusChecks').querySelectorAll('input');
    const table_divs = document.querySelectorAll('.tblDiv')
    var count = 0;

    for (const check of checks){
        var label = check.nextElementSibling.textContent.split(' ').filter(
            function x(y){return ['', '\n'].indexOf(y) == -1}
        ).join(' ').replaceAll('\n', '');
        var needed_div;

        for (let i = 0; i < table_divs.length; i++){
            var temp_h5 = table_divs[i].querySelector('h5').innerText
            if (temp_h5 == label){
                needed_div = table_divs[i];
                break;
            }
        }

        if (check.checked){
            needed_div.style.display = '';
        } else {
            count++
            needed_div.style.display = 'none';
        }
        if (count == 6){show_all()}
    }

    count = 0;
}

document.querySelector('#filter').addEventListener('click', function(e){
    const flex_arr = ['flexCheck1', 'flexCheck2', 'flexCheck3', 'flexCheck4', 'flexCheck5', 'flexCheck6']
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
        else if(flex_arr.indexOf(e.target.id) != -1){
            statusChecks()
        }
    }
})