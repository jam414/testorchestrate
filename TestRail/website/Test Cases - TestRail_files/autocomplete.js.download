function autocomplete (input, data) { 
    data = JSON.parse(data);
    let currentFocus;
    let data_string = '';
    let update_data = [0, 0, ''];
    let element = document.getElementById(input);
    let lineHeight = 21;

    setTimeout(function () {
        increaseHeight();
    });

    element.addEventListener('input', function(e) {
        let a, b, i, val = this.value;
        closeAllLists();

        if (!val) return false;

        currentFocus = -1;
        a = document.createElement('div');
        a.setAttribute('id', this.id + 'autocomplete-list');
        a.setAttribute('class', 'autocomplete-items');
        this.parentNode.appendChild(a);

        for (item of data) {                
            let patt = /\s((?:%[a-z]?[^\s%]+%?))/igm;
            data_string = val;
            update_data = [0, 0, ''];
        
            while (match = patt.exec(val)) {
                if (match[1].match(/%$/i) == null) {
                    update_data = [match.index, patt.lastIndex, match[1]];
                }
            }

            if (update_data[2] != '' && (item.substr(0, update_data[2].length).toUpperCase() == update_data[2].toUpperCase())) {
                b = document.createElement('div');
                b.innerHTML = item;
                b.innerHTML += '<input type=\'hidden\' value=\'' + item + '\'>';

                b.addEventListener('click', function(e) {
                    let select_value = this.getElementsByTagName('input')[0].value;
                    let begin = data_string.substring(0, update_data[0] + 1);
                    let end = data_string.substring(update_data[1], data_string.length);
                    element.value = begin + select_value + end;
                    element.selectionEnd = update_data[0] + 1 + select_value.length;
                    closeAllLists();
                });

                a.appendChild(b);
            }
        }

    });

    element.addEventListener('focus', function(e) {
        element.parentNode.classList.add('focus');
    });

    element.addEventListener('blur', function(e) {
        element.parentNode.classList.remove('focus');
    });

    element.addEventListener('paste', function(e) {
        increaseHeight();
    });

    element.addEventListener('keydown', function(e) {        
        let list = document.getElementById(this.id + 'autocomplete-list');

        if (list) {
            list = list.getElementsByTagName('div');
        }        

        if (e.keyCode == 40) {
            if (list && list.length) e.preventDefault();

            currentFocus++;
            addActive(list);
        } else if (e.keyCode == 38) {
            if (list && list.length) e.preventDefault();

            currentFocus--;
            addActive(list);
        } else if (e.keyCode == 86) {
            increaseHeight();
        } else if (e.keyCode == 8) {
            decreaseHeight();
        } else if (e.keyCode == 46) {
            decreaseHeight();
        } else if (e.keyCode == 13) {
            e.preventDefault();

            if (hasNoOneActive(list)) {
                let start = element.value.substring(0, element.selectionStart) + "\n";
                let end = element.value.substr(element.selectionStart);
                element.value = start + end;
                element.selectionStart = element.selectionEnd = start.length;
                increaseHeight();
            } else if (currentFocus > -1) {
                if (list) list[currentFocus].click();
            }
        }
    });

    function increaseHeight() {
        if (element.getAttribute('change-height')) {
            setTimeout(function () {
                let lines = ((element.value.match(/\n/g)||[]).length);
                let clientHeight = element.clientHeight;

                while (element.scrollHeight > clientHeight) {
                    clientHeight++;
                    element.style.height = 'auto';
                    element.style.height = clientHeight + 'px';

                    if (element.selectionStart == element.value.length) {
                        element.parentNode.scrollTop = clientHeight;
                    }

                }

                lineHeight = clientHeight / lines;
            });
        }
    }

    function decreaseHeight() {
        if (element.getAttribute('change-height')) {
            setTimeout(function () {
                let lines = ((element.value.match(/\n/g)||[]).length);
                let clientHeight = element.clientHeight;

                while ((lineHeight * lines) < clientHeight) {
                    clientHeight--;
                    element.style.height = 'auto';
                    element.style.height = clientHeight + 'px';

                    if (element.selectionStart == element.value.length) {
                        element.parentNode.scrollTop = clientHeight;
                    }

                }

                lineHeight = clientHeight / lines;
            });
        }
    }
    
    function addActive(list) {
        if (!list || !list.length) return false;

        removeActive(list);

        if (currentFocus >= list.length) currentFocus = 0;

        if (currentFocus < 0) currentFocus = (list.length - 1);

        list[currentFocus].classList.add('autocomplete-active');
    }

    function removeActive(list) {
        if (!list || !list.length) return false;

        for (let i = 0; i < list.length; i++) {
            list[i].classList.remove('autocomplete-active');
        }
    }

    function hasNoOneActive(list) {
        if (!list || !list.length) {

            return true;
        }        

        return false;
    }

    function closeAllLists(elmnt) {
        let list = document.getElementsByClassName('autocomplete-items');

        for (let i = 0; i < list.length; i++) {

            if (elmnt != list[i] && elmnt != element) {
                list[i].parentNode.removeChild(list[i]);
            }

        }
    }

    document.addEventListener('click', function (e) {
        closeAllLists(e.target);
    });
    
}

;

