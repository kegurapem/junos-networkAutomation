
const listUsersNornir = async () => {
    try {
        const response = await fetch('http://127.0.0.1:8000/listusersnornir2/')
        const data = await response.json()
        console.log(response)
        console.log(data)

        let content = ``
        data.usuarios_nornir.forEach((user, index) => {
            content += `
                <tr>
                    <td>${index+1}</td>
                    <td>${user.username}</td>
                    <td>${user.last_name}</td>
                    <td>${user.is_staff}</td>
                </tr>
            `
        })
        tableBody_usersnornir.innerHTML = content
    } catch (ex) {
        alert(ex)
    }
}

window.addEventListener("load", async () => {
    await listUsersNornir()
})