const api_url =
      "http://127.0.0.1:8000"

async function getapi(url) {
    const response = await fetch(url)

    let data = await response.json()
    console.log(data)
    return data
}

function show(data) {
    let HTMLData = `<p>
        Name: ${data.name}
        Surname: ${data.surname}
        Age: ${data.age}
    </p>`
    document.getElementById("data").innerHTML = HTMLData
}

function showUser(data) {
    let HTMLData = `<p>
        Name: ${data.user_name}
        Email: ${data.user_email}
        Password: ${data.user_password}
    </p>`
    document.getElementById("data").innerHTML = HTMLData
}

function showRecipes(data) {
    let HTMLData = `<p>
        Name: ${data.user_name}
        Email: ${data.user_email}
        Password: ${data.user_password}
    </p>`
    document.getElementById("data").innerHTML = HTMLData
}

let data = await getapi(api_url)

showUser(data)