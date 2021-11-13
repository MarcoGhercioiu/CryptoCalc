function searchTag(){
    var tag = document.getElementById("query").value;
    
    let userInfo = {
        'tag': tag
    }
    const request = new XMLHttpRequest()
    request.open('POST', '/searchTag/${JSON.stringify(userInfo)}')
    request.onload = () => {
        const flaskMessage = request.responseText
        console.log(flaskMessage)
    }
    request.send()
}
