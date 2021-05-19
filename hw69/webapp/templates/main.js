ACTIONS={
    '+':'add',
    '-':'subtract',
    '*':'multiply',
    '/':'divide'
}
function prvDefaultbtns() {
    btns = document.getElementsByClassName('sbmt')
    for (btn of btns) {
        btn.addEventListener("click", function (event) {
            event.preventDefault()
        });
    }
}
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
function set_csrf(){
    const requestURL = 'http://localhost:8000/api/token/'

    function sendRequest(method, url, body = null) {
        const headers = {
            'Content-Type': "application/json",
        }
        return fetch(url, {
            method: method,
            headers: headers
        }).then(response => {
            if (response.ok) {
                return response
            }
            return response.json().then(error => {
                const e = new Error("oops something went wrong")
                e.data = error
                throw e
            })
        })
    }
    sendRequest('GET', requestURL)
        .then(data => {})
        .catch(err => console.log(err))
}
function calc(event) {
    let a = document.getElementById('fnum').value;
    let b = document.getElementById('snum').value;
    let result = document.getElementById('result')

    let requestURL = `http://localhost:8000/api/${ACTIONS[event.currentTarget.dataset.act]}/`

    function sendRequest(method, url, body = null, csrftoken = null) {
        const headers = {
            'Content-Type': "application/json",
            'X-CSRFToken':csrftoken,

        }
        return fetch(url, {
            method: method,
            body: JSON.stringify(body),
            headers: headers
        }).then(response => {
            return response.json()
        })
    }
    body = {
        A: a,
        B: b,
    }
    console.log('body=',body)

    let csrftoken = getCookie('csrftoken')
    console.log('token=',csrftoken)
    sendRequest('POST', requestURL, body,csrftoken )
        .then(data => {
            console.log(data)
            if (data.answer){
                result.innerText=data['answer']
                result.className=('text-success')
            }
            else if (data.error){
                result.innerText=data['error']
                result.className=('text-danger')
            }

        })
        .catch(err => {
            console.log('chek3')
            {#console.log(err)#}
            result.innerText=data['error']
            result.className=('text-danger')

        })
}
window.addEventListener('load', set_csrf)
window.addEventListener('load', prvDefaultbtns)